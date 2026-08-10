# 2026-08-09 — Skillmill PLA clamp screws

- Status: failed (thread engagement; print quality successful)
- Started: 2026-08-09 20:00 PDT
- Completed: by 2026-08-09 21:34 PDT
- Related issue: none

## Goal

Print two copies of the coarse printed latch screw for the Skillmill fit-test
clamp. Success means both screws print cleanly, thread through the PETG lower
saddle without cross-threading or binding, and withstand normal hand tightening
without twisting or fracturing. The second screw is a spare and a consistency
check.

## Source and provenance

- Creator: original work created for this repository
- Model URL: none; local original model
- Exact profile/profile ID: `.local/models/skillmill-fit-test-40mm-two-plate.3mf`, plate 2 `PLA screws`
- License and date checked: all rights reserved; provenance reviewed 2026-08-09
- Local files committed: source and exported STL are already tracked; the machine-specific 3MF remains ignored
- Modifications from upstream: none; no upstream geometry is used

## Hardware

- Printer: Bambu Lab X2D (`Panda Factory`)
- Nozzle size/type: 0.4 mm hardened-steel main nozzle; 0.4 mm auxiliary installed but unused
- Build plate: Textured PEI
- Plate preparation: user reported the machine prepped and ready; live camera showed an empty installed plate before startup

## Material routing

| Role | Filament/profile | Source slot/feed | Nozzle |
| --- | --- | --- | --- |
| Object | Black Bambu PLA Basic | AMS A2 | Main 0.4 mm |
| Support base | none generated | n/a | n/a |
| Support interface | Bambu Support for PLA/PETG remained available in the external/aux feed but was not used | external/aux feed | Auxiliary unused |

## Profile and slice

- App and version: Bambu Studio 2.7.1.62
- Layer height: 0.16 mm
- Walls: 6
- Infill pattern/percentage: rectilinear, 100%
- Supports: none generated for the screws
- Adhesion/brim: auto brim, 5 mm configured width with 0.1 mm object gap
- Temperatures: Bambu PLA Basic profile defaults; no print-specific override
- Speed/flow changes: 40 mm/s outer wall; no additional print-time override
- Estimated time/material: 44m31s / 13.36 g for two screws

## Preflight

- [x] Exact local model, plate 2, and quantity of two screws verified
- [x] Similar candidate profiles compared when their retained settings differ (not applicable; original local model)
- [x] Live compatibility with the selected printer verified in Bambu Studio
- [x] Bambu Lab X2D, 0.4 mm nozzles, and Textured PEI plate verified
- [x] Black PLA object routing and absence of generated support verified
- [x] Slice preview inspected in Studio; two vertical screws, 237 layers
- [x] Final mapping verified as black PLA in AMS A2 on the main nozzle; auxiliary nozzle blank
- [x] Vertical knob-down orientation and auto brim reviewed for first-layer stability
- [x] No third-party model or profile is included

## Outcome

- Actual result: both screws completed, but the user reported that a screw
  slides directly through the PETG female thread without catching
- Dimensions/fit: failed; the printed male thread is too small relative to the
  printed female thread to create usable engagement
- Surface or structural defects: none reported on the screws themselves
- Photos: pending
- Print history or app evidence checked: Bambu Studio reported `Successfully sent` at 100%, then Device view showed the named job active with a 20:44 PDT estimated finish

## Diagnosis and next change

An initial job was submitted at about 19:51 PDT using the saved project's 30%
grid infill. Inspection immediately after submission found that this did not
match the model's 100% screw specification. The printer was stopped and the job
was canceled at layer 0 before deposition. The corrected slice uses 100%
rectilinear infill and was then resent.

The thread was nominally 12 mm x 3 mm pitch, but the modeled male major diameter
was reduced to `12.0 * 0.94 = 11.28 mm`. The female cutter was enlarged to
`12.0 + 2 * 0.40 = 12.80 mm`; with 1.2 mm thread depth, its inward crest was
10.40 mm diameter. That left only `(11.28 - 10.40) / 2 = 0.44 mm` of ideal
radial engagement. Ordinary FDM rounding and dimensional variation across the
PETG female and PLA male threads were enough to erase it.

The design has been changed to a manufactured M8 or 5/16 inch through-bolt,
top washer, and standard hex nut captured in the lower lug. The printed screw
export was retired rather than enlarged because metal hardware removes the
thread-tolerance failure mode and provides a safer, replaceable latch.

## Durable lesson

For functional parts, verify both effective slicer strength settings and the
modeled mating clearances. A fully solid, clean print cannot compensate for
insufficient geometric thread engagement. Bambu Studio also cannot use grid at
100% density and must switch the pattern to rectilinear for a fully solid slice.
