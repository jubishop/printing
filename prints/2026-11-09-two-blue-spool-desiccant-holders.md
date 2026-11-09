# 2026-11-09 — Two blue spool-center desiccant holders

- Status: in progress
- Started: 2026-11-09 15:42 PST
- Completed: not observed
- Model recipe: [spool-center desiccant holder](../models/spool-desiccant-holder/README.md)

## Goal

Print two more of Jubi's usual spool-center holders together, using the newly
loaded blue filament. Jubi explicitly requested printing and confirmed the
machine was ready.

## Source and provenance

- Creator: Mono98.
- Model: [Dessicant or weight Container for Bambu Lab Spool](https://makerworld.com/en/models/1090858-dessicant-or-weight-container-for-bambu-lab-spool#profileId-1084332).
- Original designer profile: 0.20mm Standard @BBL X1C, profile 1084332.
- License: Standard Digital File License; recorded 2026-11-08, redistribution
  terms checked 2026-11-09 in the model recipe.
- Local model files committed: none.
- Reused the saved two-holder X2D plate. Synchronized live filament profiles
  and assigned all four parts to blue Bambu PLA Matte. Geometry, orientation,
  and spacing were retained.
- Configured project saved locally as
  `.local/models/spool-desiccant-holder/two-blue-spool-holders-x2d.3mf`.

## Hardware

- Printer: Bambu Lab X2D.
- Nozzles: 0.4/0.4 mm confirmed in the send dialog; hardened steel is the
  established hardware baseline. This job uses only the main nozzle.
- Plate: Textured PEI Plate selected in the project and send dialog.
- Preparation: Jubi reported the machine ready. The camera image at job start
  showed the installed textured plate with no prior printed objects present;
  cleaning was not independently observed.

## Material routing

| Role | Filament/profile | Source slot/feed | Nozzle |
| --- | --- | --- | --- |
| Two bodies and two lids | Blue Bambu PLA Matte, X2D 0.4 mm profile | AMS A2 | Main |
| Support base/interface | None | None | None |

Direct Override in Studio's filament synchronization imported the current AMS
inventory. All four objects were assigned to project filament 2, blue
`#0078BF`; the send dialog mapped it to blue AMS A2.

## Profile and slice

- Application: Bambu Studio 2.9.1.70.
- Process: 0.20mm Standard @BBL X2D, retaining the saved plate's choices.
- Layers: 0.20 mm, including first layer; 325 layers total.
- Walls: 2.
- Infill: 15% grid.
- Supports: disabled.
- Adhesion: automatic brim setting; broad perforated flange footprints.
- Temperatures: profile specifies 220 °C nozzle and 55 °C textured plate.
- Speed/flow changes: none beyond the synchronized PLA Matte profile.
- Sequence: by layer, all four parts on one plate.
- Estimated time/material: 5h19m11s, 91.66 g.

## Preflight

- [x] Known model and saved two-holder layout verified
- [x] Connected X2D, nozzle diameters, and selected plate verified in Studio
- [x] Newly loaded blue PLA Matte synchronized from the printer
- [x] Four object assignments checked in the saved project
- [x] Full slice and layers 1 and 3 visually inspected
- [x] Four separate, broad first-layer footprints and no slice warning observed
- [x] Final blue A2/main-nozzle mapping verified
- [x] All available calibrations explicitly set to Auto immediately before Send
- [x] Third-party model and generated G-code kept out of Git

Auto Bed Leveling and Flow Dynamics Calibration were already Auto. Nozzle
Offset Calibration initially showed Off and was changed to Auto before sending.
Timelapse remained off.

## Outcome

Studio reported **Successfully sent**, and the device page showed
`two-blue-spool-holders-x2d` with the correct blue four-part thumbnail and
download at 100%. It then advanced to **Heatbed surface foreign object
detection**, with layer 0/325, bed target 55 °C, and an estimated finish of
**21:01 PST** on November 9. Completion and physical fit have not been observed.

## Diagnosis and next change

No tuning change is supported by startup evidence. This is a repeat attempt
with the requested color substitution.
