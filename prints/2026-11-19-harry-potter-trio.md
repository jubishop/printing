# 2026-11-19 — Harry Potter trio in Pure White

- Status: completed, 660 of 660 layers.
- Started: 2026-11-19 Pacific time. Studio showed completion on 2026-11-20.

## Goal

Print one Harry, one Hermione, and one Ron in Pure White on a single plate.

## Source and license

All three models are by **Badboyturnz**. Each source profile specifies
0.12 mm layers, two walls, 15% infill, and automatic tree supports.

| Model | MakerWorld profile |
| --- | --- |
| Mini Harry Potter | [2172589](https://makerworld.com/en/models/2016309-mini-harry-potter#profileId-2172589) |
| Mini Hermione Granger | [2934454](https://makerworld.com/en/models/2653985-mini-hermione-granger#profileId-2934454) |
| Mini Ron Weasley | [2934404](https://makerworld.com/en/models/2653949-mini-ron-weasley#profileId-2934404) |

The downloaded 3MFs identify all three licenses as the **Standard Digital
File License**, verified on 2026-11-20. The
[MakerWorld license terms](https://makerworld.com/en/exclusive-model-policy)
restrict distribution of the source models and modified projects. The
combined project stays in the ignored local models folder at
`.local/models/harry-potter-trio/Harry-Potter-Trio-X2D-Pure-White.3mf`.

## Hardware and material

- Bambu Lab X2D, 0.4 mm hardened-steel main nozzle, Textured PEI plate.
- Bambu Studio 2.9.1.70 adapted Hermione's P2S profile for the X2D. The
  three models retained their source scale and upright orientation.
- Bambu PLA Pure in Pure White fed the figures, support bases, and support
  interfaces through the main nozzle. A3 was the starting AMS slot and
  Studio showed A4 in its Auto-refill group. Whether the printer switched
  spools during the job was unverified.

## Slice and preflight

- Plate 1, one instance of each figure, printing by layer.
- 0.12 mm layers, 0.20 mm first layer, two walls, and 15% gyroid infill.
- Automatic tree supports at 20 degrees with 0.12 mm top and bottom
  Z gaps, two top interface layers, and 0.50 mm interface spacing.
- Automatic brim with a configured 5 mm width.
- The slice showed all three footprints and supports on one plate and
  assigned the entire job to the white filament on the main nozzle.
- Bed leveling, flow dynamics, and nozzle offset calibration all showed
  Auto immediately before sending.
- Studio listed 8h 1m 19s and 71.52 g for the completed job.

## Outcome and next change

Studio showed the plate completed. Justin reported that the supports were
very hard to remove. The figures and support interfaces used the same
PLA. For the next attempt, use Bambu Support For PLA/PETG for the contact
layers and keep Pure White PLA for the figures and tree branches. Justin
also requested 50% scale for the next attempt, so that print will change
both scale and support interface material.
