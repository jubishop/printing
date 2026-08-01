---
name: case-2026-07-27-build-plate-holder
description: PETG build-plate-holder case with warp, likely layer shift, and support-interface routing
type: reference
---

# 2026-07-27: P2S/X2D build plate holder

This is dated case evidence, not a universal PETG profile.

## Source

- Model: [P2S/X2D Build Plate Holder](https://makerworld.com/en/models/2013980)
- Creator: CS Design
- Selected profile at the time: `V3: Fitment and Thickness Adjustment`
- License observed on 2026-07-31: MakerWorld Standard Digital File License
- Repository decision: record provenance only; do not commit the downloaded
  model/profile under that license.

## Verified configuration

- Printer: Bambu Lab X2D with 0.4 mm hardened-steel nozzles
- Plate: Textured PEI
- Object: Bambu PETG Basic from AMS A4 through the left/main nozzle
- Support base: PETG
- Support interface: Bambu Support for PLA/PETG from an external spool through
  the right/auxiliary nozzle
- `Avoid interface filament for support base`: enabled
- Prime tower: enabled
- Other relevant settings: 0.2 mm layers, 2 walls, 10% grid infill, 5 mm brim
  ears, PETG at 245/250 C, and a 70 C bed

## Outcome and diagnosis

The long functional part was usable, but its bottom bowed. Its long face had a
pronounced raised ledge at one constant Z height, ragged material beneath the
ledge, and several smaller horizontal streaks. The part was removed while it
and the plate were still very warm.

The best current diagnosis is a true lateral layer shift after the long part
curled or lifted, or after the nozzle struck the part or crossing grid infill.
Hot removal likely amplified the bowing and possible bottom damage, but it
cannot explain a defect that was already visible during printing.

A raised ledge on one face paired with a recessed step on the opposite face is
strong evidence of a layer shift. An equal outward bulge on both faces is more
consistent with a flow or geometry-transition artifact.

## Reusable guidance

- Let PETG and the PEI plate cool fully before removal.
- For long warp-prone parts, consider a continuous brim, gyroid or another
  non-crossing infill, 3 walls, and conservative PETG speed/flow.
- Inspect the sliced preview for abrupt speed/flow changes and watch early
  layers for edge lift.
- Keep calibration and moisture in the diagnostic tree, but do not default to
  them when the geometry instead indicates lift, a nozzle strike, or a
  one-height layer shift.
