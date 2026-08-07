# SKÅDIS Firm-Grip Clip — X2D PETG recipe

This directory preserves the settings-only portion of the X2D PETG project.
It deliberately does not contain the upstream or modified model geometry.

> [!IMPORTANT]
> The PETG Basic retry completed successfully on 2026-08-07 using 80 mm/s top
> surfaces and 120 mm/s internal solid infill. Use the
> [`validated` process preset](skadis-firm-grip-clip-x2d-petg-basic-validated.process.json).
> Physical validation currently covers plate 1, one complete clip.

> [!WARNING]
> The legacy [`four-pack` process preset](skadis-firm-grip-clip-x2d.process.json)
> retains the fast 200/250 mm/s inherited top/solid settings from the failed
> 2026-08-03 attempt. It is kept as failure evidence and must not be printed or
> published unchanged. See the [failed print record](../../prints/2026-08-02-skadis-firm-grip-clip-4pack.md).

## Provenance and license

- Model: `SKÅDIS Firm-Grip Clip`
- Creator/profile uploader: Henryk
- Source: https://makerworld.com/en/models/1371666-skadis-firm-grip-clip#profileId-1418278
- Exact profile: `Single-Color Version`, profile `1418278`; plate 1 is the
  successful validation and plate 2 is the failed fast-baseline attempt
- Upstream license: MakerWorld `Standard Digital File License`
- License checked: 2026-08-02, from the metadata embedded in the downloaded 3MF
- Bambu Studio used: `02.07.01.62`

MakerWorld's Standard Digital File License prohibits hosting or redistributing
the digital object and derivatives. The configured 3MF files therefore remain
only in the ignored local artifact tree:

```text
.local/models/skadis-firm-grip-clip/skadis_firm_grip_clip_x2d_4pack_ready.3mf
.local/models/skadis-firm-grip-clip/skadis_firm_grip_clip_x2d_single_retry_80_120.3mf
```

Their SHA-256 values are, respectively,
`d7ae0d6d40fa3a62d9eff1fb1c9252dd10a901a1a1f938a59f31875002479271` and
`da636c1a414ce83659efb751b1dec99043d7e6af9ab43ae124900c3e4b8bed87`.

## Reconstructing the project

1. Download the exact `Single-Color Version` profile from the source URL and
   open it in Bambu Studio.
2. Select `Bambu Lab X2D 0.4 nozzle` and `Textured PEI Plate`. Use plate 1 for
   the physically validated single clip. Plate 2 contains four clips but has
   not yet been validated with the corrected speeds.
3. Use `Bambu PETG Basic` as project filament 1. Add `Bambu Support For
   PLA/PETG` as project filament 2.
4. Import [`skadis-firm-grip-clip-x2d-petg-basic-validated.process.json`](skadis-firm-grip-clip-x2d-petg-basic-validated.process.json)
   with **File → Import → Import Configs**, then select the imported validated
   process preset.
5. Verify that support base is `Default` (PETG), support interface is filament
   2, **Avoid interface filament for support base** is enabled, and the prime
   tower is present.
6. Slice the selected plate and verify the final grouping and printer mapping:

   - Main nozzle: PETG from AMS A4.
   - Auxiliary/right nozzle: Support for PLA/PETG from the external feed.

The successful 2026-08-07 plate 1 slice estimated 43m11s / 13.07 g. Generated
G-code confirmed 80 mm/s top-surface and 120 mm/s internal-solid paths through
the earlier Z=10.8–11.0 mm failure band. See the
[successful print record](../../prints/2026-08-07-skadis-firm-grip-clip-single-validation.md).

## MakerWorld publication path

The geometry is unchanged, so this is not a model remix. The revised profile
has now completed successfully, but MakerWorld still requires a real photo of
the printed result. Keep the current contribution as an unpublished draft
until that photo is available. Then publish it as a new X2D print profile
attached to Henryk's existing model, explaining that PETG prints the objects
and support bodies while the external auxiliary feed is used only for the
support interface.
