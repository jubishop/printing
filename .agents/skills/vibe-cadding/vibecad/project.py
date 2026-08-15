from __future__ import annotations

import importlib.util
import json
import os
import pathlib
import time
from dataclasses import dataclass
from types import ModuleType
from typing import Any

from .core import BuildContext, Parameter, Part, collect_parameters


@dataclass
class Project:
    model_path: pathlib.Path
    state_dir: pathlib.Path
    cache_dir: pathlib.Path
    params_path: pathlib.Path
    exports_dir: pathlib.Path
    captures_dir: pathlib.Path

    @classmethod
    def from_model_path(cls, model_path: pathlib.Path) -> "Project":
        model_path = model_path.resolve()
        state_dir = model_path.parent / ".vibecad"
        return cls(
            model_path=model_path,
            state_dir=state_dir,
            cache_dir=state_dir / "part-cache",
            params_path=state_dir / "model_params.json",
            exports_dir=state_dir / "exports",
            captures_dir=state_dir / "captures",
        )

    def ensure_dirs(self) -> None:
        self.state_dir.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.exports_dir.mkdir(parents=True, exist_ok=True)
        self.captures_dir.mkdir(parents=True, exist_ok=True)


def load_model(model_path: pathlib.Path) -> ModuleType:
    module_name = f"vibecad_model_{model_path.stat().st_mtime_ns}_{time.time_ns()}"
    spec = importlib.util.spec_from_file_location(module_name, model_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load model from {model_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_param_state(project: Project, module: ModuleType) -> dict[str, Any]:
    defaults = collect_parameters(module)
    existing = _read_json(project.params_path)
    params: dict[str, Any] = {}

    for name, spec in defaults.items():
        saved = existing.get(name, {}) if isinstance(existing.get(name), dict) else {}
        value = float(saved.get("value", spec.default))
        minimum = float(saved.get("min", spec.min))
        maximum = float(saved.get("max", spec.max))
        step = float(saved.get("step", spec.step))
        if maximum <= minimum:
            maximum = minimum + step
        value = max(minimum, min(maximum, value))
        params[name] = {
            "value": value,
            "min": minimum,
            "max": maximum,
            "step": step,
            "label": saved.get("label", spec.label or _labelize(name)),
        }

    save_param_state(project, params)
    return params


def save_param_state(project: Project, params: dict[str, Any]) -> None:
    project.params_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = project.params_path.with_name(
        f"{project.params_path.name}.{os.getpid()}.{time.time_ns()}.tmp"
    )
    tmp_path.write_text(json.dumps(params, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp_path.replace(project.params_path)


def values_from_state(params: dict[str, Any]) -> dict[str, float]:
    return {name: float(spec["value"]) for name, spec in params.items()}


def build_project(project: Project) -> tuple[ModuleType, dict[str, Any], list[Part]]:
    project.ensure_dirs()
    module = load_model(project.model_path)
    params = load_param_state(project, module)
    values = values_from_state(params)
    build = getattr(module, "build", None)
    if not callable(build):
        raise RuntimeError(f"{project.model_path} must define build(**params)")
    with BuildContext(project.cache_dir) as ctx:
        build(**values)
        parts = list(ctx.parts)
    if not parts:
        raise RuntimeError("Model build did not create any @cached_part geometry")
    return module, params, parts


def _read_json(path: pathlib.Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return value if isinstance(value, dict) else {}


def _labelize(name: str) -> str:
    return name.replace("_", " ").strip().title()
