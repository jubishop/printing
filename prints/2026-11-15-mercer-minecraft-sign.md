# 2026-11-15 — Mercer Minecraft sign

- Status: in progress
- Started: 2026-11-15 23:56 PST
- Completed: not observed

## Goal

Print one Minecraft-style MERCER sign with raised green letters on a black
backing. The model measures approximately 165 × 46 × 14 mm.

## Source and provenance

- Creator: Canale (MakeronFabus).
- Model: [Minecraft Name Personalized](https://makerworld.com/en/models/1730058-minecraft-name-personalized#profileId-1837530).
- Exact source profile: `0.2mm layer, 2 walls, 15% infill`, profile 1837530,
  one plate. MakerWorld listed it under X2D.
- License: Standard Digital File License, checked 2026-11-15. Jubi approved
  the MakerWorld export for this personal print.
- Entered `Mercer` in the designer's Parametric Model Maker file, which
  rendered the name in uppercase with the default geometry and colors.
  Exported a new 3MF targeting X2D and sliced the custom plate in Studio.
- Local project: `.local/models/mercer/mercer-x2d.3mf`. No model archives
  or generated G-code were committed.

## Hardware

- Printer: Bambu Lab X2D, Panda Factory.
- Nozzles: main and auxiliary 0.4 mm hardened steel, Standard flow, verified
  in Printer Parts. The job uses the main nozzle.
- Build plate: Textured PEI in Studio and on the live camera. The camera showed
  the plate clear of parts, with faint rectangular outlines.

## Material routing

| Role | Filament/profile | Source slot/feed | Nozzle |
| --- | --- | --- | --- |
| Backing | Bambu PLA Pure, Absolute Black | AMS A1 | Main |
| Raised lettering | Bambu PLA Matte, Grass Green | AMS A4 | Main |
| Supports | None | None | None |

Studio synchronized project filaments 1 and 2 to the loaded spools. Convenience
Mode in Filament Grouping put both colors on the AMS-fed main nozzle. The send
dialog confirmed A1 and A4 and reported one extra purge compared with the
two-nozzle grouping.

## Profile and slice

- Bambu Studio 2.9.1.70, `0.20mm Standard @BBL X2D`, 70 layers on plate 1.
- 0.2 mm layers, including the first layer. Two walls and 15% grid infill.
- Supports disabled in the active project. Automatic brim and prime tower
  enabled. Layer 1 showed a broad continuous backing and a separate tower footprint.
- Active filament presets specified a 220 °C nozzle and 55 °C textured plate
  for both materials.
- Estimate: 1h 20m and 41.05 g total.

## Preflight

- [x] Verified the selected source profile, custom spelling, and single plate
- [x] Verified the connected X2D, installed nozzles, and physical plate
- [x] Verified live filament presets and final main-nozzle mapping
- [x] Inspected the full slice and first layer
- [x] Verified Auto Bed Leveling, Flow Dynamics Calibration, and Nozzle
  Offset Calibration all set to Auto immediately before sending
- [x] Received Jubi's approval to send after preflight

Nozzle Offset Calibration initially showed Off and was set to Auto. The other
two calibration controls already showed Auto. Timelapse was off.

## Outcome

Sent once. The Device page showed `mercer-x2d_Plate 1` at layer 0/70 in
**Homing toolhead**, with an estimated finish of 01:16 PST on November 16.
Job acceptance and startup were verified. Completion and finish quality remain
unverified.
