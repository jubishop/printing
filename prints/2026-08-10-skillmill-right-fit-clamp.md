# 2026-08-10 — Skillmill right-hand PETG fit clamp

- Status: completed; bore fit passed and hinge support defect documented
- Started: 2026-08-10 12:42 PDT
- Failure detected: 2026-08-10 13:14 PDT
- Related issue: none

## Goal

Print the final-hardware right-hand upper fit piece and matching lower saddle so
the fit from the provisional 40 mm input, liner compression, M6 hinge, and M6
latch can be tested before printing the full PETG mount and separate PLA tray.
Success requires the assembled clamp to close around the lined Skillmill rail
without spinning, while both M6 joints fit and operate without damaging the
printed pockets.

## Source and provenance

- Creator: original local design by Jubi with Codex
- Model URL: none; generated in this repository
- Exact profile/profile ID: custom Bambu Studio process derived from `0.16mm Standard @BBL X2D`
- License and date checked: not applicable; no third-party model used
- Local files committed:
  - `models/skillmill-rail-catchall/exports/skillmill-fit-upper-right-40mm.stl`
  - `models/skillmill-rail-catchall/exports/skillmill-catchall-lower-right-40mm.stl`
  - `models/skillmill-rail-catchall/exports/skillmill-catchall-lower-right-40mm.3mf`
- Modifications from upstream: not applicable

## Hardware

- Printer: Bambu Lab X2D (`Panda Factory`)
- Nozzle size/type: 0.4 mm hardened steel, main nozzle
- Build plate: Bambu Textured PEI Plate
- Plate preparation: user cleaned the plate and reinstalled it immediately before printing

## Material routing

| Role | Filament/profile | Source slot/feed | Nozzle |
| --- | --- | --- | --- |
| Object | Grey Bambu PETG Basic | AMS A4 | Main, 0.4 mm |
| Support base | Not used | — | — |
| Support interface | Not used; support filament remained loaded externally | External feed, unused | Auxiliary, unused |

## Profile and slice

- App and version: Bambu Studio; version not observed
- Layer height: 0.20 mm
- Walls: 5
- Top/bottom shells: 5 / 5
- Infill pattern/percentage: gyroid, 30%
- Supports: disabled; post-failure mesh inspection showed the exported orientation was not support-free
- Adhesion/brim: process default; no brim was intentionally added
- Temperatures: Bambu PETG Basic profile; bed target observed at 70 C during startup
- Speed/flow changes: none from the selected Bambu PETG Basic profile
- Estimated time/material: 1h33m / 41.18 g; 168 layers

## Preflight

- [x] Exact right-hand upper and matching right-hand lower STL verified
- [x] Bambu Lab X2D, 0.4 mm main nozzle, and Textured PEI plate verified
- [x] Grey Bambu PETG Basic mapped from AMS A4 to the main nozzle
- [x] Supports disabled and auxiliary support filament confirmed unused
- [x] Slice preview inspected after auto-arranging the two parts
- [x] Initial overlapping placement was corrected and the clean reslice had no path-conflict warning
- [x] Final one-filament main-nozzle mapping verified in the send dialog
- [x] Auto bed leveling, flow dynamics calibration, and nozzle-offset calibration left in automatic mode
- [x] Print accepted by the printer and entered startup at 0/168 layers
- [x] Live camera inspected at layer 1/168; the small PETG contact patches appeared smooth, but their lack of broad planar support was not yet apparent
- [x] No third-party files included

## Outcome

- Actual result: failed at layer 37/168 (23%); X2D AI spaghetti detection paused the job
- Dimensions/fit: not testable
- Surface or structural defects: at least the larger/right-hand part visibly tipped and peeled away from the plate; loose PETG accumulated at the rear-left of the plate
- Photos: pending
- Print history or app evidence checked: Bambu Studio warning `[0300-8003 130710]`; live Device view showed the AI-paused job at 23%, layer 37/168, with Resume and Stop controls available

## Diagnosis and next change

The failure is primarily an orientation/contact-area problem, not evidence that
the cleaned plate or PETG profile was inadequate. Both committed STLs are in
assembly orientation and have no coplanar bottom triangles at their minimum Z:

- `skillmill-fit-upper-right-40mm.stl` reaches minimum Z at the curved hinge
  barrel (`z = -6.5 mm`).
- `skillmill-catchall-lower-right-40mm.stl` reaches minimum Z at the curved
  outside of the rail saddle (`z = -27.05 mm`).

Bambu Studio therefore dropped each part onto curved tangent contact instead of
a broad flat face. With supports disabled and no brim, the growing cross-section
eventually had enough leverage to rock or detach a part. The tipped part and the
spaghetti location directly support this diagnosis. A dirty plate or wet PETG
could worsen adhesion, but neither explains the zero-area planar footprint.

Before retrying, reorient each clamp half onto a broad side face and inspect the
first several sliced layers, or generate purpose-oriented exports. Then add a
brim and use support only where the new orientation requires it, keeping support
out of the M6 bores and captive locknut pocket.

Correction prepared later on 2026-08-10: the ordinary fit-upper and lower
OpenSCAD selectors now rotate the unchanged clamp geometry onto the +X clamp-end
face. Regenerated right and left STLs preserve their previous triangle counts
and volumes, remain manifold, and provide 443.4 mm² (fit upper) and 564.1 mm²
(lower) of planar bed contact. The documented retry adds an 8 mm brim and
build-plate-only support under the suspended latch/hinge surfaces. No retry was
sent while the plate awaited cleaning.

## Corrected retry

- Status: completed successfully
- Started: 2026-08-10 13:34 PDT
- Models: regenerated right-hand fit upper and right-hand lower clamp STLs
- Orientation: each part printed upright on its planar +X clamp-end face
- Layer height: 0.20 mm
- Walls: 5
- Top/bottom shells: 5 / 5
- Infill: gyroid, 30%
- Adhesion: outer brim only, 8 mm width, 0.1 mm object gap
- Supports: tree(auto), Tree Hybrid style, 35 degree threshold, build-plate only
- Support contact: 2 solid top interface layers, 0 mm top Z gap, 0 mm interface spacing
- Support base: Grey Bambu PETG Basic, project filament 1, main nozzle
- Support interface: Bambu Support for PLA/PETG, project filament 2, auxiliary nozzle
- Prime tower: enabled
- Slice result: 160 layers, 56.46 g, 2h14m final printer estimate
- Final live mapping: main nozzle from AMS A4 (PETG); auxiliary nozzle from external feed (Support for PLA/PETG)
- Printer preflight: Panda Factory X2D, 0.4/0.4 mm nozzles, Textured PEI plate, automatic bed leveling, flow-dynamics calibration, and nozzle-offset calibration
- Preview inspection: broad continuous first-layer footprints/brims were present; the vertical rail channels and hinge bores remained open; support interfaces appeared only beneath suspended latch/hinge geometry
- Send result: cloud transfer completed and the printer entered startup at layer 0/160
- First-layer result: passed live visual inspection; both broad clamp-end
  footprints, their 8 mm brims, the support-base footprints, and the prime
  tower remained smooth and fully seated through the transition to layer 2/160

## Corrected retry outcome

- Print quality: the user reported that both parts turned out well.
- Hardware fit: the M6 hinge and latch hardware assembled successfully.
- Rail fit: with the intended rubber liner installed, the tightened clamp still
  slides slightly on the rail and is not as snug as required.
- Next revision: retain 40 mm only as the provisional input used for the first
  test and apply a direct -0.8 mm bore-diameter adjustment. This changes the
  modeled bore from 42.1 mm to 41.3 mm without claiming that the rail itself is
  exactly 40 mm. The only field measurement remains the approximate 125 mm
  fabric-tape circumference.

## 0.8 mm tighter-bore retry

- Status: completed
- Started: 2026-08-10 17:25 PDT
- Models: right-hand fit upper and matching lower, both regenerated with a
  41.3 mm modeled bore, 0.8 mm narrower than the tested 42.1 mm bore
- Latch hardware: unchanged M6 x 30 mm bolt, washer, and captive M6 locknut
- Plate preparation: the user reported that the installed build plate was ready
- Printer: Panda Factory Bambu Lab X2D with 0.4 mm main and auxiliary nozzles
- Build plate: Textured PEI
- Layer height: 0.20 mm
- Walls: 5
- Top/bottom shells: 5 / 5
- Infill: gyroid, 30%
- Adhesion: outer brim only, 8 mm width, 0.1 mm object gap
- Supports: tree(auto), Tree Hybrid style, 35 degree threshold, build-plate only
- Support contact: 2 solid top interface layers, 0 mm top Z gap, 0 mm interface
  spacing
- Support base: Grey Bambu PETG Basic, project filament 1, main nozzle
- Support interface: Bambu Support for PLA/PETG, project filament 2, auxiliary
  nozzle
- Prime tower: enabled
- Slice result: 160 layers, 56.13 g, 2h13m final printer estimate
- Preview inspection: both planar clamp-end footprints had continuous 8 mm
  brims; support-base footprints and the prime tower were present; no toolpath
  collision warning appeared
- Final live mapping: main nozzle from AMS A4 (PETG); auxiliary nozzle from the
  external feed (Support for PLA/PETG)
- Calibration settings: automatic bed leveling, flow-dynamics calibration, and
  nozzle-offset calibration
- Send result: cloud transfer completed; the printer accepted the job and
  entered automatic bed leveling at layer 0/160
- First-layer result: not observed live in this record; the full print completed
- Saved project: Bambu Studio 2.7.1.62 project updated with the current meshes
  and slice settings; no generated G-code; account designer identifier removed
  before publication

### Tighter-bore outcome

- Rail fit: passed. The user reported that the 41.3 mm modeled bore with the
  installed liner fit the rail perfectly.
- General print result: both clamp halves completed and could be handled and
  assembled for inspection.
- Surface defect: the first face of one suspended hinge knuckle printed as
  loose concentric PETG rings with strings across the M6 bore.
- Diagnosis: the end-on orientation leaves one knuckle on each half starting
  above the build plate. Its first supported surface was an annulus, or thin
  ring, around the open bore. The support interface did not carry those first
  ring-shaped perimeters cleanly. This is a repeatable geometry/orientation
  weakness, not evidence of an incorrect rail bore or ordinary wet-filament
  stringing.
- Correction: add a removable 0.4 mm, two-layer membrane across the M6 bore at
  each suspended knuckle start. This makes the first supported face a solid
  disk. The membrane is pushed out with the M6 bolt or a 6 mm drill bit turned
  by hand after printing.

## Durable lesson

Do not label an export support-free merely because Studio produces a warning-free
slice. For functional curved parts, verify the actual coplanar first-layer area
and the growth of the first several layers in Preview before sending the job.
