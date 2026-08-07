---
name: case-2026-08-07-skadis-firm-grip-clip
description: SKADIS Firm-Grip Clip case validating slower PETG Basic top and solid paths after a repeated same-height failure
type: reference
---

# 2026-08-07: SKÅDIS Firm-Grip Clip PETG Basic validation

This is dated evidence for one model and material substitution, not a universal
PETG speed profile.

## Source and configuration

- Model: [SKÅDIS Firm-Grip Clip](https://makerworld.com/en/models/1371666-skadis-firm-grip-clip#profileId-1418278)
- Creator/profile uploader: Henryk
- Selected profile: `Single-Color Version`, profile `1418278`
- Printer and plate: Bambu Lab X2D, 0.4 mm hardened-steel nozzles, Textured PEI
- Object and support body: Bambu PETG Basic from AMS A4 through main nozzle
- Support interface: Bambu Support for PLA/PETG from external feed through
  auxiliary/right nozzle
- Repository decision: retain settings and provenance only; the Standard
  Digital File License does not permit committing the downloaded or modified
  model 3MF.

## Failed fast baseline

The upstream H2D project was authored around Bambu PETG HF. The first X2D
four-pack substituted PETG Basic but retained 200 mm/s top surfaces and 250
mm/s internal solid infill. AI detection stopped it at 88% after strands formed
at the same height across nearly every copy. All objects remained attached and
the lower layers looked good.

G-code inspection mapped the stop to Z=10.8–11.0 mm, where the repeated parts
simultaneously entered top-surface and internal-solid work. Dedicated support
interface had ended at Z=4.2 mm, ruling out an active interface-material
transition at the failure layer.

## Successful controlled retry

The retry used plate 1, one complete clip, while preserving the same material
and support routing. Top surfaces were reduced to 80 mm/s and internal solid
infill to 120 mm/s. Generated G-code confirmed those exact speeds through the
previous failure band. The 65-layer print estimated 43m11s and 13.07 g; the
user reported that the completed result came out great.

Changing both copy count and speed means the retry does not isolate speed as
the only causal variable. However, the original same-height failure on every
copy, the clean lower layers, the inactive support interface at that height,
and successful traversal at the reduced speeds strongly support excessive
PETG Basic top/solid speed as the main cause.

## Reusable guidance

- When substituting PETG Basic into a profile authored around PETG HF, inspect
  actual top-surface and internal-solid G-code speeds and volumetric limits.
- Correct first layers and support routing do not validate later high-flow
  transitions.
- For this model and setup, 80 mm/s top surface and 120 mm/s internal solid are
  physically validated on the single-clip plate.
- Preserve AI detection and validate one copy before scaling a corrected
  process back to a repeated plate.
- Treat the corrected four-pack as a separate validation until it completes.
