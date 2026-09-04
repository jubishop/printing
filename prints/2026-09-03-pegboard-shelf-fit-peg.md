# 2026-09-03 — Climbing pegboard shelf fit peg

- Status: completed
- Started: 2026-09-03 13:12 PDT
- Completed: by 2026-09-03 15:42 PDT
- Related issue: none

## Goal

Calibrate a removable printed peg against one hole of the wooden climbing
pegboard before designing the two-peg shelf. Success means that the peg reaches
the flange with ordinary hand pressure, comes out without tools, does not mark
the plywood, and has little side-to-side movement.

The planned shelf will use PLA and has a user-specified maximum combined
object load of 2 lb (0.91 kg). That future limit does not make the fit gauge or
shelf a climbing-rated component.

## Source and provenance

- Creator: Jubi, with OpenAI Codex modeling assistance
- Model URL: none; original local design
- Exact profile/profile ID: local parametric OpenSCAD model
- License and date checked: all rights reserved; 2026-09-03
- Local files committed: source, STL, render, documentation, and this print
  record in commit `59e3d7d`
- Modifications from upstream: not applicable

## Observed dimensions

- Hole diameter: approximately 31.2 mm for both holes
- Hole depth: approximately 38.3 mm for both holes
- Test peg outside diameter: 30.8 mm
- Test peg insertion length: 36.8 mm
- Initial diametral clearance: 0.4 mm

## Hardware

- Printer: Bambu Lab X2D; synchronized from the live printer
- Nozzle size/type: main and auxiliary 0.4 mm, standard-flow configuration;
  main nozzle used for this print
- Build plate: Textured PEI Plate, matched in the project and live camera view
- Plate preparation: plate appears clear in the live camera; cleaning remains a
  hands-on check before sending

## Material routing

| Role | Filament/profile | Source slot/feed | Nozzle |
| --- | --- | --- | --- |
| Object | Bambu PLA Pure | AMS A3 | Main, 0.4 mm |
| Support base | None intended | Not applicable | Not applicable |
| Support interface | None intended | Not applicable | Not applicable |

## Profile and slice

- App and version: Bambu Studio 02.08.02.61
- Layer height: 0.20 mm; 0.20 mm initial layer
- Walls: 2 wall loops; the model itself has a 2.4 mm tube wall
- Infill pattern/percentage: 15% grid in the flange and any enclosed wall gap
- Supports: disabled
- Adhesion/brim: automatic brim; preview did not show a separate support
  structure
- Temperatures: Bambu PLA Pure profile for X2D and 0.4 mm nozzle
- Speed/flow changes: none
- Dimensional compensation: 0 mm XY contour and hole compensation; circle
  compensation disabled; 0.15 mm elephant-foot compensation
- Estimated time/material: 39 minutes 58 seconds; 11.51 g; 3.86 m

## Preflight

- [x] Exact local fit-peg STL verified as one connected, watertight mesh
- [x] Printer, active nozzle diameters, and physical build plate verified
- [x] Object material assignment verified
- [x] Upright orientation with flange on the plate verified
- [x] Slice preview inspected through the open tube and flange transition
- [x] Final filament/nozzle mapping verified: PLA Pure A3 to main nozzle
- [x] Auto Bed Leveling explicitly set to Auto
- [x] Flow Dynamics Calibration explicitly set to Auto
- [x] Nozzle Offset Calibration changed from Off to Auto after the Studio update
- [x] No third-party model or profile included

The print was sent after a fresh final readback showed Auto Bed Leveling, Flow
Dynamics Calibration, and Nozzle Offset Calibration all set to Auto. Bambu
Studio accepted the cloud upload and showed the job in Printing Progress on
the X2D. The first live status check showed layer 0/204 during heatbed foreign
object detection, with an estimated finish time of 13:51 PDT.

## Outcome

- Actual result: print completed and the user tested it in the pegboard
- Dimensions/fit: the tube entered to the flange, confirming that its 36.8 mm
  insertion length was not too long. It remained noticeably wiggly. Because it
  reached the flange, this test did not show whether the hole is deeper than
  36.8 mm.
- Surface or structural defects: none reported
- Photos: none
- Print history or app evidence checked: live Bambu Studio job acceptance and
  startup state verified; later Device view showed 100%, layer 204/204, and
  `Finished`

## Diagnosis and next change

Make the second gauge 31.2 mm in diameter, removing the nominal diametral
clearance. Extend its insertion length to 39.0 mm, which is 0.7 mm beyond the
measured depth, so rear contact is visible. Do not force it if it binds.

## Durable lesson

For this specific pegboard, a 30.8 mm printed PLA peg enters a nominal 31.2 mm
hole but has more lateral movement than desired. A gauge shorter than the hole
cannot establish the usable depth when its flange seats first.
