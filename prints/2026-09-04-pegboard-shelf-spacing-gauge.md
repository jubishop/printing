# 2026-09-04 — Climbing pegboard shelf spacing gauge

- Status: planned; sliced and saved, not sent
- Started: not started
- Completed: not completed
- Related issue: none

## Goal

Check simultaneous insertion of two pegs before designing a one-piece shelf.
The user reported a perfect individual fit at 32.0 mm modeled diameter and
39.0 mm insertion length. Keep those dimensions fixed for this spacing test.

## Source and provenance

- Creator: Jubi, with OpenAI Codex modeling assistance
- Model URL: none; original local design
- Exact profile/profile ID: local OpenSCAD model, `part="spacing-gauge"`
- License and date checked: all rights reserved; 2026-09-04
- Local files committed: shared source, spacing-gauge STL/render, this record
- Modifications from upstream: not applicable
- Tool: OpenSCAD 2021.01
- Private 3MF: retained under the ignored `.local/models/` tree

## Measurement and geometry

- User's approximate nearest-edge gap: 146.5 mm, measured with calipers from
  the rightmost edge of the left hole to the leftmost edge of the right hole
- Modeled nearest-edge gap between pegs: 146.5 mm
- Trial modeled center spacing: 178.5 mm, using 146.5 + fitted CAD diameter 32.0
- This is an empirical starting spacing, not a direct hole-center measurement.
  The actual printed peg and physical hole diameters have not been remeasured.
- Each peg: 32.0 mm diameter, 39.0 mm usable insertion, 2.4 mm tube wall,
  1.0 mm tip chamfer
- Connecting bar: 24.0 mm wide, 8.0 mm thick
- Pull flanges: 42.0 mm diameter, 8.0 mm thick; same contact plane as the bar
- Overall envelope: 220.5 x 42.0 x 47.0 mm

## Hardware

- Printer configuration: Bambu Lab X2D
- Nozzle configuration: main and auxiliary 0.4 mm hardened steel
- Build plate selected: Textured PEI Plate
- Plate preparation: pending; user explicitly asked not to start printing

## Material routing

| Role | Filament/profile | Source slot/feed | Nozzle |
| --- | --- | --- | --- |
| Object | Bambu PLA Pure | Final AMS mapping pending | Main |
| Support base | None | Not applicable | Not applicable |
| Support interface | None | Not applicable | Not applicable |

## Profile and slice

- App and version: Bambu Studio 02.08.02.61
- Layer height: 0.20 mm, including initial layer; 235 layers
- Walls: 2
- Infill pattern/percentage: grid, 15%
- Supports: disabled
- Adhesion/brim: auto brim
- Temperatures: PLA profile nozzle 220 C; Textured PEI bed 55 C
- Speed/flow changes: none
- Dimensional compensation: XY contour and hole compensation 0 mm; circle
  compensation off; elephant-foot compensation 0.15 mm
- Estimated time/material: 1 hour 12 minutes 25 seconds; 40.22 g; 13.48 m
- Saved project settings compared with the successful v5 peg: identical

## Preflight

- [x] Exact STL: 4,268 triangles, one component, watertight, consistent face
  orientation; measured mesh gap, center spacing, diameters, and depth verified
- [x] All five earlier single-peg variants reproduce unchanged after refactor
- [x] X2D/nozzle/plate project settings verified
- [x] Object assigned to PLA on the main nozzle in sliced preview
- [x] One gauge fits on the selected plate, with both pegs upright
- [x] Full slice and contiguous first-layer contact inspected
- [x] Saved private 3MF archive integrity verified
- [x] Original model provenance recorded; no third-party model included
- [ ] Physical printer, nozzles, prepared plate, and material freshly checked
- [ ] Final AMS/nozzle mapping checked
- [ ] Auto Bed Leveling explicitly `Auto` immediately before send
- [ ] Flow Dynamics Calibration explicitly `Auto` immediately before send
- [ ] Nozzle Offset Calibration explicitly `Auto` immediately before send
- [ ] User authorizes sending after machine preparation

Studio is left in the prepared project. No spacing-gauge job has been sent.
The remaining live preflight must be completed before any later print.

## Outcome

- Actual result: not printed
- Dimensions/fit: not tested
- Surface or structural defects: not tested
- Photos: none stored
- Print history or app evidence checked: prepared project and sliced preview
  only; no print-history entry for this gauge

## Diagnosis and next change

First confirm the successful single peg fits each hole separately. Then test
whether both connected pegs enter together and the contact faces seat against
the board. Do not force insertion or bend the bar to make it fit. Pull evenly
from both ends to remove it. Adjust spacing only if both pegs fit separately
but not together; hole-axis alignment is another possible cause.

This is a spacing and alignment test, not a shelf load test.

## Durable lesson

No new reusable result until the spacing gauge has been physically tested.
