# 2026-08-12 — Skillmill enlarged light-blue PLA tray

- Status: in progress
- Started: 2026-08-12 08:51 PDT
- Completed: pending
- Related issue: none

## Goal

Print the revised tray for the reversed M4 joint. Success requires four usable
captive locknut pockets, alignment with the revised PETG upper, a flat floor,
and clean 27 mm walls around the enlarged 175 x 100 mm footprint.

## Source and provenance

- Creator: original local design by Jubi with Codex
- Model URL: none; generated in this repository
- Exact profile/profile ID: custom support-free X2D PLA tray project
- License and date checked: not applicable; no third-party model used
- Local files:
  - `models/skillmill-rail-catchall/exports/skillmill-pla-tray.stl`
  - `models/skillmill-rail-catchall/exports/skillmill-pla-tray-x2d.3mf`
- Modifications from upstream: not applicable

## Hardware

- Printer: Bambu Lab X2D
- Nozzle size/type: 0.4 mm hardened steel on the main nozzle
- Build plate: Bambu Textured PEI Plate
- Plate preparation: user reported a clean installed plate and a prepared
  printer immediately before the job was sent

## Material routing

| Role | Filament/profile | Source slot/feed | Nozzle |
| --- | --- | --- | --- |
| Object | Light-blue Bambu PLA Pure | AMS A1 | Main, 0.4 mm |
| Support base | not used | not used | not used |
| Support interface | not used | external support spool remains loaded | not used |

## Profile and slice

- App and version: Bambu Studio 2.7.1.62
- Layer height: 0.16 mm
- Walls: 4
- Top/bottom shells: 6 / 5
- Infill pattern/percentage: grid, 20%
- Supports: disabled; the tray's broad floor is directly on the plate
- Adhesion/brim: automatic 5 mm brim setting; no manual brim override
- Temperatures: Bambu PLA Pure profile; no manual temperature change
- Speed/flow changes: none beyond the saved X2D standard process
- Estimated time/material: 2h46m / 97.49 g; 168 layers

## Preflight

- [x] OpenSCAD reported a simple 3D object
- [x] STL triangle-edge audit found zero open or non-manifold edges
- [x] Exact dimensions verified as 175 x 100 x 27 mm
- [x] Current STL replaced the inaccessible-joint prototype in the saved 3MF
- [x] Captive M4 locknut pockets and 11 mm vertical spacing inspected
- [x] Bambu Lab X2D, 0.4 mm main nozzle, and Textured PEI plate verified
- [x] Light-blue PLA mapped from AMS A1 to the main nozzle
- [x] Auxiliary nozzle and support filament omitted from this support-free job
- [x] Four walls, six top layers, five bottom layers, and 20% infill verified
- [x] Support-free slice preview inspected through the full 168-layer range
- [x] Automatic bed leveling, flow-dynamics calibration, and nozzle-offset
  calibration retained
- [x] Cloud transfer completed and the printer accepted the job at layer 0/168
- [x] No third-party files included

## Outcome

- Actual result: pending; printer accepted the job and began its pre-print
  sequence
- Dimensions/fit: pending; nominal outside dimensions are 175 x 100 x 27 mm
- Surface or structural defects: pending
- Photos: none committed
- Print history or app evidence checked: Bambu Studio Device view showed the
  accepted job at 0%, layer 0/168, during build-plate alignment detection with
  an 11:37 PDT estimated finish

## Diagnosis and next change

The preceding tray printed well but could not be fastened because its opposite
wall blocked screwdriver access. This revision uses captive nuts inside the
tray, rear-accessible screw heads in the PETG upper, 11 mm vertical screw
spacing, a 20 mm wider and 15 mm deeper footprint, and walls reduced by 11 mm.
The 27 mm outer wall top is flush with the reinforced bolt pad; usable wall
height above the 3.2 mm floor is 23.8 mm.

Inspect all four nut pockets, test the M4 hardware without forcing it, and then
confirm tray-to-upper alignment before loading the tray on the stopped
Skillmill.

## Durable lesson

Wait for physical inspection and assembled fit before promoting a reusable
rule to repository memory.
