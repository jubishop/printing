# 2026-08-10 — Skillmill final right-hand PETG mount

- Status: failed
- Started: 2026-08-10 21:26 PDT
- Completed: 2026-08-11 (time not recorded)
- Related issue: none

## Goal

Print the final right-hand PETG upper mount and a replacement lower saddle. The
upper includes the structural bridge, tray shelf, and backplate. The lower is
reprinted because the fit-test lower had a malformed supported hinge face.
Success requires both parts to remain seated, every supported knuckle to print
cleanly, and all M4/M6 hardware openings to remain usable. The separate PLA
tray is not part of this job.

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
- Plate preparation: user reported that the printer and installed plate were ready immediately before the job was sent

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
- Supports: tree(auto), Tree Hybrid, 35 degree threshold, build plate only
- Support contact: 2 solid top interface layers, 0 mm top Z gap, 0 mm interface spacing
- Adhesion/brim: 8 mm outer brim with 0.1 mm object gap
- Temperatures: Bambu PETG Basic and support-interface profiles; no manual temperature change
- Speed/flow changes: none beyond the saved custom process
- Estimated time/material: 4h23m / 111.07 g; 360 layers

## Preflight

- [x] Exact final right-hand upper mount and matching replacement lower verified
- [x] Both generated STLs reported as simple 3D objects and passed a triangle-edge manifold audit
- [x] Final upper verified with 421.4 mm2 of planar backplate-side bed contact
- [x] Replacement lower verified with 556.6 mm2 of planar clamp-end bed contact
- [x] Intentional 0.4 mm removable membranes added at suspended hinge-bore starts
- [x] Bambu Lab X2D, 0.4/0.4 mm nozzles, and Textured PEI plate verified
- [x] Grey PETG mapped from AMS A4 to the main nozzle
- [x] Support for PLA/PETG mapped from the external feed to the auxiliary nozzle
- [x] Build-plate-only tree supports and solid auxiliary-filament interfaces verified in Preview
- [x] Broad first-layer footprints, 8 mm brims, support footprints, and prime tower inspected
- [x] Automatic bed leveling, flow-dynamics calibration, and nozzle-offset calibration retained
- [x] Cloud transfer completed and the printer accepted the job at layer 0/360
- [x] No third-party files included

## Outcome

- Actual result: failed. Both PETG parts completed, but neither hinge bore was
  usable.
- Dimensions/fit: the same 41.3 mm bore/liner combination already passed the
  physical rail-fit test.
- Surface or structural defects: the upper mount's suspended hinge face looked
  clean, but its modeled membrane sealed the bore. The lower saddle's membrane
  also sealed the bore, and the surrounding suspended hinge face printed as a
  dense malformed mass. The user could make only a pin-prick in the lower
  membrane and could not safely clear either hole by hand.
- Photos: user-supplied inspection photos were reviewed but are not stored in
  this public repository.
- Print history or app evidence checked: Bambu Studio showed the job completed
  at 360/360 layers in 4h22m59s using 111.07 g.

## Diagnosis and next change

The 0.4 mm, two-layer membrane was not practically sacrificial in PETG and must
not be retained. It sealed both holes too firmly to remove by hand. It also did
not fix the lower face because that suspended outer knuckle is vertically
shadowed by the clean bed-side knuckle. With build-plate-only support enabled,
the slicer could not begin a support branch on the intermediate knuckle surface.

The next attempt removes every membrane and allows Tree Hybrid support to start
on model surfaces. This lets the lower support rise directly from the clean
knuckle beneath the failed face while the dedicated auxiliary-filament
interface supports the open annulus.

## Durable lesson

See `memory/skillmill-rail-measurement.md` for the validated bore/liner result.
Do not model a solid closure across a functional bore unless removal has first
been validated in a small test coupon. For vertically stacked features, inspect
whether build-plate-only support prevents the slicer from using a clean model
surface beneath the overhang.
