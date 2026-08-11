# 2026-08-11 — Skillmill open-hinge PETG reprint

- Status: completed
- Started: 2026-08-11 09:21 PDT
- Completed: 2026-08-11 (time not recorded)
- Related issue: none

## Goal

Reprint the full right-hand PETG mount and lower saddle with usable, open M6
hinge bores. Success requires both parts to remain seated, both suspended hinge
faces to print cleanly, every hinge bore to accept the M6 bolt after ordinary
support removal, and the already validated 41.3 mm lined bore fit to remain
unchanged. The separate PLA tray is not part of this job.

## Source and provenance

- Creator: original local design by Jubi with Codex
- Model URL: none; generated in this repository
- Exact profile/profile ID: custom Bambu Studio process derived from `0.16mm Standard @BBL X2D`
- License and date checked: not applicable; no third-party model used
- Local files:
  - `models/skillmill-rail-catchall/exports/skillmill-petg-mount-upper-right-40mm.stl`
  - `models/skillmill-rail-catchall/exports/skillmill-catchall-lower-right-40mm.stl`
  - `models/skillmill-rail-catchall/exports/skillmill-catchall-petg-mount-right-40mm.3mf`
- Modifications from upstream: not applicable

## Hardware

- Printer: Bambu Lab X2D
- Nozzle size/type: 0.4 mm hardened steel on the main and auxiliary nozzles
- Build plate: Bambu Textured PEI Plate
- Plate preparation: user reported that the printer and cleaned plate were
  ready immediately before the job was sent

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
- Supports: tree(auto), Tree Hybrid, 35 degree threshold; support is allowed to
  start on model surfaces
- Support contact: 2 solid top interface layers, 0 mm top Z gap, 0 mm interface
  spacing
- Adhesion/brim: 8 mm outer brim with 0.1 mm object gap
- Temperatures: Bambu PETG Basic and support-interface profiles; no manual
  temperature change
- Speed/flow changes: none beyond the saved custom process
- Estimated time/material: 4h27m / 112.44 g; 360 layers

## Preflight

- [x] Exact final right-hand upper mount and matching lower verified
- [x] Failed 0.4 mm hinge-bore membranes removed from both printable models
- [x] Both generated STLs reported as simple 3D objects and passed a
  triangle-edge manifold audit
- [x] Final upper retained 421.4 mm2 of planar backplate-side bed contact
- [x] Replacement lower retained 556.6 mm2 of planar clamp-end bed contact
- [x] Bambu Lab X2D, 0.4/0.4 mm nozzles, and Textured PEI plate verified
- [x] Grey PETG mapped from AMS A4 to the main nozzle
- [x] Support for PLA/PETG mapped from the external feed to the auxiliary nozzle
- [x] Tree Hybrid supports allowed to start on model surfaces beneath the
  vertically shadowed lower knuckle
- [x] Open hinge bores and generated support regions inspected in Preview
- [x] Automatic bed leveling, flow-dynamics calibration, and nozzle-offset
  calibration retained
- [x] Cloud transfer completed and the printer accepted the job at layer 0/360
- [x] No third-party files included

## Outcome

- Actual result: completed. The user reported that both clamp parts looked
  good after removal from the plate.
- Dimensions/fit: the same 41.3 mm bore/liner combination already passed the
  physical rail-fit test
- Surface or structural defects: none reported in the completed open-bore
  reprint. M6 bolt pass-through and assembled hinge movement have not yet been
  reported separately.
- Photos: none committed
- Print history or app evidence checked: Bambu Studio Device view showed the
  named job at 0%, layer 0/360, with a 4h26m33s remaining estimate and a 13:47
  PDT estimated finish

## Diagnosis and next change

The prior modeled membranes sealed both M6 hinge bores and were too firm to
remove by hand. The lower membrane also failed to stabilize its surrounding
hinge face. The lower suspended outer knuckle is directly above the clean
bed-side knuckle in the print orientation. Build-plate-only support prevented a
branch from starting on that intermediate surface.

This attempt removes the membranes and permits support on model surfaces. The
dedicated support interface can now contact the open annular hinge faces from a
short, directly supported path. Inspect both parts before assembly. Do not use
the M6 bolt to force through fused PETG.

## Durable lesson

The completed parts passed the user's visual inspection. Wait for the M6 bolt
pass-through and assembled-hinge test before promoting the support correction
to repository memory. The validated rail-fit measurement remains in
`memory/skillmill-rail-measurement.md`.
