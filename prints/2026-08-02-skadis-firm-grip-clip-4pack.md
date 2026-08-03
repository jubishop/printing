# 2026-08-02 — SKÅDIS Firm-Grip Clip four-pack

- Status: failed
- Started: 2026-08-02 23:14 PDT
- Completed: 2026-08-03 08:49 PDT (canceled)
- Related issue: none

## Goal

Print the single-color four-pack from plate 2 in PETG, using the dedicated
PLA/PETG support material only for the support interfaces. Success means four
complete clips with cleanly removable supports and functional spring action.

## Source and provenance

- Creator: Henryk
- Model URL: https://makerworld.com/en/models/1371666-skadis-firm-grip-clip#profileId-1418278
- Exact profile/profile ID: `Single-Color Version`, profile `1418278`, plate 2
- License and date checked: `Standard Digital File License`, observed in the downloaded 3MF on 2026-08-02
- Local files committed: settings-only X2D process preset and provenance under `models/skadis-firm-grip-clip/`; no model geometry
- Modifications from upstream: converted the H2D project to X2D; selected Textured PEI Plate and Bambu PETG Basic; retained the four-pack geometry, 0.20 mm layer height, 3 walls, 30% gyroid, and manual support enforcers; routed dedicated support material to interfaces only
- Local configured project: `.local/models/skadis-firm-grip-clip/skadis_firm_grip_clip_x2d_4pack_ready.3mf` (ignored by Git; SHA-256 `d7ae0d6d40fa3a62d9eff1fb1c9252dd10a901a1a1f938a59f31875002479271`)

## Hardware

- Printer: Bambu Lab X2D
- Nozzle size/type: 0.4 mm hardened-steel main and auxiliary nozzles
- Build plate: Textured PEI Plate
- Plate preparation: user confirmed the printer was prepared; installed textured PEI plate was verified in the live camera before startup

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
- Adhesion/brim: upstream plate arrangement retained; clean slice had no first-layer path-conflict warning
- Temperatures: system Bambu PETG Basic and Support for PLA/PETG profiles; no temperature overrides added
- Speed/flow changes: support interface speed 50 mm/s; no other user speed or flow overrides added
- Estimated time/material: 2h19m, 47.75 g

## Preflight

- [x] Exact model profile and intended plates verified
- [x] Similar candidate profiles compared when their retained settings differ (exact single-color profile retained)
- [x] Live compatibility with the selected printer verified in Studio and by successful X2D job acceptance
- [x] Printer, nozzle, and physical build plate verified
- [x] Object/support material assignments verified
- [x] Slice preview inspected when using Studio
- [x] Final filament/nozzle mapping verified
- [x] First-layer and collision/adhesion risks considered
- [x] Third-party files omitted or redistribution permission recorded

## Outcome

- Actual result: failed; the user reported a stringy/spaghetti result and
  canceled the job. No usable four-pack was produced.
- Dimensions/fit: not evaluated
- Surface or structural defects: stringy/spaghetti extrusion; the failed
  pieces have not yet been photographed closely enough to identify which
  object or support feature detached first
- Photos: no failure photo recorded yet; the live camera showed an empty
  textured PEI plate after cleanup at approximately 08:57 PDT
- Print history or app evidence checked: Bambu Studio recorded `Canceled`,
  plate 2, Textured PEI Plate, 2026-08-02 23:14 through 2026-08-03 08:49,
  47.13 g PETG through the left nozzle, and 0.62 g `Sup.PLA` through the right
  external feed. The 47.75 g total matches the preflight material estimate.

## Diagnosis and next change

An initial tree-support slice reported conflicting first-layer paths. Restoring
the profile's normal/manual supports and automatic first-layer support
expansion produced a clean slice while retaining the dedicated zero-gap
support interface.

The dedicated material routing did operate: print history recorded material
through both the PETG main nozzle and the external support-material auxiliary
nozzle. The full estimated material was consumed despite the stringy result,
which is more consistent with a part or support losing adhesion while the
printer continued extruding than with a simple mapping failure. The 9.6-hour
history duration is much longer than the 2h19m slice estimate and may include
time spent faulted or awaiting cancellation; it is not evidence that normal
toolpaths ran for 9.6 hours.

Do not rerun this profile unchanged or publish its MakerWorld draft. Inspect a
close photo of the failed pieces first to distinguish object-to-plate,
support-to-plate, and support-interface failure before choosing the next
adhesion or support change.

## Durable lesson

Correct nozzle and filament routing is necessary but does not establish that a
support-heavy PETG plate is mechanically reliable. For a new profile, verify an
early layer and prefer a smaller validation print before committing to a
four-pack; record exactly which object or support feature detached if it fails.
