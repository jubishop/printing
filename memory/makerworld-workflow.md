---
name: makerworld-workflow
description: Handy-first MakerWorld routing and exact-profile preflight
type: feedback
---

# MakerWorld workflow

Start every MakerWorld request by inspecting the exact selected profile,
intended plate, material, and requested result. Prefer the simplest reliable
workflow.

**Why:** Trusted X2D profiles can often be printed unchanged from Bambu Handy,
while support routing, material provenance, and plate selection cannot be
reliably inferred from a model thumbnail or generic page metadata.

**How to apply:** Use this preflight whenever Jubi supplies a MakerWorld URL or
asks for help preparing a print.

## Choose the app

Use Bambu Handy when all of the following are true:

- MakerWorld/Handy presents the exact profile as compatible after selecting the
  X2D and intended plate.
- Orientation, supports, strength, adhesion, nozzle, and material choices are
  already suitable.
- Only an ordinary supported filament mapping or substitution is needed.
- No model or profile modification is requested.

Use Bambu Studio when the print needs any of the following:

- Supports or support-interface material created or changed.
- Auxiliary-nozzle or custom material routing.
- Orientation, walls, infill, brim, calibration, tolerance, speed, flow, or
  material tuning.
- Sliced-preview inspection or any model/profile modification.

Handy can preserve and map a dedicated support material already encoded in a
profile, but it cannot invent that setup. If its mapping screen contains only
one filament, a separate support spool will not be used.

The printer used to author a profile is not, by itself, a reason to require
Studio. MakerWorld's cloud slicer uses the currently selected printer, filament,
and plate while retaining important model and process choices such as support
and strength settings. If a profile remains available after selecting X2D,
Handy may be the correct path even when the downloaded 3MF names A1 or X1 as its
source printer. See [Bambu Lab's one-step printing
guide](https://blog.bambulab.com/makerworld-one-step-printing/) and
[[case-2026-07-31-skadis-tool-holder]].

Compatibility is not equivalence. Two profiles that have the same title,
geometry, orientation, and X2D badge can still retain materially different
overhang speeds, acceleration, compensation, adhesion, or strength choices.
Compare those choices when there is a meaningful quality-versus-speed decision.

## Exact-profile preflight

1. Confirm the model URL, exact profile/profile ID, live X2D eligibility,
   intended plate, and intended printed parts.
2. Check whether support is enabled and whether support base and support
   interface use different materials.
3. If multiple profiles appear equivalent, compare their ratings, live X2D
   estimates, and the process settings that matter for the intended material.
4. If page metadata is insufficient, inspect the authenticated 3MF. Relevant
   settings commonly live in `Metadata/project_settings.config` and
   `Metadata/model_settings.config`.
5. Treat a downloaded 3MF as the uploader's source profile. Even after an X2D
   filter is selected, the download may retain its original A1/X1 machine
   metadata; that does not reproduce the final cloud-sliced X2D job.
6. Verify object materials from active project assignments rather than embedded
   profile provenance.
7. In Studio, slice and inspect material use, support, plate placement, abrupt
   speed/flow changes, and obvious collision or adhesion risks.
8. In Handy, confirm the profile remains available for the selected X2D and
   verify the final filament, nozzle, and plate mapping.
9. Do not claim a configuration, slice, cloud conversion, or print mapping was
   verified unless it
   was directly observed.

MakerWorld may reject direct or unauthenticated model downloads. Use an
authenticated browser session when exact 3MF inspection is required, and never
commit the downloaded file without first checking its redistribution license.
