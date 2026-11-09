# Spool-center desiccant holder

Two complete holders, each consisting of a container body and a screw lid,
printed together on one plate.

## Source and license

- Model: **Dessicant or weight Container for Bambu Lab Spool** by **Mono98**.
- Source: <https://makerworld.com/en/models/1090858-dessicant-or-weight-container-for-bambu-lab-spool#profileId-1084332>.
- Exact original profile: **0.20mm Standard @BBL X1C**, profile **1084332**.
- License: **Standard Digital File License**, displayed on the source page and
  embedded in the downloaded 3MF; checked **2026-11-08**. Consult the source
  page's license terms. Redistribution permission has not been established, so
  no upstream geometry or configured 3MF is committed here.
- This directory contains a settings-only reconstruction recipe. The modified
  project is retained locally at
  `.local/models/spool-desiccant-holder/two-red-spool-holders-x2d.3mf`.
- Application: **Bambu Studio 2.9.1.70**, with BBL configuration **2.9.0.75**.

## Configuration and local modifications

1. Open the original profile and adapt its settings to **Bambu Lab X2D**,
   **0.4 mm** nozzles, **Textured PEI Plate**.
2. Duplicate both original parts once, producing two bodies and two lids.
   Retain the original orientation, with each perforated flange against the
   plate. Do not scale or modify the meshes.
3. Arrange the four parts in two rows. The saved project uses approximate
   centers X=88 mm for lids and X=168 mm for bodies, with rows at Y=88 mm and
   Y=176 mm. Verify spacing after any subsequent import or arrangement.
4. Assign every part to **red Bambu PLA Matte**, using the main nozzle. For the
   observed print, project filament 3 mapped to **AMS A3**; verify the current
   inventory again before reusing that mapping.
5. Use **0.20mm Standard @BBL X2D**, 0.20 mm first layer, two walls,
   15% grid infill, no supports, automatic brim, and print **by layer**.
   The saved PLA Matte profile specifies 220 °C nozzle and 55 °C textured
   plate temperatures. No additional speed or flow overrides were introduced.
6. Inspect the first several sliced layers and final material mapping. Set
   every available calibration control to **Auto** before sending.

The original X1C profile was adapted for X2D; this is not an unchanged reprint
of a historical job. Jubi confirmed the model visually in MakerWorld.

## Observed attempt

The [2026-11-08 print](../../prints/2026-11-08-two-red-spool-desiccant-holders.md)
was sent successfully. Studio estimated **5h19m13s**, **91.66 g**, and
**28.87 m** for the full plate. Completion and fit have not been observed.
