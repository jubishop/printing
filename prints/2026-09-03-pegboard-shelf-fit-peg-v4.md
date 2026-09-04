# 2026-09-03 — Climbing pegboard shelf fit peg v4

- Status: completed
- Started: 2026-09-03 21:42 PDT
- Completed: by 2026-09-04 07:07 PDT; exact finish time not observed
- Related issue: none

## Goal

Test a 31.8 mm outside diameter and 39.2 mm insertion length. Success means a
closer fit than v3 while the gauge still inserts and removes with ordinary hand
pressure.

## Source and provenance

- Creator: Jubi, with OpenAI Codex modeling assistance
- Model URL: none; original local design
- Exact profile/profile ID: local parametric OpenSCAD model, `fourth` variant
- License and date checked: all rights reserved; 2026-09-03
- Local files committed: shared source, variant STL/render, and this record;
  printer-specific 3MF remains private and ignored
- Modifications from upstream: not applicable

## Observed dimensions

- Hole diameter: approximately 31.2 mm for both holes
- Test peg outside diameter: 31.8 mm
- Test peg insertion length: 39.2 mm
- Change from v3: outside diameter and insertion length each increased 0.2 mm
- Nominal relationship to measured hole: 0.6 mm interference

## Hardware

- Printer: Bambu Lab X2D, verified in the project and send screen
- Nozzle size/type: main and auxiliary set to 0.4 mm hardened steel
- Build plate: Textured PEI Plate
- Plate preparation: user reported that the machine is ready

## Material routing

| Role | Filament/profile | Source slot/feed | Nozzle |
| --- | --- | --- | --- |
| Object | Bambu PLA Pure | AMS A3 | Main, 0.4 mm hardened steel |
| Support base | None intended | Not applicable | Not applicable |
| Support interface | None intended | Not applicable | Not applicable |

## Profile and slice

- App and version: Bambu Studio 02.08.02.61
- Layer height: 0.20 mm, including the initial layer
- Walls: 2; model has a 2.4 mm tube wall
- Infill pattern/percentage: grid, 15%
- Supports: disabled
- Adhesion/brim: auto brim
- Temperatures: controlled by the Bambu PLA Pure profile; no manual override
- Speed/flow changes: none intended
- Dimensional compensation: XY contour 0 mm, XY hole 0 mm, circle
  compensation off, elephant-foot compensation 0.15 mm
- Estimated time/material: 41 minutes 54 seconds; 12.32 g; 4.13 m

## Preflight

- [x] Exact local v4 STL verified as one connected, watertight mesh
- [x] X2D, active nozzle diameters, and build plate verified
- [x] Physical build plate and preparation reported ready by the user
- [x] Object material assignment verified
- [x] Upright orientation with flange on the plate verified
- [x] Slice preview inspected, including a contiguous first-layer section
- [x] Current filament/nozzle mapping verified
- [x] Auto Bed Leveling freshly rechecked immediately before send
- [x] Flow Dynamics Calibration freshly rechecked immediately before send
- [x] Nozzle Offset Calibration freshly rechecked immediately before send
- [x] No third-party model or profile included

The printer accepted the job and showed `Homing toolhead`, 0%, and layer 0/216
at 21:42 PDT. Its displayed estimated finish time was 22:23 PDT.
A follow-up live check showed `Build plate alignment detection` with no error.

## Outcome

- Actual result: completed; live Studio showed 100%, layer 216/216, Finished
- Dimensions/fit: the 39.2 mm gauge touched the back before its flange fully
  seated. The user confirmed that 39.0 mm was correct and requested a 32.0 mm
  diameter for the next test.
- Surface or structural defects: none reported
- Photos: none
- Print history or app evidence checked: live Bambu Studio device view confirmed
  the exact v4 job name and completed print state

## Diagnosis and next change

Lock insertion length at 39.0 mm. Test a 32.0 mm diameter next, a 0.2 mm
increase from v4. Do not force the next gauge if it binds.

## Durable lesson

The 39.2 mm depth is too long; 39.0 mm is the user-confirmed working insertion
length for this pegboard. The model source and README record this choice.
