---
name: 2026-11-02-skadis-paddle-holder
description: Successful SKADIS paddle holder with X2D tree supports and auxiliary support interfaces
type: reference
---

# 2026-11-02: SKÅDIS paddle-holder validation

PingPongMeister's [Pingpong paddle holder, profile 1850928](https://makerworld.com/en/models/1741694-pingpong-paddle-holder#profileId-1850928)
works for the user's paddle with the supported X2D setup recorded in the
[print log](../../prints/2026-11-02-skadis-paddle-holder.md). On 2026-11-02,
the user confirmed the single print finished and holds their paddle. A custom
design is unnecessary for that tested use.

## What made this a Studio job

The source profile, `0.2mm layer, 2 walls, 15% infill`, had supports disabled.
Its initial X2D slice reported floating regions around the pegboard hooks.
Enabling automatic tree supports removed the warning; the subsequent physical
print succeeded. The unsupported version was not physically tested.

The working setup used white Bambu PLA Pure for the object and support bodies
through the main nozzle, with Bambu Support For PLA/PETG from the external
auxiliary feed assigned only to support interfaces. Studio's recommendations
for that pairing included zero top Z distance and zero interface spacing.
The print log retains the full observed settings and preflight.

## Reusable lesson and limits

- Reuse this existing model and the validated supported setup for the tested
  paddle; recheck current hardware, materials, routing, and sliced geometry.
- Inspect the exact profile's support state and floating hook regions. An
  auxiliary support spool being loaded does not assign it to interfaces.
  This case supports the routing guidance in [[makerworld-workflow]].
- Budget from the final slice: this run estimated 1h 33m 52s and 23.74 g total,
  versus 9.25 g for the model alone. Supports and priming materially affect a
  small print's cost; these are estimates, not measured consumption.
- Completion and paddle-holding function are user-confirmed. Support-removal
  quality, pegboard fit, long-term durability, and fit for other paddles were
  not separately established. Treat these settings as model-specific evidence.
