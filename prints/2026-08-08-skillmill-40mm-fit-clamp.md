# 2026-08-08 — Skillmill 40 mm rail fit clamp

- Status: failed (dimensional fit; print quality successful)
- Started: 2026-08-08 22:43 PDT
- Completed: by 2026-08-09 (exact time not recorded)
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

- Actual result: completed cleanly; the user reported that it “printed great
  and looks great,” but the assembled clamp was loose enough to spin freely
  around the rail
- Dimensions/fit: failed the grip requirement; the nominal 40 mm input plus
  0.8 mm radial liner allowance and 0.25 mm radial fit clearance produced a
  42.1 mm bore
- Surface or structural defects: none reported
- Photos: pending
- Print history or app evidence checked: final send dialog mapped PETG from AMS
  A4 to the main nozzle and Support for PLA/PETG from the external feed to the
  auxiliary nozzle; the device view entered active printing at 22:43 PDT

## Diagnosis and next change

The print-quality result validates the geometry and PETG/support process, while
the free rotation shows that the first bore was too large for the way it was
tested. The nominal 40 mm rail measurement still agrees with the measured
125 mm circumference; the excess comes from the modeled liner and fit
allowances. A 36 mm rail input with those allowances would create a 38.1 mm
bore and is likely to be undersized for the measured rail.

Before reprinting, distinguish between two intended interfaces:

- For a lined clamp, test the 40 mm print with the intended approximately
  0.8 mm soft liner and a tightened screw.
- For a bare-plastic fit test, keep the 40 mm rail diameter but set liner
  thickness to 0 and reduce radial fit clearance to approximately 0.15 mm,
  producing a 40.3 mm bore.

## Durable lesson

Keep physical rail diameter separate from liner and printing clearance. The
first test demonstrates that adding the full liner allowance without installing
the liner leaves a nominal 40 mm clamp approximately 2.1 mm oversized.
