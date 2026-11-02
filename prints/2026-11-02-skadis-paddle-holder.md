# 2026-11-02 — One SKÅDIS ping pong paddle holder

- Status: in progress
- Started: 2026-11-02 11:28 PST
- Completed: not yet observed
- Related issue: none

## Goal

Print one holder for a ping pong paddle on an IKEA SKÅDIS pegboard. Success
requires a completed print, removable supports, secure pegboard fit, and a
stable paddle fit; none of those final outcomes has been observed yet.

## Source and provenance

- Creator: PingPongMeister
- Model: [Pingpong paddle holder](https://makerworld.com/en/models/1741694-pingpong-paddle-holder)
- Exact designer profile: [1850928](https://makerworld.com/en/models/1741694-pingpong-paddle-holder#profileId-1850928),
  titled `0.2mm layer, 2 walls, 15% infill`
- License observed 2026-11-02: Creative Commons Attribution-Noncommercial-Share
  Alike 4.0
- Local files committed: none; this record contains no model, project, or G-code.
- Modifications: adapted the source project to X2D; synchronized current
  materials; enabled tree supports with dedicated support interfaces.

## Hardware

- Printer: Bambu Lab X2D
- Nozzles: main and auxiliary, 0.4 mm hardened steel, standard flow
- Build plate: Textured PEI, selected in Studio and observed in the live camera
- Plate preparation: user reported the printer ready; camera showed the plate
  empty. Cleaning method was not recorded.

## Material routing

| Role | Filament/profile | Source slot/feed | Nozzle |
| --- | --- | --- | --- |
| Object | White Bambu PLA Pure | AMS A2 | Main |
| Support base | Default/object PLA | AMS A2 | Main |
| Support interface | Bambu Support For PLA/PETG | External spool | Auxiliary |

The live synchronization, sliced filament grouping, and final send dialog were
checked. The user also confirmed support filament remained on the auxiliary
feed. Other synchronized AMS materials were not assigned to this print.

## Profile and slice

- App: Bambu Studio 2.8.2.61
- Quantity: one `Schlägerhalter_V6.step` object on plate 1
- Layer height: 0.2 mm
- Walls: 2
- Infill: 15% grid
- Supports: automatic tree, Tree Hybrid, 35-degree threshold
- Support interfaces: filament 5; zero top Z distance and zero interface
  spacing, following Studio's recommendation for this material pairing
- Support base: default; avoid using interface filament for support body enabled
- Adhesion: automatic brim, configured width 5 mm; broad support footprints
  and the first five sliced layers were inspected
- Bed target observed during startup: 55 °C
- Temperature and speed presets: synchronized X2D material profiles; accepted
  Studio's support-interface recommendations, including 50 mm/s interface speed
- Estimated time/material: 1h 33m 52s / 23.74 g total, including supports and
  the priming tower; sliced model material alone was 9.25 g
- Timelapse: Off

## Preflight

- [x] Exact designer profile and one intended object verified
- [x] Connected X2D selected and the project resliced for it
- [x] Printer, nozzle configuration, and physical plate checked
- [x] Object, support-base, and support-interface assignments verified
- [x] Slice preview and first-layer footprint inspected
- [x] Final mapping verified: AMS A2 main, external support auxiliary
- [x] Auto Bed Leveling, Flow Dynamics Calibration, and Nozzle Offset
  Calibration all explicitly Auto immediately before sending
- [x] User approved sending after receiving the completed preflight
- [x] Third-party files and private printer/account data omitted from Git

There was only one designer profile. This was a Studio print; final Handy cloud
slicing was not used or claimed to be verified.

## Outcome

The job was sent once after approval. Studio switched to the live Device view,
showed the holder thumbnail, active pause/stop controls, layer 0/212, and the
bed warming toward 55 °C. Its initial estimated finish time was 13:01 PST.

Completion, physical first-layer quality, support removal, pegboard fit, and
paddle fit have not yet been observed. No private camera photos are committed.

## Diagnosis and next change

The upstream profile had supports disabled. A MakerWorld commenter reported
problems printing the pegboard hooks, and the initial X2D slice independently
reported floating regions. Enabling supports removed that warning and produced
a `Slice ok` result. This establishes a corrected slice, not a successful
physical print. Keep this evidence with this model rather than treating the
support settings as universal defaults.

## Durable lesson

No general memory rule changed; this is a model-specific print attempt.
