# 2026-11-11 — Two green spool-center desiccant holders

- Status: in progress
- Started: 2026-11-11 10:01 PST
- Completed: not observed
- Model recipe: [spool-center desiccant holder](../models/spool-desiccant-holder/README.md)

## Goal

Print two of Jubi's usual spool-center desiccant containers, each with a
screw lid, in green on one plate.

## Source and provenance

- Creator: Mono98.
- Model: [Dessicant or weight Container for Bambu Lab Spool](https://makerworld.com/en/models/1090858-dessicant-or-weight-container-for-bambu-lab-spool#profileId-1084332).
- Original profile: 0.20mm Standard @BBL X1C, profile 1084332.
- License: Standard Digital File License, recorded 2026-11-08. The model
  recipe documents the 2026-11-09 review of the redistribution terms.
- Reused the two-holder X2D project from the
  [blue run](2026-11-09-two-blue-spool-desiccant-holders.md) and changed the
  filament assignments to green. Geometry, orientation, and layout were retained.
- Local project: `.local/models/spool-desiccant-holder/two-green-spool-holders-x2d.3mf`.
  No model archive or generated G-code was committed.

## Hardware

- Printer: Bambu Lab X2D.
- Nozzles: 0.4/0.4 mm shown in the send dialog, with hardened steel as the
  established hardware baseline. Only the main nozzle was assigned filament.
- Build plate: Textured PEI Plate in Studio. The live camera showed the
  installed textured plate clear of prior prints. Jubi reported it ready.

## Material routing

| Role | Filament/profile | Source slot/feed | Nozzle |
| --- | --- | --- | --- |
| Two bodies and two lids | Green Bambu PLA Matte, X2D 0.4 mm profile | AMS A4 | Main |
| Support base/interface | None | None | None |

Studio synchronized the live AMS list. All four objects were assigned to
project filament 4 (`#61C680`), mapped to green AMS A4 in the send dialog.

## Profile and slice

- Application: Bambu Studio 2.9.1.70.
- Process: 0.20mm Standard @BBL X2D, 0.20 mm first layer, 325 layers total.
- Walls and infill: two walls, 15% grid infill.
- Supports: disabled. Brim setting: automatic. Print sequence: by layer.
- Filament profile temperatures: 220 °C nozzle and 55 °C textured plate.
- Estimate: 5h19m14s and 91.66 g.

## Preflight

- [x] Known model and single plate with two bodies and two lids verified
- [x] Connected X2D, 0.4 mm nozzles, and physical textured plate verified
- [x] Green PLA Matte synchronized and all four object assignments verified
- [x] Full slice and layers 1 and 4 inspected, with four separated flange footprints
- [x] Final green A4 mapping to the main nozzle verified
- [x] Auto Bed Leveling, Flow Dynamics Calibration, and Nozzle Offset Calibration verified on Auto immediately before sending
- [x] Jubi approved sending after preflight

Nozzle Offset Calibration opened on Off and was set to Auto. The other two
calibrations were already on Auto. Timelapse was off.

## Outcome

The device page showed `two-green-spool-holders-x2d` downloaded to 100% and
then **Homing toolhead** at layer 0/325. Its estimated finish was 15:20 PST.
Completion, dimensions, fit, and finish quality were not observed.
