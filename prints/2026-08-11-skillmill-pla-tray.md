# 2026-08-11 — Skillmill light-blue PLA tray

- Status: completed
- Started: 2026-08-11 15:19 PDT
- Completed: 2026-08-11 (time not recorded)
- Related issue: none

## Goal

Print the removable catchall tray that bolts to the validated PETG Skillmill
rail mount. Success requires a flat tray floor, clean walls, and four usable M4
mounting holes that align with the current PETG backplate.

## Source and provenance

- Creator: original local design by Jubi with Codex
- Model URL: none; generated in this repository
- Exact profile/profile ID: custom Bambu Studio process derived from
  `0.16mm Standard @BBL X2D`
- License and date checked: not applicable; no third-party model used
- Local files:
  - `models/skillmill-rail-catchall/exports/skillmill-pla-tray.stl`
  - `models/skillmill-rail-catchall/exports/skillmill-pla-tray-x2d.3mf`
- Modifications from upstream: not applicable

## Hardware

- Printer: Bambu Lab X2D
- Nozzle size/type: 0.4 mm hardened steel main nozzle
- Build plate: Bambu Textured PEI Plate
- Plate preparation: user reported that the printer and plate were ready
  immediately before the job was sent

## Material routing

| Role | Filament/profile | Source slot/feed | Nozzle |
| --- | --- | --- | --- |
| Object | Light-blue Bambu PLA Pure | AMS A1 | Main, 0.4 mm |
| Support base | not used | not used | not used |
| Support interface | not used | external spool remains loaded | not used |

## Profile and slice

- App and version: Bambu Studio 2.7.1.62
- Layer height: 0.16 mm
- Walls: 4
- Top/bottom shells: 6 / 5
- Infill pattern/percentage: grid, 20%
- Supports: disabled; the tray is oriented with its broad floor on the plate
- Adhesion/brim: automatic 5 mm brim setting; no manual brim override
- Temperatures: Bambu PLA Pure profile; no manual temperature change
- Speed/flow changes: none beyond the X2D standard process
- Estimated time/material: 2h47m / 95.47 g; 237 layers

## Preflight

- [x] Exact local PLA tray and intended plate verified
- [x] Bambu Lab X2D, 0.4 mm main nozzle, and Textured PEI plate verified
- [x] Light-blue PLA mapped from AMS A1 to the main nozzle
- [x] Auxiliary nozzle and support filament omitted from this support-free job
- [x] Four walls, five bottom layers, and 20% infill verified in the saved 3MF
- [x] Supports disabled in the process and verified in the sliced preview
- [x] Broad first-layer footprint and tray orientation inspected in Preview
- [x] Automatic bed leveling, flow-dynamics calibration, and nozzle-offset
  calibration retained
- [x] Cloud transfer completed and the printer accepted the job at layer 0/237
- [x] No third-party files included

## Outcome

- Actual result: the tray printed, but the tray and PETG upper cannot be
  assembled practically. The opposite tray wall blocks a straight screwdriver
  approach to the four inward-facing Phillips screw heads.
- Dimensions/fit: nominal model size is 155 x 85 x 38 mm; the physical screw
  centers aligned closely enough to reveal the access failure during assembly
- Surface or structural defects: none reported; this is a joint-orientation
  design failure rather than a print-quality failure
- Photos: none committed
- Print history or app evidence checked: Bambu Studio Device view showed
  `skillmill-pla-tray-x2d` at 0%, layer 0/237, with 2h46m41s remaining and an
  18:05 PDT estimated finish

## Diagnosis and next change

Reverse the joint. Put the captive M4 locknuts inside the PLA tray and the
recessed Phillips heads on the exposed rear of the PETG backplate. Because both
joint halves must be reprinted, increase the paired screw spacing from 9 mm to
11 mm at the same time. Reuse the existing lower clamp and M4 x 12 mm hardware.

## Durable lesson

For a deep open bin, do not place driven fastener heads on an inner wall unless
a real screwdriver has a verified straight approach. Validate tool access, not
only fastener clearance and thread engagement.
