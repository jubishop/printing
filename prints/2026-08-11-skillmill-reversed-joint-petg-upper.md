# 2026-08-11 — Skillmill reversed-joint PETG upper

- Status: in progress
- Started: 2026-08-11 21:42 PDT
- Completed: pending
- Related issue: none

## Goal

Print only the revised right-hand PETG upper mount. Success requires the proven
open M6 hinge bore, four usable rear-facing M4 pan-head counterbores with a
straight screwdriver approach, and compatibility with the already validated
lower clamp. The lower clamp and PLA tray are not part of this job.

## Source and provenance

- Creator: original local design by Jubi with Codex
- Model URL: none; generated in this repository
- Exact profile/profile ID: custom Bambu Studio process derived from the
  validated open-hinge X2D project
- License and date checked: not applicable; no third-party model used
- Local files:
  - `models/skillmill-rail-catchall/exports/skillmill-petg-mount-upper-right-40mm.stl`
  - `models/skillmill-rail-catchall/exports/skillmill-reversed-joint-petg-upper-right-40mm.3mf`
- Modifications from upstream: not applicable

## Hardware

- Printer: Bambu Lab X2D
- Nozzle size/type: 0.4 mm hardened steel on the main and auxiliary nozzles
- Build plate: Bambu Textured PEI Plate
- Plate preparation: user reported that the printer and build plate were ready
  immediately before the job was sent

## Material routing

| Role | Filament/profile | Source slot/feed | Nozzle |
| --- | --- | --- | --- |
| Object | Grey Bambu PETG Basic | AMS A4 | Main, 0.4 mm |
| Support base | Grey Bambu PETG Basic | AMS A4 | Main, 0.4 mm |
| Support interface | Bambu Support for PLA/PETG | External feed | Auxiliary, 0.4 mm |

## Profile and slice

- App and version: Bambu Studio 2.7.1.62
- Layer height: 0.20 mm
- Walls: 5
- Top/bottom shells: 5 / 5
- Infill pattern/percentage: gyroid, 30%
- Supports: tree(auto), Tree Hybrid, 35 degree threshold; support may start on
  model surfaces
- Support contact: 2 solid top interface layers, 0 mm top Z gap, and 0 mm
  interface spacing
- Adhesion/brim: 8 mm outer brim with 0.1 mm object gap
- Temperatures: Bambu PETG Basic and support-interface profiles; no manual
  temperature change
- Speed/flow changes: none beyond the saved custom process
- Estimated time/material: 3h32m / 88.23 g; 360 layers

## Preflight

- [x] Exact revised right-hand upper imported by full path
- [x] Saved 3MF metadata identifies only
  `skillmill-petg-mount-upper-right-40mm.stl`; lower clamp is absent
- [x] OpenSCAD reported a simple 3D object and the STL passed a triangle-edge
  manifold audit with zero open or non-manifold edges
- [x] Four rear-facing M4 counterbores and 11 mm vertical spacing inspected
- [x] Bambu Lab X2D, 0.4/0.4 mm nozzles, and Textured PEI plate verified
- [x] Grey PETG mapped from AMS A4 to the main nozzle
- [x] Support for PLA/PETG mapped from the external feed to the auxiliary nozzle
- [x] Tree Hybrid supports reach the horizontal M4 counterbores and hinge faces
- [x] Open hinge bore and generated support-interface paths inspected in Preview
- [x] Automatic bed leveling, flow-dynamics calibration, and nozzle-offset
  calibration retained
- [x] Cloud transfer completed and the printer accepted the job at layer 0/360
- [x] No third-party files included

## Outcome

- Actual result: pending; printer accepted the upper-only job and began its
  pre-print sequence
- Dimensions/fit: pending; lower clamp remains the previously validated part
- Surface or structural defects: pending
- Photos: none committed
- Print history or app evidence checked: Bambu Studio Device view showed
  `skillmill-reversed-joint-petg-upper-right-40mm` at 0%, layer 0/360, with
  3h31m50s remaining and a 01:12 PDT estimated finish

## Diagnosis and next change

The preceding joint put the four Phillips screw heads inside the deep PLA tray.
The opposite tray wall prevented a straight screwdriver approach even though
the holes aligned. This revision moves the recessed heads to the exposed rear
of the PETG backplate, moves the captive locknuts into the next PLA tray, and
increases vertical hole spacing from 9 mm to 11 mm. Inspect all four
counterbores and the hinge bore before printing the replacement tray.

## Durable lesson

Wait for physical inspection and the reversed PLA tray assembly test before
promoting the accessible-fastener rule to repository memory.
