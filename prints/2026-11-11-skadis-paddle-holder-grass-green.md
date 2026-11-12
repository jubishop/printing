# 2026-11-11 — One Grass Green SKÅDIS paddle holder

- Status: in progress
- Started: 2026-11-11 20:00 PST
- Completed: not observed

## Goal

Print one more of the [validated paddle holder](2026-11-02-skadis-paddle-holder.md)
in Grass Green PLA Matte.

## Source and provenance

- Creator: PingPongMeister.
- Model: [Pingpong paddle holder](https://makerworld.com/en/models/1741694-pingpong-paddle-holder#profileId-1850928).
- Exact source profile: `0.2mm layer, 2 walls, 15% infill`, profile 1850928,
  plate 1.
- License: CC BY-NC-SA 4.0, checked 2026-11-02 and recorded with the
  [validated project](../models/skadis-paddle-holder/README.md).
- Starting project: the saved [Marine Blue repeat](2026-11-10-skadis-paddle-holder-marine-blue.md).
  The object retained its PLA Matte preset and changed to the live Grass Green
  spool's color. The geometry, placement, and support recipe were retained.
- Local project: `.local/models/skadis-paddle-holder/skadis-paddle-holder-one-grass-green-x2d.3mf`.
  No new model archive or generated G-code was committed.

## Hardware

- Printer: Bambu Lab X2D.
- Nozzles: main and auxiliary 0.4 mm hardened steel, Standard flow, verified
  in Printer Parts and the send dialog.
- Build plate: Textured PEI, verified in Studio and on the live camera. The
  camera showed no parts on the plate and four faint rectangular outlines.

## Material routing

| Role | Filament/profile | Source slot/feed | Nozzle |
| --- | --- | --- | --- |
| Object | Bambu PLA Matte, Grass Green | AMS A4 | Main |
| Support base | Object PLA Matte | AMS A4 | Main |
| Support interface | Bambu Support For PLA/PETG, Nature | External spool | Auxiliary |

Project filament 2 was assigned to the object and mapped to AMS A4 in the
send dialog. Filament 5 was mapped to the external support spool.

## Profile and slice

- Bambu Studio 2.9.1.70. One holder on plate 1, 212 layers.
- 0.2 mm layers, two walls, and 15% grid infill.
- Automatic Tree Hybrid supports at 35 degrees, with zero top Z distance and
  zero interface spacing.
- Automatic brim with 5 mm configured width. Prime tower enabled.
- Estimate: 1h 25m 10s and 25.04 g total (21.13 g green PLA and 3.91 g
  support material, including the prime tower). The model itself used an
  estimated 10.11 g. Studio reported 64 filament changes.
- Device showed a startup bed target of 55 °C. Timelapse was off.

## Preflight

- [x] Verified the model, single holder, X2D, both nozzles, and textured plate
- [x] Verified live filament presets, project assignments, and final nozzle mapping
- [x] Inspected the full slice and early layers, including the first-layer
  footprint and clearance from the separate prime tower
- [x] Rechecked Auto Bed Leveling, Flow Dynamics Calibration, and Nozzle
  Offset Calibration were all set to Auto immediately before sending
- [x] Received Jubi's approval to send after preflight

## Outcome

Sent once. The Device page showed `skadis-paddle-holder-one-grass-green-x2d`
at layer 0/212 in **Cooling chamber**, with an estimated finish of 21:25 PST.
Job acceptance and startup were verified. Completion, fit, and finish were
not observed.
