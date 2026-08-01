# Models

This directory is for original or third-party model artifacts whose licenses
permit redistribution. Availability for download does not by itself grant
permission to republish a file here.

If redistribution is not permitted or the license is unclear, store only the
upstream URL, profile ID, configuration, and outcome in the relevant print log
or memory case.

## Required provenance

Every committed model directory must include a README recording:

- Model name and creator.
- Canonical source URL and exact profile/profile ID.
- License name, license URL or text, and the date checked.
- Whether the artifact is original, an unchanged upstream file, or modified.
- A clear summary of every local modification.
- Relevant application and version used to produce exports.
- The intended printer, nozzle, material, and plate when those constraints are
  intrinsic to the artifact.

A suggested layout is:

```text
models/<model-slug>/
  README.md
  source/       # only when redistribution is permitted
  modified/     # editable local variants
  exports/      # redistributable print-ready outputs
```

## Safety and storage

- Inspect 3MF and slicer project files for embedded account, device, network,
  local-path, and other private metadata before committing them.
- Do not commit generated G-code.
- Git LFS is intentionally not enabled yet. Before adding large binary `.3mf`,
  `.stl`, `.step`, `.f3d`, or similar files, configure and verify LFS tracking
  in the same commit.
- There is no blanket repository license. Each artifact retains the license
  documented beside it.
