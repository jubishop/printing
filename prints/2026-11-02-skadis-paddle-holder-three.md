# 2026-11-02 — Three more SKÅDIS ping pong paddle holders

- Status: completed — Studio print history reports Success
- Started: sent 2026-11-02 16:42 PST; printer startup confirmed afterward
- Completed: confirmed in Studio history on 2026-11-04; exact finish time not recorded
- Related issue: none

## Goal

Print three additional white holders in one batch, bringing the total to four
including the [successful first holder](2026-11-02-skadis-paddle-holder.md).
Studio reports the batch completed successfully; physical fit remains unverified.

## Source and provenance

- Creator: PingPongMeister
- Source: [MakerWorld model 1741694, profile 1850928](https://makerworld.com/en/models/1741694-pingpong-paddle-holder#profileId-1850928)
- Exact source profile: `0.2mm layer, 2 walls, 15% infill`
- License: CC BY-NC-SA 4.0, checked 2026-11-02
- Starting artifact: [committed single-holder X2D project](../models/skadis-paddle-holder/README.md)
- Modifications for this run: cloned the holder twice and arranged all three
  on plate 1, retaining the validated upright orientation and active process
  settings. Saved the batch project locally; it is not committed.

## Hardware

- Printer: Bambu Lab X2D
- Nozzles: main and auxiliary, 0.4 mm hardened steel, standard flow; verified
  in the live Printer Parts dialog
- Build plate: Textured PEI, selected in Studio and visible in the camera
- Plate preparation: user confirmed the machine ready; camera showed an empty
  plate. Cleaning method was not recorded.

## Material routing

| Role | Filament/profile | Source slot/feed | Nozzle |
| --- | --- | --- | --- |
| Objects | White Bambu PLA Pure | AMS A2 | Main |
| Support bodies | Default/object PLA | AMS A2 | Main |
| Support interfaces | Bambu Support For PLA/PETG | External spool | Auxiliary |

Project filament 1 supplies the objects and support bodies; filament 5 supplies
interfaces. Final send mapping showed white PLA from A2 and auxiliary external
support material. Other synchronized filaments were unused.

## Profile and slice

- App: Bambu Studio 2.8.2.61
- Quantity: exactly three printable holders on one plate, confirmed in Studio
  and the saved project's build items
- Layer height: 0.2 mm; walls: 2; infill: 15% grid
- Supports: automatic tree, Tree Hybrid, 35-degree threshold
- Interfaces: zero top Z distance, zero spacing, rectilinear interlaced;
  50 mm/s for the active standard-flow nozzle variants
- Adhesion: automatic brim, configured width 5 mm; prime tower enabled
- Temperatures: synchronized material profiles; live startup showed bed
  target 55 °C and main-nozzle target 220 °C
- Speed/flow changes: none to the active recipe from the successful single
- Timelapse: Off
- Estimated time: 2h 41m; live Device view reported 2h 41m 6s
- Filament changes reported by the slicer: 64

| Material | Models | Supports | Prime tower | Total |
| --- | --- | --- | --- | --- |
| White PLA | 27.85 g | 8.45 g | 7.77 g | 44.08 g / 14.78 m |
| Dedicated support | 0 g | 1.76 g | 3.32 g | 5.07 g / 1.77 m |
| Total | 27.85 g | 10.21 g | 11.09 g | 49.15 g / 16.55 m |

Values are slicer estimates, with minor rounding differences between columns.
This is 22.07 g less than three times the earlier single-print estimate of
23.74 g; actual consumption has not been measured.

## Preflight

- [x] Committed starting project and exactly three printable objects verified
- [x] X2D, both nozzle configurations, and physical plate verified
- [x] Object, support-body, and support-interface assignments checked
- [x] Slice completed without warnings; first layer and first five layers
  inspected, including support footprints and prime tower
- [x] All three objects and tower fit inside the plate; adjacent support brim
  footprints touch in places, with no object collision warning
- [x] Final mapping verified: white PLA from AMS A2, external support auxiliary
- [x] Auto Bed Leveling, Flow Dynamics Calibration, and Nozzle Offset
  Calibration each explicitly Auto immediately before sending
- [x] User approved sending after the completed preflight and confirmed ready
- [x] No private camera images, account identifiers, or generated G-code added

## Outcome

Sent once through Studio. The Device view confirmed the three-holder thumbnail,
49.15 g job, active pause/stop controls, and layer 0/212. It displayed
`Changing filament` and `Filament loading...`, with an initial estimated finish
time of 19:25 PST.

On 2026-11-04, Studio's print history showed the matching 2026-11-02 16:42
holder job with a duration of 2.7h and status `Success`. This confirms reported
job completion. Physical fit, support-removal quality, defects, and actual
material consumption were not separately assessed.

## Diagnosis and next change

No startup fault was displayed, and Studio subsequently reported success.
No further process change is indicated by those observations.

## Durable lesson

The [single-holder case](../memory/cases/2026-11-02-skadis-paddle-holder.md)
remains the result with user-confirmed paddle fit. The three-copy slice
demonstrates reduced estimated total material per holder, and Studio reports
successful completion. This batch's physical fit has not been confirmed.
