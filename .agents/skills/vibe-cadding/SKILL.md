---
name: vibe-cadding
description: >-
  Build and iteratively verify CadQuery models with the bundled vibecad viewer,
  parameters, cached colored parts, screencaps, and repeatable visual QA views.
  Use only when the user explicitly invokes this skill for programmatic CAD
  work that benefits from an interactive 3D viewer.
disable-model-invocation: true
argument-hint: "[CAD request, project name, or screencap token]"
---

# Vibe Cadding

The bundled `vibecad/` library serves each project's model,
`projects/<name>/model.py`, in a local 3D viewer. Run the commands below from
this skill's directory, where their relative paths resolve; each `uv run`
command's `--help` lists its options.

## Starting the server

For a new project, `scripts/init_example_project.sh <name>` installs the
dependencies, including the Playwright Chromium that renders agent views, and
creates the model from an example; replace the example once the viewer works.
Start the viewer with:

```bash
uv run vibecad --model projects/<name>/model.py
```

As soon as it listens, give the user its clickable URL from the output, such
as `Local viewer: http://127.0.0.1:8000`. A first start can spend minutes
between its `Importing CadQuery/OCP` and `Imported CadQuery/OCP.` lines; don't
restart it then unless it exits or stops using CPU.

## Modeling

- `build()` receives the value of each module-level
  `vibecad.parameter(default, min, max, step, label)` as a keyword argument.
  Declare one for each value the user might want to adjust. Slider values and
  limits saved in `projects/<name>/.vibecad/model_params.json` override the
  model's defaults, so update or remove a saved entry when changing its
  default or limits.
- The viewer and its exports show only parts made by functions decorated with
  `@cached_part(name, color)` or imported with `stl_part`, so wrap each
  semantically named component in one. Pass every value that can change its
  geometry through its arguments, such as parameter values and an external
  file's hash: the cache key covers only those arguments and the model file's
  text, so anything else the function reads, such as a global that `build()`
  sets, can serve stale geometry.
- `Workplane("XZ")` faces `-Y`, so a positive `extrude()` grows into `-Y`;
  check the bounding box when the direction matters.

## Visual QA

CAD geometry is error-prone, so verify each material change visually. The
viewer's "Send screenshot" button saves an annotated capture and copies a token
such as `<screencap-12345 cutaway at z=8>` for the user to paste. Given one,
resolve it with this command, which prints its annotated image's path, camera,
cutaway, and parameters, and inspect the image before changing the model:

```bash
uv run vibecad-screencap '<screencap-12345 cutaway at z=8>' --model projects/<name>/model.py
```

After each material change, rerun it with `--render` to rerender the current
model from the saved camera, and inspect the result. Without a screencap,
render and inspect the standard 2x2 view:

```bash
uv run vibecad-view --out /tmp/vibecad-standard.png
```

Rendering goes through the running server at `http://127.0.0.1:8000` unless
given `--server`.
