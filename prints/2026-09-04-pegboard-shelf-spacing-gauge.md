# 2026-09-04 — Climbing pegboard shelf spacing gauge

- Status: completed; spacing confirmed on the first two-peg trial
- Started: 2026-09-04 at 08:45 PDT
- Completed: 2026-09-04; exact completion time not observed
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
- Nozzle configuration: main and auxiliary 0.4 mm, freshly confirmed in the
  final send dialog; hardened steel is the recorded hardware baseline and
  saved project setting
- Build plate selected: Textured PEI Plate
- Plate preparation: user confirmed the machine was ready; live camera showed
  the installed textured plate clear of previous prints before sending

## Material routing

| Role | Filament/profile | Source slot/feed | Nozzle |
| --- | --- | --- | --- |
| Object | Bambu PLA Pure | AMS A3, white PLA | Main, 0.4 mm |
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
- [x] Live X2D, both nozzle diameters, clear plate, and material freshly checked
- [x] Final AMS/nozzle mapping checked: PLA A3 to main; auxiliary unused
- [x] Auto Bed Leveling explicitly `Auto` immediately before send
- [x] Flow Dynamics Calibration explicitly `Auto` immediately before send
- [x] Nozzle Offset Calibration explicitly `Auto` immediately before send
- [x] User authorizes sending after machine preparation

Nozzle Offset Calibration opened as `Off`; it was changed to `Auto` before
sending. The final dialog and saved application settings both showed all three
controls as `Auto`. Timelapse was `Off`.

The job was sent at 08:45 PDT. Independent Device-page readback showed the
exact spacing-gauge job, 0/235 layers, an active startup state, and a bed target
of 55 C. Studio initially estimated completion at 09:57 PDT.

## Outcome

- Actual result: completed; the user reported that it nailed the spacing on the
  first try
- Dimensions/fit: both fitted pegs entered their holes together, confirming the
  178.5 mm modeled center spacing for the final shelf
- Surface or structural defects: none reported
- Photos: none stored
- Print history or app evidence checked: prepared project, full sliced preview,
  final send mapping/calibrations, live camera, active Device-page job, and the
  user's completed-fit report

## Diagnosis and next change

No spacing change is needed. Reuse the successful 32.0 mm outside diameter,
39.0 mm insertion length, and 178.5 mm center spacing in the final shelf.

This is a spacing and alignment test, not a shelf load test.

## Durable lesson

The combination of 32.0 mm modeled peg diameter, 39.0 mm insertion length, and
178.5 mm center spacing fits both holes simultaneously with this printer,
material profile, orientation, and dimensional-compensation setup.
