from __future__ import annotations

import contextvars
import functools
import hashlib
import inspect
import json
import os
import pathlib
import shutil
import struct
import time
from dataclasses import dataclass
from typing import Any, Callable, Iterable

print("Importing CadQuery/OCP: this can take a few minutes on a cold start.", flush=True)
import cadquery as cq
print("Imported CadQuery/OCP.", flush=True)


Color = tuple[float, float, float]
Scale3D = float | tuple[float, float, float]

_active_context: contextvars.ContextVar["BuildContext | None"] = contextvars.ContextVar(
    "vibecad_build_context", default=None
)


@dataclass(frozen=True)
class Parameter:
    default: float
    min: float
    max: float
    step: float = 1.0
    label: str | None = None


@dataclass
class Part:
    name: str
    color: Color
    geometry: cq.Workplane | None
    cache_key: str
    stl_path: pathlib.Path
    step_path: pathlib.Path


def parameter(
    default: float, min: float, max: float, step: float = 1.0, label: str | None = None
) -> Parameter:
    return Parameter(default=default, min=min, max=max, step=step, label=label)


def cached_part(name: str, color: Color) -> Callable[[Callable[..., cq.Workplane]], Callable[..., cq.Workplane]]:
    def decorate(func: Callable[..., cq.Workplane]) -> Callable[..., cq.Workplane]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> cq.Workplane:
            ctx = _active_context.get()
            if ctx is None:
                return func(*args, **kwargs)
            return ctx.resolve_part(func, name, color, args, kwargs)

        wrapper._vibecad_part_name = name  # type: ignore[attr-defined]
        wrapper._vibecad_part_color = color  # type: ignore[attr-defined]
        return wrapper

    return decorate


def stl_part(name: str, color: Color, source_path: str | pathlib.Path, scale: Scale3D = 1.0) -> cq.Workplane | None:
    path = pathlib.Path(source_path)
    ctx = _active_context.get()
    if ctx is None:
        return _import_stl(path)
    return ctx.resolve_stl_part(name, color, path, scale)


class BuildContext:
    def __init__(self, cache_dir: pathlib.Path):
        self.cache_dir = cache_dir
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.parts: list[Part] = []

    def __enter__(self) -> "BuildContext":
        self._token = _active_context.set(self)
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any) -> None:
        _active_context.reset(self._token)

    def resolve_part(
        self,
        func: Callable[..., cq.Workplane],
        name: str,
        color: Color,
        args: tuple[Any, ...],
        kwargs: dict[str, Any],
    ) -> cq.Workplane:
        key = self._cache_key(func, name, args, kwargs)
        part_dir = self.cache_dir / key
        part_dir.mkdir(parents=True, exist_ok=True)
        step_path = part_dir / f"{key}.step"
        stl_path = part_dir / f"{key}.stl"

        if step_path.exists():
            geometry = cq.importers.importStep(str(step_path))
        else:
            geometry = func(*args, **kwargs)
            tmp_step = _tmp_path(step_path)
            cq.exporters.export(geometry, str(tmp_step), exportType="STEP")
            if step_path.exists():
                tmp_step.unlink(missing_ok=True)
            else:
                tmp_step.replace(step_path)

        if not stl_path.exists() or stl_path.stat().st_mtime < step_path.stat().st_mtime:
            tmp_stl = _tmp_path(stl_path)
            cq.exporters.export(geometry, str(tmp_stl), exportType="STL", tolerance=0.08, angularTolerance=0.1)
            if stl_path.exists() and stl_path.stat().st_mtime >= step_path.stat().st_mtime:
                tmp_stl.unlink(missing_ok=True)
            else:
                tmp_stl.replace(stl_path)

        part = Part(
            name=name,
            color=color,
            geometry=geometry,
            cache_key=key,
            stl_path=stl_path,
            step_path=step_path,
        )
        self.parts.append(part)
        return geometry

    def resolve_stl_part(
        self,
        name: str,
        color: Color,
        source_path: pathlib.Path,
        scale: Scale3D,
    ) -> cq.Workplane | None:
        scale_xyz = _normalize_scale(scale)
        source_path = source_path.resolve()
        source_stat = source_path.stat()
        key = self._stl_cache_key(name, source_path, source_stat.st_size, source_stat.st_mtime_ns, scale_xyz)
        part_dir = self.cache_dir / key
        part_dir.mkdir(parents=True, exist_ok=True)
        stl_path = part_dir / f"{key}.stl"

        if not stl_path.exists():
            tmp_stl = _tmp_path(stl_path)
            _write_scaled_stl(source_path, tmp_stl, scale_xyz)
            if stl_path.exists():
                tmp_stl.unlink(missing_ok=True)
            else:
                tmp_stl.replace(stl_path)

        part = Part(
            name=name,
            color=color,
            geometry=None,
            cache_key=key,
            stl_path=stl_path,
            step_path=stl_path,
        )
        self.parts.append(part)
        return None

    def clear(self) -> None:
        if self.cache_dir.exists():
            shutil.rmtree(self.cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _cache_key(
        self,
        func: Callable[..., cq.Workplane],
        name: str,
        args: tuple[Any, ...],
        kwargs: dict[str, Any],
    ) -> str:
        payload = {
            "part": name,
            "function": func.__qualname__,
            "source_sha256": _source_hash(func),
            "signature": _bound_arguments(func, args, kwargs),
        }
        digest = hashlib.sha256(json.dumps(payload, sort_keys=True).encode("utf-8")).hexdigest()[:20]
        return f"{_slug(name)}-{digest}"

    def _stl_cache_key(
        self,
        name: str,
        source_path: pathlib.Path,
        source_size: int,
        source_mtime_ns: int,
        scale: tuple[float, float, float],
    ) -> str:
        payload = {
            "part": name,
            "source": str(source_path),
            "source_size": source_size,
            "source_mtime_ns": source_mtime_ns,
            "scale": scale,
        }
        digest = hashlib.sha256(json.dumps(payload, sort_keys=True).encode("utf-8")).hexdigest()[:20]
        return f"{_slug(name)}-{digest}"


def collect_parameters(module: Any) -> dict[str, Parameter]:
    return {
        name: value
        for name, value in vars(module).items()
        if isinstance(value, Parameter) and not name.startswith("_")
    }


def combine(parts: Iterable[Part]) -> cq.Compound:
    shapes: list[cq.Shape] = []
    for part in parts:
        geometry = part.geometry if part.geometry is not None else _import_stl(part.stl_path)
        vals = geometry.vals()
        shapes.extend(value for value in vals if isinstance(value, cq.Shape))
    if not shapes:
        raise ValueError("Model did not create any CadQuery shapes")
    return cq.Compound.makeCompound(shapes)


def export_compound(parts: Iterable[Part], path: pathlib.Path, export_type: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    compound = combine(parts)
    tmp_path = _tmp_path(path)
    cq.exporters.export(compound, str(tmp_path), exportType=export_type)
    tmp_path.replace(path)


def _bound_arguments(func: Callable[..., cq.Workplane], args: tuple[Any, ...], kwargs: dict[str, Any]) -> Any:
    signature = inspect.signature(func)
    bound = signature.bind(*args, **kwargs)
    bound.apply_defaults()
    return _jsonable(bound.arguments)


def _source_hash(func: Callable[..., cq.Workplane]) -> str:
    source_path = inspect.getsourcefile(func)
    if not source_path:
        return ""
    try:
        content = pathlib.Path(source_path).read_bytes()
    except OSError:
        return ""
    return hashlib.sha256(content).hexdigest()


def _jsonable(value: Any) -> Any:
    if isinstance(value, pathlib.Path):
        return str(value)
    if isinstance(value, dict):
        return {str(key): _jsonable(value[key]) for key in sorted(value)}
    if isinstance(value, (tuple, list)):
        return [_jsonable(item) for item in value]
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return repr(value)


def _slug(value: str) -> str:
    chars = [char.lower() if char.isalnum() else "-" for char in value.strip()]
    slug = "".join(chars).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug or "part"


def _tmp_path(path: pathlib.Path) -> pathlib.Path:
    return path.with_name(f"{path.name}.{os.getpid()}.{time.time_ns()}.tmp")


def _import_stl(path: pathlib.Path) -> cq.Workplane:
    from OCP.StlAPI import StlAPI_Reader
    from OCP.TopoDS import TopoDS_Shape

    shape = TopoDS_Shape()
    if not StlAPI_Reader().Read(shape, str(path)) or shape.IsNull():
        raise RuntimeError(f"Could not import STL: {path}")
    return cq.Workplane("XY").add(cq.Shape.cast(shape))


def _normalize_scale(scale: Scale3D) -> tuple[float, float, float]:
    if isinstance(scale, (int, float)):
        scale_xyz = (float(scale), float(scale), float(scale))
    else:
        if len(scale) != 3:
            raise ValueError("STL scale must be a number or a 3-tuple")
        scale_xyz = (float(scale[0]), float(scale[1]), float(scale[2]))
    if any(value <= 0 for value in scale_xyz):
        raise ValueError("STL scale must be greater than zero")
    return scale_xyz


def _write_scaled_stl(source_path: pathlib.Path, target_path: pathlib.Path, scale: tuple[float, float, float]) -> None:
    if scale == (1.0, 1.0, 1.0):
        shutil.copy2(source_path, target_path)
        return
    if _is_binary_stl(source_path):
        _write_scaled_binary_stl(source_path, target_path, scale)
        return
    _write_scaled_ascii_stl(source_path, target_path, scale)


def _is_binary_stl(path: pathlib.Path) -> bool:
    size = path.stat().st_size
    if size < 84:
        return False
    with path.open("rb") as file:
        file.seek(80)
        triangle_count = struct.unpack("<I", file.read(4))[0]
    return size == 84 + triangle_count * 50


def _write_scaled_binary_stl(source_path: pathlib.Path, target_path: pathlib.Path, scale: tuple[float, float, float]) -> None:
    with source_path.open("rb") as source, target_path.open("wb") as target:
        header = source.read(84)
        target.write(header)
        while True:
            triangle = source.read(50)
            if not triangle:
                break
            if len(triangle) != 50:
                raise ValueError(f"Invalid binary STL triangle record in {source_path}")
            values = list(struct.unpack("<12fH", triangle))
            normal = _scaled_normal(values[0], values[1], values[2], scale)
            values[0], values[1], values[2] = normal
            for index in range(3, 12, 3):
                values[index] *= scale[0]
                values[index + 1] *= scale[1]
                values[index + 2] *= scale[2]
            target.write(struct.pack("<12fH", *values))


def _write_scaled_ascii_stl(source_path: pathlib.Path, target_path: pathlib.Path, scale: tuple[float, float, float]) -> None:
    with source_path.open("r", encoding="utf-8", errors="replace") as source, target_path.open(
        "w", encoding="utf-8"
    ) as target:
        for line in source:
            stripped = line.lstrip()
            indent = line[: len(line) - len(stripped)]
            if stripped.startswith("vertex "):
                _, x, y, z = stripped.split()[:4]
                target.write(
                    f"{indent}vertex {float(x) * scale[0]:.9g} {float(y) * scale[1]:.9g} {float(z) * scale[2]:.9g}\n"
                )
            elif stripped.startswith("facet normal "):
                _, _, nx, ny, nz = stripped.split()[:5]
                normal = _scaled_normal(float(nx), float(ny), float(nz), scale)
                target.write(
                    f"{indent}facet normal {normal[0]:.9g} {normal[1]:.9g} {normal[2]:.9g}\n"
                )
            else:
                target.write(line)


def _scaled_normal(nx: float, ny: float, nz: float, scale: tuple[float, float, float]) -> tuple[float, float, float]:
    normal = (nx / scale[0], ny / scale[1], nz / scale[2])
    length = (normal[0] ** 2 + normal[1] ** 2 + normal[2] ** 2) ** 0.5
    if length == 0:
        return (nx, ny, nz)
    return (normal[0] / length, normal[1] / length, normal[2] / length)
