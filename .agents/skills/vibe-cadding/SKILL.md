---
name: vibe-cadding
description: >-
  Build and iteratively verify CadQuery models with the bundled vibecad viewer,
  parameters, cached colored parts, screencaps, and repeatable visual QA views.
  Use only when the user explicitly invokes $vibe-cadding for programmatic CAD
  work that benefits from an interactive 3D viewer.
user_invocable: true
disable-model-invocation: true
argument: Optional CAD request, project name, or vibecad screencap token
---

# Vibe Cadding

The skill contains the reusable `vibecad/` library. Keep each project model in
`projects/<name>/model.py`. Run the bundled commands from this skill's directory
so their relative paths resolve correctly.

## Initializing a project

For a fresh project, run:

```bash
./scripts/init_example_project.sh my-project
```

The script installs dependencies with `uv sync`, installs the Playwright Chromium runtime used for agent screenshots, and creates `projects/my-project/model.py` from the bundled example model. It also seeds the example model's `.vibecad/part-cache/` from `scripts/templates/example_gears_part_cache/` when available so the first `/api/model` request can reuse pre-exported STEP/STL parts. The generated model file is intentionally example code and says so at the top; replace it with the real project model after confirming the viewer works.

The first server start on a machine can still spend time importing CadQuery/OCP. That is separate from geometry caching, so do not assume a silent `uv run vibecad ...` process is hung before checking whether Python is still importing.

After initialization, start the webserver for that model:

```bash
uv run vibecad --model projects/my-project/model.py --host 127.0.0.1 --port 8000
```

For repeated agent commands, set shell defaults once:

```bash
export VIBECAD_MODEL=projects/my-project/model.py
export VIBECAD_SERVER=http://127.0.0.1:8000
```

The Python commands read those variables by default. Explicit flags such as `--model ...` and `--server ...` always override the environment, which keeps commands reproducible when needed.


## Starting the server

When the local web server starts or restarts, give the user its clickable URL as
soon as it is available. Use the actual host and port from the command output,
for example:

```text
Local viewer: http://127.0.0.1:8000
```

Cold start warning: the first server launch in a fresh environment can spend a few minutes importing CadQuery/OCP before Uvicorn prints anything or binds the port. This is expected and is separate from the starter geometry cache. Do not restart a silent `uv run vibecad ...` process during this window unless it has exited or you have confirmed it is not making progress. Check with:

```bash
ps -axo pid,ppid,stat,etime,pcpu,command | rg 'vibecad|uv run'
lsof -nP -iTCP:8000 -sTCP:LISTEN || true
```

If the Python child is alive and using CPU or has only been running for a few minutes, keep waiting. Once Uvicorn prints the listening URL or `curl http://127.0.0.1:8000/` responds, paste the local viewer link.

## Parameters

Declare model parameters the user might want to modify (especially if they ask for them) with `vibecad.parameter(default, min, max, step, label)`. The server merges those defaults with `projects/<name>/.vibecad/model_params.json`, so slider values and edited slider limits persist across restarts.

## Geometry conventions

CadQuery's `Workplane("XZ").extrude(distance)` sends a positive extrusion in `-Y`, which is easy to get backwards. When modeling from the XZ plane, check the resulting bounding box before assuming the part extruded in the intended direction:

```python
solid = cq.Workplane("XZ").rect(width, height).extrude(thickness)
bb = solid.val().BoundingBox()
print(bb.ymin, bb.ymax)
```

For a positive XZ extrusion, expect `bb.ymin` to be negative and `bb.ymax` to be near zero. If the part should extend into `+Y`, use a negative extrusion distance or translate it after checking the bounding box.

## Cached parts

Wrap every semantically named component with `@cached_part(name, color)`.

```python
@cached_part("left red gear", (0.84, 0.12, 0.13))
def left_gear(teeth, module, thickness, bore_radius, x, z):
    ...
```

Pass every value that can change the geometry through the function arguments. The persistent cache key is derived from the part name, function name, model source content, and bound arguments. That means a server restart or model reload keeps the cache hot when those arguments and the model file are unchanged, and template caches remain portable when the same model content is copied into a new project.

Important: Do not use GLOBAL_VARIABLES inside methods: always pass as arguments. (Using GLOBALS breaks cache invalidation)

The decorator records the part name and color for the web preview, legend, screencap metadata, and multi-part STL serving.

## Visual QA

CAD geometry is error-prone and requires visual verification. When the user
provides a screencap token, inspect its annotated image before changing the
model. After each material change, rerender from the saved camera and inspect
the result. Without a screencap, render and inspect the standard 2x2 view.

Reuse the running server for screenshots so it benefits from the same hot
CadQuery cache:

```bash
uv run vibecad-view --server http://127.0.0.1:8000 --out /tmp/vibecad-standard.png
uv run vibecad-view --server http://127.0.0.1:8000 --capture-id screencap-12345 --out /tmp/vibecad-same-camera.png
```

If `VIBECAD_SERVER` is set, `--server` can be omitted. If `VIBECAD_MODEL` is set, `vibecad-screencap` can also omit `--model`.

The web UI's "Send screenshot" action saves `annotated.png` and `metadata.json` under `.vibecad/captures/<id>/`, then copies a token like `<screencap-12345 cutaway at z=8>` for the user to paste into chat.

Resolve a pasted screencap token directly with:

```bash
uv run vibecad-screencap '<screencap-12345 cutaway at z=8>' --model projects/my-project/model.py
```

That prints JSON containing the annotated input image path, metadata path, saved camera, cutaway, and parameter values. To also rerender the current model from the same saved camera using the already running server, use:

```bash
uv run vibecad-screencap '<screencap-12345 cutaway at z=8>' --model projects/my-project/model.py --server http://127.0.0.1:8000 --render
```

With the env vars set, this short form is preferred:

```bash
uv run vibecad-screencap '<screencap-12345 cutaway at z=8>' --render
```

Prefer this helper over manually searching `.vibecad/captures/`.
