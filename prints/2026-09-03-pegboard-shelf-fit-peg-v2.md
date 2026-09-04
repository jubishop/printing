# 2026-09-03 — Climbing pegboard shelf fit peg v2

- Status: completed
- Started: 2026-09-03 17:31 PDT
- Completed: by 2026-09-03 19:31 PDT
- Related issue: none

## Goal

Resolve the two uncertainties left by the first gauge. Success means the
31.2 mm peg has less side-to-side movement while still inserting and removing
with ordinary hand pressure. The 39.0 mm insertion length should touch the rear
of the hole before the flange seats if the measured 38.3 mm depth is close.

## Source and provenance

- Creator: Jubi, with OpenAI Codex modeling assistance
- Model URL: none; original local design
- Exact profile/profile ID: local parametric OpenSCAD model, `second` variant
- License and date checked: all rights reserved; 2026-09-03
- Local files committed: shared source, variant STL/render, and this record;
  printer-specific 3MF remains private and ignored
- Modifications from upstream: not applicable

## Observed dimensions

- Hole diameter: approximately 31.2 mm for both holes
- Hole depth: approximately 38.3 mm for both holes
- Test peg outside diameter: 31.2 mm
- Test peg insertion length: 39.0 mm
- Diametral clearance: 0.0 mm nominal
- Intentional depth overtravel: 0.7 mm

## Hardware

- Printer: Bambu Lab X2D; synchronized from the live printer
- Nozzle size/type: main and auxiliary 0.4 mm, standard-flow configuration;
  main nozzle selected for this print
- Build plate: Textured PEI Plate selected in the project and send screen;
  user reported that the prepared machine remained ready before send
- Plate preparation: user reported that the prepared machine remained ready
  before send

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
- Estimated time/material: 41 minutes 10 seconds; 12.10 g; 4.06 m

## Preflight

- [x] Exact local v2 STL verified as one connected, watertight mesh
- [x] X2D, both active 0.4 mm nozzle diameters, and Textured PEI project
  selection verified
- [x] Physical build plate and preparation confirmed ready by the user before
  print; Textured PEI Plate selected on the send screen
- [x] Object material assignment verified
- [x] Upright orientation with flange on the plate verified
- [x] Slice preview inspected
- [x] Current filament/nozzle mapping verified: PLA Pure A3 to main nozzle
- [x] Auto Bed Leveling freshly rechecked immediately before send: Auto
- [x] Flow Dynamics Calibration freshly rechecked immediately before send: Auto
- [x] Nozzle Offset Calibration freshly rechecked immediately before send: Auto
- [x] No third-party model or profile included

Immediately before send, the screen and Bambu Studio configuration both showed
all three calibration controls as `Auto`. Bambu Studio uploaded the job through
the cloud service. The live device view then progressed through bed inspection,
plate identification, filament loading, and nozzle cleaning. At 17:35 PDT it
showed 1%, layer 0/215, while running Auto Bed Leveling, with no alert or
intervention request.

## Outcome

- Actual result: completed successfully; live Bambu Studio readback showed 100%
  and layer 215/215, Finished
- Dimensions/fit: 39.0 mm insertion depth was good; 31.2 mm outside diameter
  still felt slightly narrow and had unwanted movement
- Surface or structural defects: none reported
- Photos: none
- Print history or app evidence checked: live Bambu Studio device view showed
  the named job Finished at 100%, layer 215/215

## Diagnosis and next change

Keep the confirmed 39.0 mm insertion length. Increase only the outside diameter
by 0.4 mm, to 31.6 mm, for the third gauge. Do not force the larger gauge if it
starts to bind.

## Durable lesson

The 39.0 mm insertion length is suitable for this pegboard. Modeled outside
diameters through 31.2 mm remained too loose with this printer/profile pairing.
