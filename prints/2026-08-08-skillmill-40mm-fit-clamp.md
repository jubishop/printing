# 2026-08-08 — Skillmill 40 mm rail fit clamp

- Status: in progress
- Started: 2026-08-08 22:43 PDT
- Completed: pending
- Related issue: none

## Goal

Validate the 40 mm clamp bore, fully printed hinge, and coarse printed latch
thread before printing the attached catch-all tray. Success means the lined
clamp closes around the Skillmill rail without bottoming out, the screw engages
cleanly, and the empty clamp resists gentle rotation without damaging the rail.

## Source and provenance

- Creator: original model created for this repository
- Model URL: none
- Exact profile/profile ID: local `skillmill-fit-test-40mm-two-plate` project,
  plate 1, `PETG fit clamp`
- License and date checked: original work; all rights reserved as of 2026-08-08
- Local files committed: parametric OpenSCAD source, eight 40 mm STL exports,
  assembly render, and model documentation under
  `models/skillmill-rail-catchall/`
- Modifications from upstream: none; no upstream geometry used
- Local configured project:
  `.local/models/skillmill-fit-test-40mm-two-plate.3mf` (ignored by Git;
  SHA-256 `d1d96b2a768e532332841946816742fcbbd85b63b03c265e6c2a2807603acac9`)

## Hardware

- Printer: Bambu Lab X2D
- Nozzle size/type: 0.4 mm hardened-steel main and auxiliary nozzles
- Build plate: Textured PEI Plate
- Plate preparation: user reported the machine prepped and ready; the live
  camera showed the installed plate empty before the job was sent

## Material routing

| Role | Filament/profile | Source slot/feed | Nozzle |
| --- | --- | --- | --- |
| Object | Bambu PETG Basic | AMS A4 | Main |
| Support base | Bambu PETG Basic | AMS A4 | Main |
| Support interface | Bambu Support for PLA/PETG | External feed | Auxiliary/right |

## Profile and slice

- App and version: Bambu Studio `02.07.01.62`
- Layer height: 0.16 mm
- Walls: 6; 5 top and 5 bottom shells
- Infill pattern/percentage: grid, 30%
- Supports: Tree Hybrid; PETG support base; dedicated support interface;
  35-degree threshold; 2 top interface layers; 0 mm top Z distance; 0 mm
  interface spacing; avoid interface filament for support base enabled; prime
  tower enabled
- Adhesion/brim: automatic 5 mm brim setting; final slice showed no conflict or
  floating-region warning
- Temperatures: system Bambu PETG Basic and Support for PLA/PETG profiles; no
  temperature overrides added
- Speed/flow changes: outer wall 40 mm/s; support interface 50 mm/s; no manual
  flow override
- Estimated time/material: 3h19m, 60.65 g total

## Preflight

- [x] Exact local model and PETG fit-test plate verified
- [x] Similar MakerWorld candidates rejected because they did not match the required geometry
- [x] Live compatibility with the selected X2D verified in Studio and by job acceptance
- [x] Printer, nozzle, and physical build plate verified
- [x] Object/support material assignments verified
- [x] Slice preview inspected in Studio
- [x] Final filament/nozzle mapping verified
- [x] First-layer, prime-tower, support, and collision risks considered
- [x] Third-party files omitted; model provenance recorded

## Outcome

- Actual result: in progress; Bambu Studio reported 0%, layer 0/241, and
  `Homing toolhead` after the printer accepted the job
- Dimensions/fit: pending
- Surface or structural defects: pending
- Photos: pending
- Print history or app evidence checked: final send dialog mapped PETG from AMS
  A4 to the main nozzle and Support for PLA/PETG from the external feed to the
  auxiliary nozzle; the device view entered active printing at 22:43 PDT

## Diagnosis and next change

Pending the completed print and stationary rail fit test. Before printing the
full catch-all upper, check the screw in the lower saddle off-machine, install
approximately 0.8 mm soft liner, and record the remaining latch gap and any
rotation under gentle hand load.

## Durable lesson

No reusable conclusion yet; this is the first physical validation of the
40 mm clamp and printed hardware.
