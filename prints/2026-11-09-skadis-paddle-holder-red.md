# 2026-11-09 — One Scarlet Red SKÅDIS paddle holder

- Status: in progress
- Started: 2026-11-09 09:44 PST
- Completed: not yet observed
- Related iteration notes: none

## Goal

Print one additional paddle holder in red using the supported setup from the
[successful white single](2026-11-02-skadis-paddle-holder.md).

## Source and provenance

- Creator: PingPongMeister
- Model URL: [MakerWorld model 1741694, profile 1850928](https://makerworld.com/en/models/1741694-pingpong-paddle-holder#profileId-1850928)
- Exact source profile: `0.2mm layer, 2 walls, 15% infill`, plate 1
- License: CC BY-NC-SA 4.0, checked 2026-11-02
- Starting artifact: [committed single-holder X2D project](../models/skadis-paddle-holder/README.md)
- Modifications: synchronized the live printer and filament list, then assigned
  the single object to filament 3, Bambu PLA Matte in Scarlet Red. Geometry,
  placement, and the supported process recipe were retained.
- Saved a separate red project locally. The reusable model is already
  committed; this record adds no new model archive or generated G-code.

## Hardware

- Printer: Bambu Lab X2D
- Nozzles: main and auxiliary, 0.4 mm hardened steel, Standard flow; verified
  in the live Printer Parts dialog
- Build plate: Textured PEI, verified in the project, final send dialog, and
  live camera
- Plate preparation: user reported the machine ready. Live camera showed the
  installed textured plate without completed objects; four rectangular
  outlines were visible on its surface. Cleaning method was not recorded.

## Material routing

| Role | Filament/profile | Source slot/feed | Nozzle |
| --- | --- | --- | --- |
| Object | Bambu PLA Matte, Scarlet Red | AMS A3 | Main |
| Support base | Default/object PLA Matte | AMS A3 | Main |
| Support interface | Bambu Support For PLA/PETG, Nature | External spool | Auxiliary |

The live material dialogs identified A3 as Scarlet Red PLA Matte and the
external material as Support For PLA/PETG. Saved-project metadata confirmed
one printable object assigned to filament 3 and interfaces assigned to
filament 5. The sliced grouping and final send mapping confirmed main A3 and
auxiliary Ext.

## Profile and slice

- App: Bambu Studio 2.9.1.70
- Quantity: one holder on plate 1; 212 layers
- Layer height: 0.2 mm; walls: 2; infill: 15% grid
- Supports: automatic tree, Tree Hybrid, 35-degree threshold
- Interfaces: zero top Z distance and spacing; 50 mm/s for the active
  Standard-flow variants
- Adhesion: automatic brim, configured width 5 mm; prime tower enabled
- Temperatures: retained matched filament presets; startup bed target 55 °C
- Speed/flow changes: no manual changes to the retained process recipe
- Timelapse: Off
- Estimated time: 1h 25m 10s in the Device view
- Filament changes: 64

| Material | Model | Supports | Prime tower | Total |
| --- | --- | --- | --- | --- |
| Scarlet Red PLA Matte | 10.11 g | 2.74 g | 8.27 g | 21.13 g / 6.66 m |
| Dedicated support | 0 g | 0.59 g | 3.32 g | 3.91 g / 1.37 m |
| Total | 10.11 g | 3.33 g | 11.60 g | 25.04 g / 8.02 m |

These are slicer estimates; displayed columns have minor rounding differences.

## Preflight

- [x] Committed model, exact source profile, and one printable holder verified
- [x] Active X2D, nozzle hardware, and physical plate verified
- [x] Object and support materials checked against live inventory
- [x] Slice completed without a displayed warning; first layer and first five
  layers inspected for broad support footprints and plate clearance
- [x] Final main A3 and auxiliary Ext mapping verified
- [x] Auto Bed Leveling, Flow Dynamics Calibration, and Nozzle Offset
  Calibration all explicitly Auto immediately before Send
- [x] User explicitly authorized sending this red print in the request
- [x] Existing model attribution and license retained; private identifiers,
  camera photos, and generated G-code omitted from this record

## Outcome

Sent once. Studio showed the red single-holder thumbnail, the job name
`skadis-paddle-holder-one-red-x2d`, 25.04 g, active Pause/Stop controls, and
layer 0/212. The bed began warming toward 55 °C. The initial estimated finish
was 11:09 PST.

Job acceptance and startup are verified. Completion, first-layer quality,
support removal, defects, fit, and actual consumption remain unverified.

## Diagnosis and next change

No startup fault was displayed. No process change is indicated by the observed
startup state.

## Durable lesson

The [existing paddle-holder case](../memory/cases/2026-11-02-skadis-paddle-holder.md)
remains the validated physical result. This run records a switch to the loaded
red PLA Matte preset; its physical outcome is not yet known.
