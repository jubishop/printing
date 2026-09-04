# 2026-09-04 — Climbing pegboard shelf fit peg v5

- Status: completed
- Started: 2026-09-04 07:12 PDT
- Completed: by 2026-09-04; exact finish time not observed
- Related issue: none

## Goal

Test a 32.0 mm outside diameter with the user-confirmed 39.0 mm insertion
length. The fourth gauge was too long at 39.2 mm because it touched the back
before the flange seated. The working depth is now locked at 39.0 mm.

Success means little side-to-side movement, full seating, and removal with
ordinary hand pressure. Do not force the gauge if it binds.

## Source and provenance

- Creator: Jubi, with OpenAI Codex modeling assistance
- Model URL: none; original local design
- Exact profile/profile ID: local parametric OpenSCAD model, `fifth` variant
- License and date checked: all rights reserved; 2026-09-04
- Local files committed: shared source, variant STL/render, and this record;
  printer-specific 3MF remains private and ignored
- Modifications from upstream: not applicable
- Geometry change from v4: diameter +0.2 mm; insertion length -0.2 mm
- Unchanged geometry: 2.4 mm tube wall, 1.0 mm tip chamfer, 42.0 x 4.0 mm flange
- Tool: OpenSCAD 2021.01

## Hardware

- Printer: Bambu Lab X2D, verified in Studio and the send screen
- Nozzle size/type: main and auxiliary configured as 0.4 mm hardened steel
- Build plate: Textured PEI Plate
- Plate preparation: user reported the machine ready

## Material routing

| Role | Filament/profile | Source slot/feed | Nozzle |
| --- | --- | --- | --- |
| Object | Bambu PLA Pure | AMS A3 | Main, 0.4 mm |
| Support base | None | Not applicable | Not applicable |
| Support interface | None | Not applicable | Not applicable |

## Profile and slice

- App and version: Bambu Studio 02.08.02.61
- Layer height: 0.20 mm, including the initial layer; 215 layers
- Walls: 2; the modeled tube wall remains 2.4 mm thick
- Infill pattern/percentage: grid, 15%
- Supports: disabled
- Adhesion/brim: auto brim
- Temperatures: PLA profile nozzle 220 C; Textured PEI bed 55 C
- Speed/flow changes: none
- Dimensional compensation: XY contour and hole compensation 0 mm; circle
  compensation off; elephant-foot compensation 0.15 mm
- Estimated time/material: 41 minutes 22 seconds; 12.33 g; 4.14 m
- Saved project settings compared with v4: identical
- Local project retained under the ignored `.local/models/` tree

## Preflight

- [x] Exact STL checked: 2,300 triangles, one component, watertight, consistent
  face orientation; 32.0 mm body diameter and 39.0 mm insertion length
- [x] Printer, nozzle configuration, and plate verified
- [x] User confirmed physical machine preparation
- [x] PLA object assignment and final AMS A3/main-nozzle mapping verified
- [x] One upright gauge, flange on the plate, with no supports
- [x] Full preview and contiguous first-layer contact inspected
- [x] Auto Bed Leveling explicitly `Auto` immediately before send
- [x] Flow Dynamics Calibration explicitly `Auto` immediately before send
- [x] Nozzle Offset Calibration explicitly `Auto` immediately before send
- [x] All three values independently read back from Studio's saved settings
- [x] Saved 3MF archive integrity verified
- [x] No third-party model included

## Outcome

- Actual result: completed, based on the user's physical test
- Dimensions/fit: user reported the fit was perfect at 32.0 mm diameter and
  39.0 mm insertion length; fit in each hole separately was not specified
- Surface or structural defects: none reported
- Photos: none stored
- Print history or app evidence checked: live Studio showed the exact v5 job,
  0%, layer 0/215, and `Cooling chamber`; initial estimated finish 07:53 PDT
- Follow-up readback: advanced to `Identifying build plate type`; live camera
  showed the cleared textured plate. Estimated finish updated to 07:54 PDT.
- Completion readback on 2026-09-04: live Studio showed the exact v5 job at
  100%, layer 215/215, `Finished`.

## Diagnosis and next change

Keep both the 32.0 mm modeled diameter and 39.0 mm insertion length fixed.
Next, test two pegs joined by a rigid bar to check simultaneous insertion and
spacing. The user's approximate nearest-edge gap is 146.5 mm.

## Durable lesson

The user-confirmed single-peg fit is 32.0 x 39.0 mm. These are fitted model
dimensions, not a new measurement of the physical holes. The model source
and README record the result.
