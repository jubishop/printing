# SKÅDIS Firm-Grip Clip — X2D four-pack recipe

This directory preserves the settings-only portion of the X2D PETG four-pack
prepared on 2026-08-02. It deliberately does not contain the upstream or
modified model geometry.

## Provenance and license

- Model: `SKÅDIS Firm-Grip Clip`
- Creator/profile uploader: Henryk
- Source: https://makerworld.com/en/models/1371666-skadis-firm-grip-clip#profileId-1418278
- Exact profile: `Single-Color Version`, profile `1418278`, plate 2
- Upstream license: MakerWorld `Standard Digital File License`
- License checked: 2026-08-02, from the metadata embedded in the downloaded 3MF
- Bambu Studio used: `02.07.01.62`

MakerWorld's Standard Digital File License prohibits hosting or redistributing
the digital object and derivatives. The configured 3MF therefore remains only
in the ignored local artifact tree:

```text
.local/models/skadis-firm-grip-clip/skadis_firm_grip_clip_x2d_4pack_ready.3mf
```

Its SHA-256 is
`d7ae0d6d40fa3a62d9eff1fb1c9252dd10a901a1a1f938a59f31875002479271`.

## Reconstructing the project

1. Download the exact `Single-Color Version` profile from the source URL and
   open it in Bambu Studio.
2. Select `Bambu Lab X2D 0.4 nozzle`, `Textured PEI Plate`, and plate 2 (the
   twelve parts that form four complete clips).
3. Use `Bambu PETG Basic` as project filament 1. Add `Bambu Support For
   PLA/PETG` as project filament 2.
4. Import [`skadis-firm-grip-clip-x2d.process.json`](skadis-firm-grip-clip-x2d.process.json)
   with **File → Import → Import Configs**, then select the imported process
   preset.
5. Verify that support base is `Default` (PETG), support interface is filament
   2, **Avoid interface filament for support base** is enabled, and the prime
   tower is present.
6. Slice plate 2 and verify the final grouping and printer mapping:

   - Main nozzle: PETG from AMS A4.
   - Auxiliary/right nozzle: Support for PLA/PETG from the external feed.

The verified 2026-08-02 slice had no path-conflict warning and estimated
2h19m / 47.75 g. Treat those values as comparison evidence, since slicer and
filament-profile updates may change them.

## MakerWorld publication path

The geometry is unchanged, so this is not a model remix. After the physical
print has completed successfully, the appropriate MakerWorld contribution is a
new X2D print profile attached to Henryk's existing model. Include the actual
print result and explain that PETG prints the objects and support bodies while
the external auxiliary feed is used only for the support interface.
