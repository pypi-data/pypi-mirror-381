
import re
from typing import Any
from ..pcb import PCB, RouteException
from ...material import Material, PEC
from ...cs import GCS, CoordinateSystem
from loguru import logger
from math import hypot

try: 
    import ezdxf
    from ezdxf.recover import readfile as recover_readfile
    from ezdxf.path import make_path, from_hatch
except ImportError as e:
    logger.error('Cannot find the required ezdxf library. Install using: pip install ezdxf')
    raise e

INSUNITS_TO_NAME = {
    0: "unitless",
    1: "inch",
    2: "foot",
    3: "mile",
    4: "millimeter",
    5: "centimeter",
    6: "meter",
    7: "kilometer",
    8: "microinch",
    9: "mil",          # thousandth of an inch
    10: "yard",
    11: "angstrom",
    12: "nanometer",
    13: "micrometer",
    14: "decimeter",
    15: "decameter",
    16: "hectometer",
    17: "gigameter",
    18: "astronomical unit",
    19: "light year",
    20: "parsec",
}

# scale factor: drawing units -> millimeters
INSUNITS_TO_MM = {
    0: 1.0,           # unitless; treat as mm by convention
    1: 25.4,
    2: 304.8,
    3: 1609344.0,
    4: 1.0,
    5: 10.0,
    6: 1000.0,
    7: 1_000_000.0,
    8: 25.4e-6,
    9: 0.0254,
    10: 914.4,
    11: 1e-7,
    12: 1e-6,
    13: 1e-3,
    14: 100.0,
    15: 10_000.0,
    16: 100_000.0,
    17: 1e12,
    18: 1.495978707e14,     # AU in mm
    19: 9.460730472e18,     # ly in mm
    20: 3.085677581e19,     # pc in mm
}

def cluster_values(values, tol):
    """Return [(center, count), ...] clustering sorted values by tolerance."""
    if not values:
        return []
    values = sorted(values)
    clusters = [[values[0]]]
    for v in values[1:]:
        if abs(v - clusters[-1][-1]) <= tol:
            clusters[-1].append(v)
        else:
            clusters.append([v])
    out = []
    for c in clusters:
        out.append((sum(c)/len(c), len(c)))
    return out

STACKUP_TOKENS = [
    r"fr-?4", r"rogers ?\d+", r"core", r"prepreg", r"dielectric",
    r"cu(?:\W|$)|copper", r"\b1\.?6\s*mm\b", r"\b0\.?8\s*mm\b",
    r"\b[12]\s*oz\b", r"\b35\s*µ?m\b", r"\b70\s*µ?m\b",
    r"stack[- ]?up", r"layer\s*\d+", r"pcb", r"thickness",
]

def inspect_pcb_from_dxf(
    filename: str,
    flatten_tol: float = 0.25,    # curve flattening tolerance (drawing units)
    z_tol: float | None = None,   # cluster tolerance for Z (drawing units); default auto
    layer_filter: str | None = None,
):
    """
    Returns a dict with:
      {
        'units': {'code': int, 'name': str, 'to_mm': float},
        'z_levels': [{'z': float, 'count': int}],           # in drawing units
        'thickness_units': 'same as units',
        'thickness': float,                                  # in drawing units
        'thickness_mm': float,                               # convenience
        'notes': {'materials': [...], 'raw_text_hits': [...]}
      }
    """
    doc, auditor = recover_readfile(filename)
    msp = doc.modelspace()

    # Units
    code = int(doc.header.get("$INSUNITS", 0))
    unit_name = INSUNITS_TO_NAME.get(code, f"unknown({code})")
    to_mm = INSUNITS_TO_MM.get(code, 1.0)

    # Gather geometry Zs (WCS), also consider entity.dxf.elevation as fallback
    z_values = []

    def on_layer(e) -> bool:
        return layer_filter is None or e.dxf.layer == layer_filter

    for e in msp:
        if not on_layer(e):
            continue
        dxtype = e.dxftype()
        paths = []
        try:
            if dxtype in ("HATCH", "MPOLYGON"):
                paths = list(from_hatch(e))
            else:
                paths = [make_path(e)]
        except TypeError:
            # skip unsupported entity types
            pass
        except Exception:
            pass

        for p in paths:
            subs = p.sub_paths() if getattr(p, "has_sub_paths", False) and p.has_sub_paths else [p]
            for sp in subs:
                try:
                    verts = list(sp.flattening(distance=flatten_tol))
                except Exception:
                    continue
                for v in verts:
                    # v may be Vec2 or Vec3; handle both
                    z = getattr(v, "z", None)
                    if z is None:
                        # fallback to entity elevation if available
                        z = float(getattr(e.dxf, "elevation", 0.0))
                    z_values.append(float(z))

        # Entities with explicit THICKNESS (rare but possible)
        thick = getattr(e.dxf, "thickness", None)
        if thick not in (None, 0):
            # If an entity is extruded, its "top" would be at elevation+thickness along normal.
            # We can't reliably map OCS normal here; just record the magnitude as a hint.
            pass

    # Cluster Zs
    auto_tol = (1e-6 if to_mm >= 1.0 else 1e-6 / to_mm)  # ~1 nm in mm space → tiny in most units
    ztol = z_tol if z_tol is not None else auto_tol
    z_clusters = cluster_values(z_values, tol=ztol)
    z_levels = [{"z": z, "count": n} for z, n in z_clusters]

    # Thickness from geometry (only meaningful if multiple distinct Zs)
    if z_values:
        zmin, zmax = min(z_values), max(z_values)
        thickness = zmax - zmin
    else:
        zmin = zmax = thickness = 0.0

    # Parse material/thickness hints from TEXT/MTEXT
    material_hits = set()
    raw_text_hits = []
    token_re = re.compile("|".join(STACKUP_TOKENS), re.IGNORECASE)

    for e in msp.query("TEXT MTEXT"):
        try:
            text = e.dxf.text if e.dxftype() == "TEXT" else e.text
        except Exception:
            continue
        if not text:
            continue
        if token_re.search(text):
            raw_text_hits.append(text.strip())
            # simple keyword extraction
            for kw in ["FR4", "Rogers", "core", "prepreg", "copper", "stackup", "thickness", "oz", "µm", "um", "mm"]:
                if re.search(kw, text, re.IGNORECASE):
                    material_hits.add(kw.upper())

    return {
        "units": {"code": code, "name": unit_name, "to_mm": to_mm},
        "z_levels": z_levels,
        "thickness_units": unit_name,
        "thickness": thickness,
        "thickness_mm": thickness * to_mm,
        "notes": {
            "materials": sorted(material_hits),
            "raw_text_hits": raw_text_hits[:50],  # cap to keep output sane
            "comment": (
                "Single Z level detected; geometry alone cannot determine PCB thickness."
                if len(z_levels) <= 1 else
                "Thickness estimated from min/max Z across all geometry."
            )
        },
    }

def path_items_with_semantics(e, p, distance=0.25):
    """Yield dicts describing each sub-path with geometry + semantics we can infer."""
    subs = p.sub_paths() if getattr(p, "has_sub_paths", False) and p.has_sub_paths else [p]
    for sp in subs:
        verts = list(sp.flattening(distance=distance))
        if len(verts) < 2:
            continue

        # geometry in XY (keep Z if you like)
        pts = [(v.x, v.y) for v in verts]
        is_closed = pts[0] == pts[-1]

        item = {
            "layer": e.dxf.layer,
            "entity": e.dxftype(),
            "handle": e.dxf.handle,
            "is_closed": is_closed,
            "points": pts if is_closed else None,       # polygon ring for closed shapes
            "start": None,
            "end": None,
            "length": None,                             # centerline length for open paths
            "width": None,                              # LWPOLYLINE width if available
        }

        if not is_closed:
            item["start"] = pts[0]
            item["end"]   = pts[-1]
            # polyline centerline length
            item["length"] = sum(
                hypot(x2 - x1, y2 - y1) for (x1, y1), (x2, y2) in zip(pts, pts[1:])
            )

        # Preserve potential trace width info from LWPOLYLINE
        if e.dxftype() == "LWPOLYLINE":
            cw = getattr(e.dxf, "const_width", None)
            if cw not in (None, 0):
                item["width"] = float(cw)
            else:
                # per-vertex widths (rare but possible)
                try:
                    item["widths"] = [(v[0], v[1]) for v in zip(e.get_start_widths(), e.get_end_widths())]
                except Exception:
                    pass

        yield item
        
def extract_polygons_with_meta(
    filename: str,
    layer: str | None = None,
    distance: float = 0.25,
    skip_open: bool = True,
) -> dict[str, Any]:
    """
    Returns a list of dicts:
      {
        'ring': [(x, y), ...],         # closed ring
        'layer': 'LayerName',
        'z': 12.34,                    # representative height (median Z of ring)
        'entity': 'LWPOLYLINE' | ...,
        'handle': 'ABCD'
      }
    """
    doc, auditor = recover_readfile(filename)
    msp = doc.modelspace()

    def on_layer(e) -> bool:
        return layer is None or e.dxf.layer == layer

    items = []

    for e in msp:
        if not on_layer(e):
            continue

        dxtype = e.dxftype()
        paths = []
        try:
            if dxtype in ("HATCH", "MPOLYGON"):
                paths = list(from_hatch(e))
            else:
                paths = [make_path(e)]
        except TypeError:
            continue
        except Exception:
            continue

        for p in paths:
            subs = p.sub_paths() if p.has_sub_paths else [p]
            for sp in subs:
                
                verts = list(sp.flattening(distance=distance))  # Vec3 in WCS
                if len(verts) < 2:
                    continue

                # ensure not closed
                if (verts[0].x, verts[0].y) == (verts[-1].x, verts[-1].y):
                    verts = verts[:-1]

                # ring in XY (your original target), but also compute a Z for reference
                ring_xy = [(v.x, v.y) for v in verts]
                zs = sorted(v.z for v in verts)
                z = zs[len(zs)//2] if zs else float(getattr(e.dxf, "elevation", 0.0))  # median Z

                items.append({
                    "ring": ring_xy,
                    "layer": e.dxf.layer,
                    "z": float(z),
                    "entity": dxtype,
                    "handle": e.dxf.handle,
                })

    return items


def import_dxf(filename: str, 
               material: Material, 
               thickness: float | None = None,
               unit: float | None = None,
               cs: CoordinateSystem | None = GCS,
               trace_material: Material = PEC) -> PCB:
    
    polies = extract_polygons_with_meta(filename)
    prop = inspect_pcb_from_dxf(filename)
    
    if prop['units']['name'] == 'unitless':
        if unit is None:
            raise RouteException(f'Cannot generate PCB because the unit is not found in the DXF file or provided in the import_dxf function.')
        pcb_unit = unit
    else:
        pcb_unit = 0.001 * prop['units']['to_mm']
    
    if prop['thickness'] == 0.0:
        if thickness is None:
            raise RouteException(f'Cannot generate PCB because no thickness is found int he DXF file and none is provided in the import_dxf function.')
        pcb_thickness = thickness
    else:
        pcb_thickness = 0.001 * prop['thickness_mm'] / pcb_unit
    
    if cs is None:
        cs = GCS
    
    zs = sorted(list(set([pol['z'] for pol in polies])))
    pcb = PCB(pcb_thickness, pcb_unit, cs, material=material, trace_material=trace_material)
    
    for poly in polies:
        xs, ys = zip(*poly['ring'])
        z = poly['z']
        zs.append(z)
        xs = [x for x in xs]
        ys = [y for y in ys]
        
        pcb.add_poly(xs, ys, z=z, name=poly['handle'])
    return pcb
    