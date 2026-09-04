# 2026-09-04 — Climbing pegboard shelf

- Status: in progress
- Started: 2026-09-04 at 12:21 PDT
- Completed: pending
- Related issue: none

## Goal

Print the final temporary shelf that uses the two proven pegboard holes. Success
requires both pegs to seat without force, the flat rear face to bear against the
wood, and the shelf to support no more than 2 lb of stationary objects after a
cautious physical load test.

This is not climbing equipment. Remove it before anyone uses the pegboard.

## Source and provenance

- Creator: Jubi, with OpenAI Codex modeling assistance
- Model URL: none; original local design
- Exact profile/profile ID: local OpenSCAD model, `part="shelf"`
- License and date checked: all rights reserved; 2026-09-04
- Local files committed: shared source, STL, renders, and model README; this
  attempt record is initially uncommitted
- Modifications from upstream: not applicable
- Tool: OpenSCAD 2021.01
- Private 3MF: `.local/models/climbing-pegboard-shelf/pegboard-shelf-220p5x100-lip12mm-pla.3mf`

## Hardware

- Printer: Bambu Lab X2D
- Nozzle size/type: main and auxiliary 0.4 mm; hardened steel is the recorded
  hardware baseline
- Build plate: Bambu Textured PEI Plate
- Plate preparation: user confirmed the machine was prepared; the live Device
  camera showed the textured plate installed and clear before sending

## Material routing

| Role | Filament/profile | Source slot/feed | Nozzle |
| --- | --- | --- | --- |
| Object | Bambu PLA Pure, white | AMS A3 | Main, 0.4 mm |
| Support base | Bambu PLA Pure, inherited from object | AMS A3 | Main, 0.4 mm |
| Support interface | Bambu Support For PLA/PETG | External auxiliary feed | Auxiliary, 0.4 mm |

The support filament is non-soluble. Studio warned against using it for the
whole support base, so the tree bodies remain in PLA and the dedicated material
is used only for the two dense contact-interface layers. `Avoid interface
filament for base` was enabled.

## Profile and slice

- App and version: Bambu Studio 02.08.02.61
- Process: `0.20mm Standard @BBL X2D`
- Layer height: 0.20 mm, including the initial layer; 270 layers
- Walls: 3
- Infill pattern/percentage: grid, 20%
- Supports: tree auto, Tree Hybrid; 35 degree threshold; support base in PLA;
  interface in Bambu Support For PLA/PETG; 2 top interface layers; 0 mm top Z
  distance and 0 mm interface spacing; 5 mm initial support-layer expansion;
  3 mm tree branch diameter and 7 degree diameter angle; remove small
  overhangs enabled
- Adhesion/brim: auto brim, 5 mm width, 0.1 mm object gap
- Prime tower: enabled for the dual-nozzle print
- Temperatures: object PLA profile 220 C; support profile 210 C; live startup
  readback showed a 55 C bed target
- Speed/flow changes: none beyond the support-material recommendation; support
  interface speeds were set to Bambu's 50 mm/s recommendation
- Estimated time/material: 5 hours 27 minutes 14 seconds; 181.05 g total;
  60.75 m

## Preflight

- [x] Exact final STL and intended shelf geometry verified
- [x] Original model provenance recorded; no third-party model included
- [x] X2D selected with main and auxiliary 0.4 mm nozzles
- [x] Textured PEI plate selected in the project and confirmed by live camera
- [x] Object and support-base PLA assigned to main nozzle from AMS A3
- [x] Support-interface material assigned to auxiliary nozzle from external feed
- [x] Full dual-nozzle slice inspected, including the two supported peg tubes
  and prime tower
- [x] Final send dialog showed main `PLA / A3` and auxiliary `Sup.PLA / Ext`
- [x] Auto Bed Leveling explicitly `Auto` immediately before send
- [x] Flow Dynamics Calibration explicitly `Auto` immediately before send
- [x] Nozzle Offset Calibration explicitly `Auto` immediately before send
- [x] User explicitly authorized sending after preparing the machine

The first send dialog opened with Nozzle Offset Calibration set to `Off`. It
was changed to `Auto`. Before the job was sent, the user noted that dedicated
support material remained in the auxiliary extruder. The single-nozzle send
was canceled, the interface was assigned to filament 5, the project was
resliced, and the entire final preflight was repeated. Timelapse remained
`Off`.

Bambu Studio sent the corrected job at 12:21 PDT. Independent Device-page
readback showed the exact shelf job active at 0/270 layers and `Homing
toolhead`, with an initial estimated finish of 17:48 PDT.

## Outcome

- Actual result: in progress
- Dimensions/fit: pending
- Surface or structural defects: pending
- Photos: none stored
- Print history or app evidence checked: prepared project, full dual-nozzle
  preview, final live mapping and calibration dialog, and active Device-page
  job

## Diagnosis and next change

Wait for completion. Then inspect the supported lower surfaces of both pegs,
confirm that both pegs still enter together without force, and perform a
cautious load test before using the shelf for ordinary objects.

## Durable lesson

No new reusable rule yet. Record the completed fit and load-test result here.
