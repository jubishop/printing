from __future__ import annotations

import hashlib
import math
import os
import struct
import zipfile
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET

import cadquery as cq
from OCP.StlAPI import StlAPI_Reader
from OCP.TopoDS import TopoDS_Shape

from vibecad import cached_part, parameter


PROJECT_DIR = Path(__file__).resolve().parent
PRINTING_REPO = Path(os.environ.get("PRINTING_REPO", "/Users/jubi/projects/printing"))
PRIVATE_DIR = PRINTING_REPO / ".local/models/stick-drift-travel-protector-taller"
SOURCE_3MF = PRIVATE_DIR / "original-body6.3mf"
SOURCE_OBJECT_ID = "1"
SOURCE_SHA256 = "e3f17d92236931bde4611f653aac2a81c98ce5dbbaf0e56460b08df157269ff3"

LOW_COLOR = (0.16, 0.58, 0.92)
HIGH_COLOR = (0.95, 0.55, 0.12)

low_height = parameter(5.0, 4.0, 7.0, 0.25, "Low pair height (mm)")
high_height = parameter(6.0, 4.0, 8.0, 0.25, "High pair height (mm)")
column_spacing = parameter(34.0, 30.0, 45.0, 1.0, "Column spacing (mm)")
row_spacing = parameter(34.0, 30.0, 45.0, 1.0, "Row spacing (mm)")


def build(
    low_height: float,
    high_height: float,
    column_spacing: float,
    row_spacing: float,
) -> None:
    """Show two of each height in their shared-plate arrangement."""
    x = column_spacing / 2
    y = row_spacing / 2
    low_left(low_height, -x, -y, SOURCE_SHA256)
    low_right(low_height, x, -y, SOURCE_SHA256)
    high_left(high_height, -x, y, SOURCE_SHA256)
    high_right(high_height, x, y, SOURCE_SHA256)


@cached_part("5 mm - left", LOW_COLOR)
def low_left(height: float, x: float, y: float, source_sha256: str) -> cq.Shape:
    return _protector_shape(height, x, y, source_sha256)


@cached_part("5 mm - right", LOW_COLOR)
def low_right(height: float, x: float, y: float, source_sha256: str) -> cq.Shape:
    return _protector_shape(height, x, y, source_sha256)


@cached_part("6 mm - left", HIGH_COLOR)
def high_left(height: float, x: float, y: float, source_sha256: str) -> cq.Shape:
    return _protector_shape(height, x, y, source_sha256)


@cached_part("6 mm - right", HIGH_COLOR)
def high_right(height: float, x: float, y: float, source_sha256: str) -> cq.Shape:
    return _protector_shape(height, x, y, source_sha256)


def _protector_shape(height: float, x: float, y: float, source_sha256: str) -> cq.Shape:
    if _sha256(SOURCE_3MF) != source_sha256:
        raise RuntimeError("The private MakerWorld source file does not match the inspected download")

    vertices, triangles = _load_source_mesh(SOURCE_3MF, SOURCE_OBJECT_ID)
    printable_vertices, printable_triangles = _make_printable(vertices, triangles, height)
    generated_dir = PROJECT_DIR / ".vibecad/generated"
    generated_dir.mkdir(parents=True, exist_ok=True)
    stl_path = generated_dir / f"protector-{height:.2f}mm.stl"
    _write_binary_stl(stl_path, printable_vertices, printable_triangles)
    shape = TopoDS_Shape()
    if not StlAPI_Reader().Read(shape, str(stl_path)) or shape.IsNull():
        raise RuntimeError(f"Could not load generated STL: {stl_path}")
    return cq.Shape(shape).translate((x, y, 0))


def export_deliverables() -> dict[str, object]:
    """Export separate STLs and one four-object 3MF plate."""
    if _sha256(SOURCE_3MF) != SOURCE_SHA256:
        raise RuntimeError("The private MakerWorld source file does not match the inspected download")

    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    source_vertices, source_triangles = _load_source_mesh(SOURCE_3MF, SOURCE_OBJECT_ID)
    meshes: dict[float, tuple[list[tuple[float, float, float]], list[tuple[int, int, int]]]] = {}
    outputs: dict[str, object] = {}

    for height in (5.0, 6.0):
        mesh = _make_printable(source_vertices, source_triangles, height)
        meshes[height] = mesh
        stl_path = PRIVATE_DIR / f"stick-drift-travel-protector-{height:.0f}mm.stl"
        _write_binary_stl(stl_path, *mesh)
        outputs[f"stl_{height:.0f}mm"] = str(stl_path)

    placements = [
        ("protector 5mm A", 5.0, -17.0, -17.0),
        ("protector 5mm B", 5.0, 17.0, -17.0),
        ("protector 6mm A", 6.0, -17.0, 17.0),
        ("protector 6mm B", 6.0, 17.0, 17.0),
    ]
    plate_path = PRIVATE_DIR / "stick-drift-travel-protectors-2x5mm-2x6mm.3mf"
    _write_3mf_plate(plate_path, meshes, placements)
    outputs["plate_3mf"] = str(plate_path)

    checks = {}
    for height, (vertices, triangles) in meshes.items():
        checks[f"{height:.0f}mm"] = _mesh_checks(vertices, triangles)
    outputs["checks"] = checks
    return outputs


def _load_source_mesh(
    source: Path,
    object_id: str,
) -> tuple[list[tuple[float, float, float]], list[tuple[int, int, int]]]:
    with zipfile.ZipFile(source) as archive:
        root = ET.fromstring(archive.read("3D/3dmodel.model"))
    ns = {"m": "http://schemas.microsoft.com/3dmanufacturing/core/2015/02"}
    mesh = root.find(f".//m:object[@id='{object_id}']/m:mesh", ns)
    if mesh is None:
        raise RuntimeError(f"Mesh object {object_id} not found in {source}")

    vertices = [
        (float(v.attrib["x"]), float(v.attrib["y"]), float(v.attrib["z"]))
        for v in mesh.findall("./m:vertices/m:vertex", ns)
    ]
    triangles = [
        (int(t.attrib["v1"]), int(t.attrib["v2"]), int(t.attrib["v3"]))
        for t in mesh.findall("./m:triangles/m:triangle", ns)
    ]
    return vertices, triangles


def _make_printable(
    vertices: list[tuple[float, float, float]],
    triangles: list[tuple[int, int, int]],
    target_height: float,
) -> tuple[list[tuple[float, float, float]], list[tuple[int, int, int]]]:
    """Keep XY unchanged, preserve the original print face, and change only Z height."""
    z_min = min(v[2] for v in vertices)
    z_max = max(v[2] for v in vertices)
    scale = target_height / (z_max - z_min)

    # The MakerWorld plate prints the source mesh with Z inverted. Converting here
    # leaves that exact face at Z=0 and scales upward from the bed.
    printable_vertices = [(x, y, (z_max - z) * scale) for x, y, z in vertices]
    # Z inversion changes handedness, so reverse winding to retain outward faces.
    printable_triangles = [(a, c, b) for a, b, c in triangles]
    return printable_vertices, printable_triangles


def _write_binary_stl(
    path: Path,
    vertices: list[tuple[float, float, float]],
    triangles: list[tuple[int, int, int]],
) -> None:
    header = b"Personal-use taller variant of MakerWorld model 1449609"
    with path.open("wb") as stream:
        stream.write(header.ljust(80, b"\0"))
        stream.write(struct.pack("<I", len(triangles)))
        for a, b, c in triangles:
            p, q, r = vertices[a], vertices[b], vertices[c]
            normal = _normal(p, q, r)
            stream.write(struct.pack("<12fH", *normal, *p, *q, *r, 0))


def _write_3mf_plate(
    path: Path,
    meshes: dict[float, tuple[list[tuple[float, float, float]], list[tuple[int, int, int]]]],
    placements: list[tuple[str, float, float, float]],
) -> None:
    core = "http://schemas.microsoft.com/3dmanufacturing/core/2015/02"
    ET.register_namespace("", core)
    model = ET.Element(f"{{{core}}}model", {"unit": "millimeter", "{http://www.w3.org/XML/1998/namespace}lang": "en-US"})
    ET.SubElement(model, f"{{{core}}}metadata", {"name": "Application"}).text = "Codex/CadQuery private personal-use variant"
    ET.SubElement(model, f"{{{core}}}metadata", {"name": "Title"}).text = "Stick drift travel protectors - 2x 5mm and 2x 6mm"
    ET.SubElement(model, f"{{{core}}}metadata", {"name": "Designer"}).text = "PolyNova; height-only personal-use adaptation for Jubi"
    ET.SubElement(model, f"{{{core}}}metadata", {"name": "License"}).text = "MakerWorld Exclusive License - do not redistribute outside MakerWorld"
    resources = ET.SubElement(model, f"{{{core}}}resources")
    build = ET.SubElement(model, f"{{{core}}}build")

    for object_id, (name, height, x, y) in enumerate(placements, start=1):
        vertices, triangles = meshes[height]
        obj = ET.SubElement(resources, f"{{{core}}}object", {"id": str(object_id), "type": "model", "name": name})
        mesh = ET.SubElement(obj, f"{{{core}}}mesh")
        vertex_root = ET.SubElement(mesh, f"{{{core}}}vertices")
        for vx, vy, vz in vertices:
            ET.SubElement(vertex_root, f"{{{core}}}vertex", {"x": _fmt(vx), "y": _fmt(vy), "z": _fmt(vz)})
        triangle_root = ET.SubElement(mesh, f"{{{core}}}triangles")
        for a, b, c in triangles:
            ET.SubElement(triangle_root, f"{{{core}}}triangle", {"v1": str(a), "v2": str(b), "v3": str(c)})
        ET.SubElement(
            build,
            f"{{{core}}}item",
            {"objectid": str(object_id), "transform": f"1 0 0 0 1 0 0 0 1 {_fmt(x)} {_fmt(y)} 0", "printable": "1"},
        )

    model_xml = ET.tostring(model, encoding="utf-8", xml_declaration=True)
    content_types = b'''<?xml version="1.0" encoding="UTF-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/>
</Types>'''
    relationships = b'''<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Target="/3D/3dmodel.model" Id="rel-1" Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/>
</Relationships>'''
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("[Content_Types].xml", content_types)
        archive.writestr("_rels/.rels", relationships)
        archive.writestr("3D/3dmodel.model", model_xml)


def _mesh_checks(
    vertices: list[tuple[float, float, float]],
    triangles: list[tuple[int, int, int]],
) -> dict[str, object]:
    edge_counts: Counter[tuple[int, int]] = Counter()
    signed_volume = 0.0
    for a, b, c in triangles:
        for u, v in ((a, b), (b, c), (c, a)):
            edge_counts[tuple(sorted((u, v)))] += 1
        p, q, r = vertices[a], vertices[b], vertices[c]
        signed_volume += (
            p[0] * (q[1] * r[2] - q[2] * r[1])
            - p[1] * (q[0] * r[2] - q[2] * r[0])
            + p[2] * (q[0] * r[1] - q[1] * r[0])
        ) / 6.0

    bounds = [
        [min(v[axis] for v in vertices), max(v[axis] for v in vertices)]
        for axis in range(3)
    ]
    return {
        "vertices": len(vertices),
        "triangles": len(triangles),
        "boundary_edges": sum(count == 1 for count in edge_counts.values()),
        "nonmanifold_edges": sum(count != 2 for count in edge_counts.values()),
        "signed_volume_mm3": round(signed_volume, 3),
        "bounds_mm": [[round(value, 3) for value in pair] for pair in bounds],
    }


def _normal(
    p: tuple[float, float, float],
    q: tuple[float, float, float],
    r: tuple[float, float, float],
) -> tuple[float, float, float]:
    ux, uy, uz = q[0] - p[0], q[1] - p[1], q[2] - p[2]
    vx, vy, vz = r[0] - p[0], r[1] - p[1], r[2] - p[2]
    nx, ny, nz = uy * vz - uz * vy, uz * vx - ux * vz, ux * vy - uy * vx
    length = math.sqrt(nx * nx + ny * ny + nz * nz)
    if length == 0:
        return 0.0, 0.0, 0.0
    return nx / length, ny / length, nz / length


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _fmt(value: float) -> str:
    return f"{value:.6f}".rstrip("0").rstrip(".")


if __name__ == "__main__":
    print(export_deliverables())
