from __future__ import annotations

import argparse
import asyncio
import json
import os
import pathlib
import re
from typing import Any

import httpx

from .capture_view import _render_capture
from .project import Project


TOKEN_RE = re.compile(r"(screencap-\d+)")


def main() -> None:
    parser = argparse.ArgumentParser(description="Resolve a vibe-cadding screencap token and optionally rerender that camera.")
    parser.add_argument("token", help="Pasted token such as '<screencap-123 cutaway at z=8>' or a bare screencap id.")
    parser.add_argument("--model", default=os.environ.get("VIBECAD_MODEL", "projects/my-project/model.py"), help="Model path used to locate the project's .vibecad/captures directory. Defaults to VIBECAD_MODEL.")
    parser.add_argument("--server", default=os.environ.get("VIBECAD_SERVER", "http://127.0.0.1:8000"), help="Already running vibe-cadding server to reuse for rerenders. Defaults to VIBECAD_SERVER.")
    parser.add_argument("--render", action="store_true", help="Render the current model from the saved camera.")
    parser.add_argument("--out", help="Output path for --render. Defaults next to the capture metadata.")
    parser.add_argument("--width", type=int, default=1400)
    parser.add_argument("--height", type=int, default=1000)
    args = parser.parse_args()

    capture_id = _capture_id(args.token)
    project = Project.from_model_path(pathlib.Path(args.model))
    capture_dir = project.captures_dir / capture_id
    metadata_path = capture_dir / "metadata.json"
    if not metadata_path.exists():
        raise SystemExit(f"Capture metadata not found: {metadata_path}")

    metadata = _read_json(metadata_path)
    image_path = pathlib.Path(str(metadata.get("image") or capture_dir / "annotated.png")).resolve()
    output: dict[str, Any] = {
        "id": capture_id,
        "annotated_image": str(image_path),
        "metadata": str(metadata_path.resolve()),
        "model": str(project.model_path),
        "server": args.server.rstrip("/"),
        "camera": metadata.get("camera"),
        "cutaway": metadata.get("cutaway"),
        "params": metadata.get("params"),
    }

    if args.render:
        out = pathlib.Path(args.out).resolve() if args.out else (capture_dir / "rerender.png").resolve()
        out.parent.mkdir(parents=True, exist_ok=True)
        asyncio.run(_render_capture(args.server.rstrip("/"), capture_id, out, args.width, args.height))
        output["rerender"] = str(out)

    print(json.dumps(output, indent=2, sort_keys=True))


def _capture_id(token: str) -> str:
    match = TOKEN_RE.search(token)
    if not match:
        raise SystemExit(f"Could not find screencap id in token: {token}")
    return match.group(1)


def _read_json(path: pathlib.Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid capture metadata JSON: {path}") from exc
    if not isinstance(value, dict):
        raise SystemExit(f"Capture metadata is not an object: {path}")
    return value


if __name__ == "__main__":
    main()
