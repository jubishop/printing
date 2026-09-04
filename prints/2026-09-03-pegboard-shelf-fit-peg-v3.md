# 2026-09-03 — Climbing pegboard shelf fit peg v3

- Status: completed
- Started: 2026-09-03 19:38 PDT
- Completed: by 2026-09-03 21:34 PDT
- Related issue: none

## Goal

Test a 31.6 mm peg while preserving the confirmed 39.0 mm insertion length.
Success means less side-to-side movement than the 31.2 mm gauge while the peg
still inserts and removes with ordinary hand pressure.

## Source and provenance

- Creator: Jubi, with OpenAI Codex modeling assistance
- Model URL: none; original local design
- Exact profile/profile ID: local parametric OpenSCAD model, `third` variant
- License and date checked: all rights reserved; 2026-09-03
- Local files committed: shared source, variant STL/render, and this record;
  printer-specific 3MF remains private and ignored
- Modifications from upstream: not applicable

## Observed dimensions

- Hole diameter: approximately 31.2 mm for both holes
- Confirmed fit-gauge insertion length: 39.0 mm
- Test peg outside diameter: 31.6 mm
- Change from v2: outside diameter increased 0.4 mm; depth unchanged
- Nominal relationship to measured hole: 0.4 mm interference

## Hardware

- Printer: Bambu Lab X2D; synchronized from the live printer
- Nozzle size/type: main and auxiliary 0.4 mm hardened-steel, standard-flow
  configuration; main nozzle selected for this print
- Build plate: Textured PEI Plate selected in the project and send screen
- Plate preparation: same machine and plate used for the completed v2 print;
  user requested the immediate next fit iteration after removing and testing v2

## Material routing

| Role | Filament/profile | Source slot/feed | Nozzle |
| --- | --- | --- | --- |
| Object | Bambu PLA Pure | AMS A3 | Main, 0.4 mm |
| Support base | None intended | Not applicable | Not applicable |
| Support interface | None intended | Not applicable | Not applicable |

## Profile and slice

- App and version: Bambu Studio 02.08.02.61
- Layer height: 0.20 mm; 0.20 mm initial layer
- Walls: 2 wall loops; the model has a 2.4 mm tube wall
- Infill pattern/percentage: 15% grid in the flange and any enclosed wall gap
- Supports: disabled
- Adhesion/brim: automatic brim
- Temperatures: Bambu PLA Pure profile for X2D and 0.4 mm nozzle
- Speed/flow changes: none
- Dimensional compensation: 0 mm XY contour and hole compensation; circle
  compensation disabled; 0.15 mm elephant-foot compensation
- Estimated time/material: 41 minutes 41 seconds; 12.22 g; 4.10 m

## Preflight

- [x] Exact local v3 STL verified as one connected, watertight mesh
- [x] X2D, both active 0.4 mm nozzle diameters, and Textured PEI selection
  verified
- [x] Physical setup carried forward from the completed v2 print; user removed
  and tested v2 before requesting this immediate next print
- [x] Object material assignment verified
- [x] Upright orientation with flange on the plate verified
- [x] Slice preview and first-layer geometry inspected
- [x] Current filament/nozzle mapping verified: PLA Pure A3 to main nozzle
- [x] Auto Bed Leveling freshly rechecked immediately before send: Auto
- [x] Flow Dynamics Calibration freshly rechecked immediately before send: Auto
- [x] Nozzle Offset Calibration freshly rechecked immediately before send: Auto
- [x] No third-party model or profile included

Immediately before send, the screen and Bambu Studio configuration both showed
all three calibration controls as `Auto`. Bambu Studio uploaded the job through
the cloud service. The live device view showed Printing Progress at 0%, layer
0/215, then advanced into build-plate alignment detection with no alert or
intervention request.

## Outcome

- Actual result: completed successfully; live Bambu Studio readback showed 100%
  and layer 215/215, Finished
- Dimensions/fit: closer than v2, but the 31.6 mm outside diameter still felt
  narrow; user requested 0.2 mm more diameter and 0.2 mm more insertion depth
- Surface or structural defects: none reported
- Photos: none
- Print history or app evidence checked: live Bambu Studio device view showed
  the named job Finished at 100%, layer 215/215

## Diagnosis and next change

Increase outside diameter to 31.8 mm and insertion length to 39.2 mm for v4.
Do not force the larger gauge if it starts to bind.

## Durable lesson

The 31.6 x 39.0 mm gauge was closer but still did not establish the final fit.
Continue with the user's requested 0.2 mm change in both dimensions.
