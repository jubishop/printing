# 2026-11-04 — One Baby Blue SKÅDIS paddle holder

- Status: in progress
- Started: 2026-11-04 19:03 PST
- Completed: not yet observed
- Related issue: none

## Goal

Print one additional paddle holder in light blue, reusing the supported setup
from the [successful white single](2026-11-02-skadis-paddle-holder.md).

## Source and provenance

- Creator: PingPongMeister
- Source: [MakerWorld model 1741694, profile 1850928](https://makerworld.com/en/models/1741694-pingpong-paddle-holder#profileId-1850928)
- Exact profile: `0.2mm layer, 2 walls, 15% infill`
- License: CC BY-NC-SA 4.0, checked 2026-11-02
- Starting artifact: [committed single-holder X2D project](../models/skadis-paddle-holder/README.md)
- Modifications: synchronized current printer information and filaments;
  changed the single object's assignment to project filament 3, Baby Blue PLA.
  Geometry, placement, and the active supported recipe were retained.
- Saved a separate Baby Blue project locally; no new model or G-code is
  committed with this record.

## Hardware

- Printer: Bambu Lab X2D
- Nozzles: main and auxiliary, 0.4 mm hardened steel, standard flow; checked in
  the live Printer Parts dialog
- Build plate: Textured PEI, selected in the project and final send dialog
- Plate preparation: user reported ready. The camera's recent still showed the
  textured plate without completed parts; live video was initially black and
  became visible during job startup. Cleaning method was not recorded.

## Material routing

| Role | Filament/profile | Source slot/feed | Nozzle |
| --- | --- | --- | --- |
| Object | Bambu PLA Pure, Baby Blue | AMS A3 | Main |
| Support bodies | Default/object PLA | AMS A3 | Main |
| Support interfaces | Bambu Support For PLA/PETG | External spool | Auxiliary |

The live A3 material dialog identified PLA Pure in Baby Blue. The saved project
contains one printable object assigned to filament 3. The sliced grouping and
final send dialog confirmed filament 3 on the main nozzle and support filament
5 on the auxiliary nozzle, mapped to A3 and Ext respectively.

## Profile and slice

- App: Bambu Studio 2.9.1.70, updated by the user before this slice
- Quantity: one holder on plate 1
- Layer height: 0.2 mm; walls: 2; infill: 15% grid
- Supports: automatic tree, Tree Hybrid, 35-degree threshold
- Support interfaces: zero top Z distance and zero interface spacing;
  50 mm/s for the active standard-flow nozzle variants
- Adhesion: automatic brim, configured width 5 mm; prime tower enabled
- Temperatures: retained material presets; startup bed target observed at 55 °C
- Speed/flow changes: none to the active recipe
- Timelapse: Off
- Estimated time: 1h 33m 2s in the Device view
- Slicer-reported filament changes: 64

| Material | Model | Supports | Prime tower | Total |
| --- | --- | --- | --- | --- |
| Baby Blue PLA | 9.25 g | 2.37 g | 7.77 g | 19.39 g / 6.50 m |
| Dedicated support | 0 g | 0.59 g | 3.32 g | 3.91 g / 1.37 m |
| Total | 9.25 g | 2.95 g | 11.10 g | 23.30 g / 7.87 m |

These are slicer estimates, with minor rounding differences between columns.

## Preflight

- [x] Validated starting project and exactly one printable holder verified
- [x] Active X2D, nozzle hardware, plate selection, and camera image checked
- [x] Live Baby Blue material identity and object/support assignments verified
- [x] Slice completed without a displayed warning; first layer and first five
  layers inspected for broad support footprints and plate clearance
- [x] Final mapping verified: main AMS A3 and auxiliary external support
- [x] Auto Bed Leveling, Flow Dynamics Calibration, and Nozzle Offset
  Calibration all explicitly Auto, rechecked immediately before sending
- [x] User approved sending after receiving the completed preflight
- [x] Private photos, account/device identifiers, and generated G-code omitted

## Outcome

Sent once. Studio switched to Device and showed the single blue holder
thumbnail, the Baby Blue project name, 23.30 g, active pause/stop controls, and
layer 0/212. Startup status was `Cooling chamber`, with the bed warming toward
55 °C and an initial estimated finish time of 20:36 PST.

This confirms job acceptance and startup. Completion, first-layer quality,
support removal, defects, fit, and actual consumption remain unverified.

## Diagnosis and next change

No startup fault was displayed. No process change is indicated by the observed
startup state.

## Durable lesson

The [existing paddle-holder case](../memory/cases/2026-11-02-skadis-paddle-holder.md)
remains the validated physical result. This run records a color substitution
and a fresh slice in the updated Studio; its physical outcome is not yet known.
