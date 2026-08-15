from __future__ import annotations

import argparse
import base64
from dataclasses import replace
import json
import os
import pathlib
import shutil
import subprocess
import time
from typing import Any

import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse, Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from .core import export_compound
from .project import Project, build_project, load_model, load_param_state, save_param_state


class ParamUpdate(BaseModel):
    params: dict[str, dict[str, Any]]


class CapturePayload(BaseModel):
    image: str
    metadata: dict[str, Any]
    note: str = ""


class ClipboardPayload(BaseModel):
    text: str


def create_app(project: Project) -> FastAPI:
    project.ensure_dirs()
    static_dir = pathlib.Path(__file__).parent / "static"
    app = FastAPI(title="vibe-cadding")
    app.state.project = project
    app.state.model_cache = None
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

    @app.get("/", response_class=HTMLResponse)
    def index() -> str:
        return (static_dir / "index.html").read_text(encoding="utf-8")

    @app.get("/standard", response_class=HTMLResponse)
    def standard_view() -> str:
        return (static_dir / "standard.html").read_text(encoding="utf-8")

    @app.get("/api/model")
    def api_model(request: Request) -> dict[str, Any]:
        module = load_model(project.model_path)
        params = load_param_state(project, module)
        stamp = _geometry_stamp(project, module, params)
        cached = app.state.model_cache
        if cached and cached["stamp"] == stamp:
            return _model_payload(request, project, module, params, cached["parts"])
        try:
            _, params, parts = build_project(project)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc
        parts_payload = _parts_payload(request, parts)
        app.state.model_cache = {"stamp": _geometry_stamp(project, module, params), "parts": parts_payload}
        return _model_payload(request, project, module, params, parts_payload)

    @app.post("/api/preview")
    def api_preview(update: ParamUpdate) -> dict[str, Any]:
        module = load_model(project.model_path)
        current = load_param_state(project, module)
        for name, incoming in update.params.items():
            if name in current and "value" in incoming:
                current[name]["value"] = incoming["value"]
        return {
            "previewTransforms": _preview_transforms(module, current),
            "previewOnlyParams": sorted(getattr(module, "PREVIEW_ONLY_PARAMS", set())),
        }

    @app.post("/api/params")
    def api_params(update: ParamUpdate) -> dict[str, Any]:
        module = load_model(project.model_path)
        current = load_param_state(project, module)
        for name, incoming in update.params.items():
            if name not in current:
                continue
            merged = dict(current[name])
            for key in ("value", "min", "max", "step", "label"):
                if key in incoming:
                    merged[key] = incoming[key]
            minimum = float(merged["min"])
            maximum = float(merged["max"])
            if maximum <= minimum:
                maximum = minimum + float(merged["step"])
            merged["min"] = minimum
            merged["max"] = maximum
            merged["value"] = max(minimum, min(maximum, float(merged["value"])))
            current[name] = merged
        save_param_state(project, current)
        return {"ok": True, "params": current}

    @app.get("/api/parts/{cache_key}.stl", name="part_stl")
    def part_stl(cache_key: str) -> FileResponse:
        path = project.cache_dir / cache_key / f"{cache_key}.stl"
        if not path.exists():
            raise HTTPException(status_code=404, detail="Part STL not found")
        return FileResponse(path, media_type="model/stl")

    @app.get("/api/export/{fmt}", name="export_model")
    def export_model(fmt: str) -> FileResponse:
        fmt = fmt.lower()
        if fmt not in {"stl", "step"}:
            raise HTTPException(status_code=400, detail="Use stl or step")
        try:
            _, params, parts = build_project(project)
            parts = _apply_preview_transforms(parts, params)
            path = project.exports_dir / f"{project.model_path.stem}.{fmt}"
            export_type = "STL" if fmt == "stl" else "STEP"
            export_compound(parts, path, export_type)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc
        return FileResponse(path, filename=path.name)

    @app.post("/api/captures")
    def create_capture(payload: CapturePayload) -> dict[str, Any]:
        capture_id = f"screencap-{int(time.time() * 1000)}"
        capture_dir = project.captures_dir / capture_id
        capture_dir.mkdir(parents=True, exist_ok=True)
        image_data = payload.image.split(",", 1)[-1]
        image_path = capture_dir / "annotated.png"
        metadata_path = capture_dir / "metadata.json"
        try:
            image_path.write_bytes(base64.b64decode(image_data))
        except Exception as exc:
            raise HTTPException(status_code=400, detail="Invalid image data") from exc

        metadata = dict(payload.metadata)
        if payload.note:
            metadata["note"] = payload.note
        metadata["image"] = str(image_path)
        metadata["model"] = str(project.model_path)
        metadata["createdAt"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
        metadata_path.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8")

        cutaway = metadata.get("cutaway") or {}
        cutaway_text = ""
        if cutaway.get("enabled"):
            cutaway_text = f" cutaway at z={cutaway.get('z')}"
        token = f"<{capture_id}{cutaway_text}>"
        return {
            "id": capture_id,
            "token": token,
            "image": str(image_path),
            "metadata": str(metadata_path),
        }

    @app.post("/api/clipboard")
    def copy_to_clipboard(payload: ClipboardPayload) -> dict[str, bool]:
        if not payload.text:
            raise HTTPException(status_code=400, detail="No clipboard text provided")
        command = _clipboard_command()
        if not command:
            raise HTTPException(status_code=501, detail="No system clipboard command available")
        try:
            subprocess.run(command, input=payload.text, text=True, check=True)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=f"Clipboard write failed: {exc}") from exc
        return {"ok": True}

    @app.get("/api/captures/{capture_id}")
    def get_capture(capture_id: str) -> dict[str, Any]:
        metadata_path = project.captures_dir / capture_id / "metadata.json"
        if not metadata_path.exists():
            raise HTTPException(status_code=404, detail="Capture not found")
        return json.loads(metadata_path.read_text(encoding="utf-8"))

    @app.get("/api/standard-view")
    async def render_standard_view(request: Request) -> Response:
        url = str(request.url_for("standard_view"))
        out = project.captures_dir / f"standard-{int(time.time() * 1000)}.png"
        try:
            await _render_page(url, out, width=1400, height=1000)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=f"Could not render standard view: {exc}") from exc
        return FileResponse(out, media_type="image/png", filename=out.name)

    return app


def _parts_payload(request: Request, parts: list[Any]) -> list[dict[str, Any]]:
    return [
        {
            "name": part.name,
            "color": part.color,
            "cacheKey": part.cache_key,
            "stlUrl": str(request.url_for("part_stl", cache_key=part.cache_key)) + f"?t={part.stl_path.stat().st_mtime_ns}",
        }
        for part in parts
    ]


def _model_payload(request: Request, project: Project, module: Any, params: dict[str, Any], parts: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "model": str(project.model_path),
        "modelMtime": project.model_path.stat().st_mtime,
        "params": params,
        "parts": parts,
        "previewTransforms": _preview_transforms(module, params),
        "previewOnlyParams": sorted(getattr(module, "PREVIEW_ONLY_PARAMS", set())),
        "exports": {
            "stl": str(request.url_for("export_model", fmt="stl")),
            "step": str(request.url_for("export_model", fmt="step")),
        },
    }


def _geometry_stamp(project: Project, module: Any, params: dict[str, Any]) -> tuple[int, tuple[tuple[str, float], ...]]:
    preview_only = set(getattr(module, "PREVIEW_ONLY_PARAMS", set()))
    values = tuple(
        sorted(
            (name, float(spec["value"]))
            for name, spec in params.items()
            if name not in preview_only
        )
    )
    return project.model_path.stat().st_mtime_ns, values


def _preview_transforms(module: Any, params: dict[str, Any]) -> dict[str, list[float]]:
    preview = getattr(module, "preview", None)
    if not callable(preview):
        return {}
    values = {name: float(spec["value"]) for name, spec in params.items()}
    transforms = preview(**values)
    if not isinstance(transforms, dict):
        return {}
    return {str(name): list(matrix) for name, matrix in transforms.items()}


def _apply_preview_transforms(parts: list[Any], params: dict[str, Any]) -> list[Any]:
    theta = float(params.get("theta", {}).get("value", 0.0))
    if theta == 0:
        return parts
    transformed = []
    for part in parts:
        if "gear" not in part.name:
            transformed.append(part)
            continue
        angle = theta if "left" in part.name else -theta
        bbox = part.geometry.val().BoundingBox()
        pivot_x = (bbox.xmin + bbox.xmax) / 2
        pivot_y = (bbox.ymin + bbox.ymax) / 2
        geometry = part.geometry.rotate((pivot_x, pivot_y, 0), (pivot_x, pivot_y, 1), angle)
        transformed.append(replace(part, geometry=geometry))
    return transformed


def _clipboard_command() -> list[str] | None:
    for command in (["pbcopy"], ["wl-copy"], ["xclip", "-selection", "clipboard"]):
        if shutil.which(command[0]):
            return command
    return None


async def _render_page(url: str, out: pathlib.Path, width: int, height: int) -> None:
    from playwright.async_api import async_playwright

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=1)
        await page.goto(url, wait_until="networkidle")
        await page.wait_for_function("window.__vibecadReady === true", timeout=60000)
        await page.screenshot(path=str(out), full_page=True)
        await browser.close()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default=os.environ.get("VIBECAD_MODEL", "projects/my-project/model.py"))
    parser.add_argument("--host", default=os.environ.get("VIBECAD_HOST", "127.0.0.1"))
    parser.add_argument("--port", type=int, default=int(os.environ.get("VIBECAD_PORT", "8000")))
    args = parser.parse_args()
    project = Project.from_model_path(pathlib.Path(args.model))
    uvicorn.run(create_app(project), host=args.host, port=args.port)


if __name__ == "__main__":
    main()
