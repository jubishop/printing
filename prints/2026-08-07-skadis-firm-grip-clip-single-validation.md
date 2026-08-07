# 2026-08-07 — SKÅDIS Firm-Grip Clip single validation

- Status: completed
- Started: 2026-08-07 08:27 PDT
- Completed: by 2026-08-07 09:38 PDT (exact time not recorded)
- Related issue: none

## Goal

Validate one complete clip before retrying the four-pack, preserving the
working PETG/support-material routing while reducing the high-flow top and
solid speeds implicated in the earlier failure. Success means a complete,
clean clip without the same-height strands seen in the four-pack attempt.

## Source and provenance

- Creator: Henryk
- Model URL: https://makerworld.com/en/models/1371666-skadis-firm-grip-clip#profileId-1418278
- Exact profile/profile ID: `Single-Color Version`, profile `1418278`, plate 1
- License and date checked: `Standard Digital File License`, observed in the downloaded 3MF on 2026-08-02
- Local files committed: settings-only validated X2D process preset and provenance; no model geometry
- Modifications from upstream: converted the H2D project to X2D; selected Textured PEI Plate, plate 1, and Bambu PETG Basic; retained 0.20 mm layers, 3 walls, 30% gyroid, manual supports, and dedicated support interface; reduced top surface from 200 to 80 mm/s and internal solid infill from 250 to 120 mm/s
- Local configured project: `.local/models/skadis-firm-grip-clip/skadis_firm_grip_clip_x2d_single_retry_80_120.3mf` (ignored by Git; SHA-256 `da636c1a414ce83659efb751b1dec99043d7e6af9ab43ae124900c3e4b8bed87`)

## Hardware

- Printer: Bambu Lab X2D
- Nozzle size/type: 0.4 mm hardened-steel main and auxiliary nozzles
- Build plate: Textured PEI Plate
- Plate preparation: user prepared the installed plate immediately before the print; exact cleaning method was not recorded

## Material routing

| Role | Filament/profile | Source slot/feed | Nozzle |
| --- | --- | --- | --- |
| Object | Bambu PETG Basic | AMS A4 | Main |
| Support base | Bambu PETG Basic | AMS A4 | Main |
| Support interface | Bambu Support for PLA/PETG | External feed | Auxiliary/right |

## Profile and slice

- App and version: Bambu Studio `02.07.01.62`
- Layer height: 0.20 mm
- Walls: 3
- Infill pattern/percentage: gyroid, 30%
- Supports: normal/manual; PETG base; dedicated interface material; 0 mm top Z distance; 0 mm interface spacing; rectilinear-interlaced interface; avoid interface filament for support base enabled; prime tower enabled
- Adhesion/brim: upstream plate 1 arrangement retained on Textured PEI; no slicing warning
- Temperatures: system Bambu PETG Basic and Support for PLA/PETG profiles; no temperature overrides added
- Speed/flow changes: top surface 80 mm/s; internal solid infill 120 mm/s; support interface 50 mm/s; generated G-code at Z=10.8 mm confirmed top paths at 80 mm/s and internal-solid paths at 120 mm/s
- Estimated time/material: 43m11s, 13.07 g total (12.83 g PETG and 0.24 g support material)

## Preflight

- [x] Exact model profile and intended plates verified
- [x] Similar candidate profiles compared when their retained settings differ
- [x] Live compatibility with the selected printer verified in Studio and by successful X2D job acceptance
- [x] Printer, nozzle, and physical build plate verified
- [x] Object/support material assignments verified
- [x] Slice preview inspected when using Studio
- [x] Final filament/nozzle mapping verified
- [x] First-layer and collision/adhesion risks considered
- [x] Third-party files omitted or redistribution permission recorded

## Outcome

- Actual result: completed; at 09:38 PDT the user reported that the one-clip print “came out great”
- Dimensions/fit: no measurements or SKÅDIS fit test recorded yet
- Surface or structural defects: none reported
- Photos: none recorded; a real result photo is still required before publishing the MakerWorld print profile
- Print history or app evidence checked: Bambu Studio accepted the one-clip job, showed 65 layers and a 43m11s estimate, and entered active printing at layer 0/65; successful completion and quality are based on the user's direct inspection

## Diagnosis and next change

The successful print supports the earlier diagnosis that the PETG HF-oriented
200/250 mm/s top/solid settings were too aggressive for PETG Basic. The
support routing and zero-gap dedicated interface were unchanged, while the
problematic G-code paths were reduced to 80/120 mm/s.

Use this process for future PETG Basic attempts. The single-clip plate is
physically validated; a four-pack using these settings should still be treated
as a separate scale-up validation rather than assumed successful.

## Durable lesson

For this model on X2D with PETG Basic, 80 mm/s top surfaces and 120 mm/s
internal solid infill completed the layer transition that failed at 200/250
mm/s. Preserve the dedicated support-interface routing and validate one clip
before scaling up the plate count. See the
[reusable case note](../memory/cases/2026-08-07-skadis-firm-grip-clip.md).
