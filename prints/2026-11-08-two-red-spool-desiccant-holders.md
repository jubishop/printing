# 2026-11-08 — Two red spool-center desiccant holders

- Status: in progress
- Started: 2026-11-08 19:43 PST
- Completed: not observed
- Related model recipe: [spool-center desiccant holder](../models/spool-desiccant-holder/README.md)

## Goal

Print two complete red holders on one plate for the centers of Bambu spools.
Jubi identified the model in MakerWorld and explicitly authorized sending the
two-copy print after confirming the machine was ready.

## Source and provenance

- Creator: Mono98.
- Model URL: <https://makerworld.com/en/models/1090858-dessicant-or-weight-container-for-bambu-lab-spool#profileId-1084332>.
- Exact profile: **0.20mm Standard @BBL X1C**, profile **1084332**.
- License: Standard Digital File License, checked 2026-11-08.
- Local model files committed: none; configured 3MF retained in ignored
  `.local/models/spool-desiccant-holder/`.
- Modifications: adapted to X2D, duplicated body and lid, spaced all four parts
  on one plate, and assigned red Bambu PLA Matte to every part. No mesh edits.

## Hardware

- Printer: Bambu Lab X2D.
- Nozzles: 0.4/0.4 mm verified in the send dialog; hardened steel is the
  established hardware baseline. Only the main nozzle is used by this slice.
- Build plate: Textured PEI Plate selected in the project and send dialog.
- Plate preparation: Jubi reported the machine ready. The device camera image
  at job start showed an installed textured plate without prior printed objects;
  cleaning was not independently observed.

## Material routing

| Role | Filament/profile | Source slot/feed | Nozzle |
| --- | --- | --- | --- |
| All four object parts | Red Bambu PLA Matte, X2D 0.4 mm profile | AMS A3 | Main |
| Support base/interface | None | None | None |

The live AMS inventory was synchronized. Project filament 3 was red; the
final send dialog mapped it to the red A3 spool, with no auxiliary filament.

## Profile and slice

- App: Bambu Studio 2.9.1.70; BBL configuration 2.9.0.75.
- Process: 0.20mm Standard @BBL X2D, with retained source choices.
- Layer height: 0.20 mm, including the first layer; 325 layers.
- Walls: 2.
- Infill: 15% grid.
- Supports: disabled.
- Adhesion: automatic brim setting; broad perforated flanges on the plate.
- Temperatures: saved profile specifies 220 °C nozzle and 55 °C bed.
- Speed/flow: adapted preset values, without additional manual overrides.
- Print sequence: by layer, both holders on one plate.
- Estimate: 5h19m13s, 91.66 g, 28.87 m.

## Preflight

- [x] User-confirmed model, exact designer profile, and single intended plate
- [x] X2D selected and original profile adapted in Studio
- [x] Printer and nozzle diameters checked in the final send dialog
- [x] Textured PEI selected; user confirmed physical machine ready
- [x] Four separate parts assigned only to red PLA Matte
- [x] Full preview and early layers inspected, including layers 1 and 3
- [x] Four separated, coplanar flange footprints visible; no slice warning shown
- [x] Final red AMS A3/main-nozzle mapping verified
- [x] Auto Bed Leveling, Flow Dynamics Calibration, and Nozzle Offset Calibration
  each explicitly set to Auto immediately before sending
- [x] Third-party geometry and generated G-code omitted from Git

Timelapse was off. Nozzle Offset Calibration initially showed Off in the send
dialog and was changed to Auto before sending; the other two were already Auto.

## Outcome

Studio reported **Successfully sent**, then displayed the correct four-part
thumbnail and `two-red-spool-holders-x2d` as the active job. The device page
showed layer 0/325 and a bed target of 55 °C as startup began, then advanced to
**Build plate alignment detection** with an estimated finish of **01:03 PST
on November 9**. This records a started attempt, not a completed or fit-tested
result.

Dimensions, fit, surface quality, and final completion have not been observed.
No diagnosis or tuning change is justified by the startup evidence.
