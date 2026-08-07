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

- Actual result: the printer's AI detection stopped the job at 88% progress;
  the user then canceled it. Every object remained attached to the plate and
  looked generally good below the stopped layer, but no complete four-pack was
  produced.
- Dimensions/fit: not evaluated
- Surface or structural defects: strands projected from the top of nearly all
  pieces at the same Z height. There was no object-to-plate or support-to-plate
  detachment.
- Photos: no failure photo recorded yet; the live camera showed an empty
  textured PEI plate after cleanup at approximately 08:57 PDT
- Print history or app evidence checked: Bambu Studio recorded `Canceled`,
  plate 2, Textured PEI Plate, 2026-08-02 23:14 through 2026-08-03 08:49,
  47.13 g PETG through the left nozzle, and 0.62 g `Sup.PLA` through the right
  external feed. Those displayed amounts match the slice estimate and must not
  be treated as metered consumption from a job stopped at 88%.

## Diagnosis and next change

An initial tree-support slice reported conflicting first-layer paths. Restoring
the profile's normal/manual supports and automatic first-layer support
expansion produced a clean slice while retaining the dedicated zero-gap
support interface.

The dedicated material routing did operate: print history recorded PETG on the
main nozzle and support material on the external auxiliary nozzle. Reslicing
the retained project and inspecting its G-code mapped 88% progress to
Z=10.8-11.0 mm, layers 54-55 of 65. At this transition every repeated copy is
performing top-surface or internal-solid work. Top surfaces are configured at
200 mm/s and internal solid infill at 250 mm/s; the generated top-surface path
runs at approximately 199 mm/s. The support-interface toolpaths ended much
earlier, at Z=4.2 mm, so dedicated support material was not active at the
failure layer.

The upstream H2D profile was authored for Bambu PETG HF with a 25 mm^3/s
maximum volumetric speed. This attempt substituted Bambu PETG Basic, whose
embedded X2D profile uses 15 mm^3/s, while retaining the fast process speeds.
The repeated same-height strands, intact adhesion, and otherwise clean lower
layers therefore point to an overly aggressive high-flow solid/top transition
for PETG Basic, potentially compounded by travel ooze, rather than an adhesion
or support-interface failure.

The 9.6-hour history duration is much longer than the 2h19m slice estimate
because the AI-stopped job remained pending until morning cancellation; it is
not evidence that normal toolpaths ran for 9.6 hours.

Do not rerun this profile unchanged or publish its MakerWorld draft. The next
controlled validation should use one set rather than the four-pack, retain the
working support routing, reduce top-surface and internal-solid speeds, and
inspect the Z=10.8-11.0 mm preview before another physical print. Keep AI
detection enabled.

That follow-up completed successfully on 2026-08-07 with one clip, 80 mm/s top
surfaces, and 120 mm/s internal solid infill. See the
[successful validation record](2026-08-07-skadis-firm-grip-clip-single-validation.md).

## Durable lesson

When substituting PETG Basic for a profile authored around PETG HF, verify
high-flow top and solid layers as well as material mapping. A good first layer
and correct support routing do not validate later process transitions; test one
copy before committing to a repeated plate.
