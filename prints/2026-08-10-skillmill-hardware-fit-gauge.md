# 2026-08-10 — Skillmill M4/M6 hardware-fit gauge

- Status: in progress
- Started: 2026-08-10 11:47 PDT
- Completed: pending
- Related issue: none

## Goal

Validate the purchased M4 and M6 hardware against the exact captive-locknut
pockets and bolt-clearance holes used by the revised Skillmill catch-all before
printing another clamp. Success means both locknut sizes seat with light finger
pressure, resist turning without splitting the gauge, and the M4 and M6 bolts
pass through their corresponding clearance holes.

## Source and provenance

- Creator: original model created for this repository
- Model URL: none; local original model
- Exact profile/profile ID:
  `models/skillmill-rail-catchall/exports/skillmill-hardware-fit-gauge-m4-m6.stl`
- License and date checked: original work; all rights reserved as of 2026-08-10
- Local files committed: parametric OpenSCAD source, documentation, and related
  exports under `models/skillmill-rail-catchall/`; this revised gauge export is
  currently present in the working tree
- Modifications from upstream: none; no upstream geometry used

## Hardware

- Printer: Bambu Lab X2D (`Panda Factory`)
- Nozzle size/type: 0.4 mm hardened-steel main nozzle; 0.4 mm auxiliary nozzle
  installed but unused
- Build plate: Textured PEI
- Plate preparation: user reported the machine prepped; the live camera showed
  an empty installed plate before submission

## Material routing

| Role | Filament/profile | Source slot/feed | Nozzle |
| --- | --- | --- | --- |
| Object | Grey Bambu PETG Basic | AMS A4 | Main 0.4 mm |
| Support base | none generated | n/a | n/a |
| Support interface | Bambu Support for PLA/PETG remained available externally but was not used | external/aux feed | Auxiliary unused |

## Profile and slice

- App and version: Bambu Studio `02.07.01.62`
- Layer height: 0.20 mm; sliced height was 65 layers for the 13 mm gauge
- Walls: 4
- Infill pattern/percentage: grid, 30%
- Supports: disabled; auxiliary-nozzle column remained empty in both the slice
  summary and final mapping
- Adhesion/brim: preset default; the preview showed one flat gauge with no
  support, prime tower, or other auxiliary structure
- Temperatures: system Bambu PETG Basic profile; the active startup showed a
  240 C main-nozzle target while loading filament and a 70 C bed target
- Speed/flow changes: none added for this fit gauge
- Estimated time/material: 26m55s / 11.01 g

## Preflight

- [x] Exact local M4/M6 hardware-fit gauge verified
- [x] Similar candidate profiles compared when their retained settings differ (not applicable; original local model)
- [x] Live compatibility with the selected X2D verified in Studio and by job acceptance
- [x] X2D, 0.4 mm main nozzle, and Textured PEI plate verified
- [x] Grey PETG object assignment and absence of generated support verified
- [x] Slice preview inspected at the full model and at an internal layer; holes remained open and the 30% infill was visible
- [x] Final mapping verified as PETG in AMS A4 through the main nozzle; auxiliary nozzle blank
- [x] Flat pocket-up orientation and first-layer footprint reviewed
- [x] No third-party model or profile is included

## Outcome

- Actual result: pending; X2D accepted the job and entered startup at 0%, layer
  0/65
- Dimensions/fit: pending hardware test
- Surface or structural defects: pending
- Photos: pending
- Print history or app evidence checked: final send dialog showed X2D,
  Textured PEI, PETG from AMS A4 on the main nozzle, and an empty auxiliary
  mapping; Device view then showed the named job active

## Diagnosis and next change

Pending the physical fit test. If a locknut will not seat, enlarge only its
corresponding pocket-across-flats parameter by 0.2 mm. If it spins freely,
reduce that parameter by 0.2 mm. Do not scale the entire gauge or clamp.

## Durable lesson

Pending. Keep any one-off hardware tolerance result in this print log unless it
establishes a reusable pocket-clearance rule.
