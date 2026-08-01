---
name: case-2026-07-31-skadis-tool-holder
description: IKEA SKADIS profile comparison showing cross-printer Handy conversion and retained process differences
type: reference
---

# 2026-07-31: IKEA SKADIS tool-holder preflight

This records a profile inspection and workflow decision; no completed print
outcome was captured.

## Source

- Model: [IKEA SKADIS TOOL HOLDER](https://makerworld.com/en/models/149809-ikea-skadis-tool-holder)
- Creator: Gr3dstampaidee
- Compared designer profiles:
  - [Profile 164983](https://makerworld.com/en/models/149809-ikea-skadis-tool-holder#profileId-164983), authored for A1 mini
  - [Profile 163446](https://makerworld.com/en/models/149809-ikea-skadis-tool-holder#profileId-163446), authored for X1/P1
- License observed on 2026-07-31: MakerWorld Standard Digital File License
- Repository decision: record provenance and settings only; do not commit the
  downloaded model/profile under that license.

## What the files established

The two designer cards had the same `0.16mm layer, 2 walls, 30% infill` title
and visually similar prepared layouts. The wording made it plausible that only
one was support-free, but the actual 3MF files settled the question:

- Both contained the holder and two separate T-clips in the same orientation.
- Both had `enable_support = 0`, `support_filament = 0`, and
  `support_interface_filament = 0`.
- Both used 0.16 mm layers, 2 walls, 30% grid infill, and a 5 mm automatic brim
  with a 0.1 mm object gap.

The main retained process differences were:

| Setting | Profile 164983, A1 mini source | Profile 163446, X1/P1 source |
| --- | --- | --- |
| Fully unsupported overhang speed | 19 mm/s | 50 mm/s |
| Default acceleration | 6000 mm/s² | 10000 mm/s² |
| Elephant-foot compensation | 0 mm | 0.15 mm |
| Original estimate | about 1.2 hours | about 56 minutes |

These are two support-free recipes, not supported and unsupported variants.
The slower profile is more conservative at fully unsupported overhangs; the
faster profile includes elephant-foot compensation and substantially reduces
the estimate.

## What the live X2D view established

After X2D was selected on MakerWorld, both profiles remained available. The
X1/P1 profile's estimate changed from about 56 minutes to about 51 minutes,
showing that MakerWorld was presenting an X2D-adapted cloud-slicing path rather
than requiring the embedded X1 G-code to be sent unchanged.

Downloading profile 164983 while the X2D filter was active produced the same
3MF bytes as the original A1-mini download. The downloaded file therefore
describes the uploader's source machine and retained process settings; it is
not an export of the final X2D cloud slice.

## Decision and correction

Both profiles were valid Handy choices for the X2D. The source printer name was
not a reason, by itself, to require Studio. The corrected recommendation was:

- For ordinary PLA, prefer profile 163446 for its substantially shorter time
  and strong print history.
- Prefer profile 164983 when conservative fully unsupported-overhang behavior
  matters more than time, including as a reasonable starting preference for
  fussier materials such as PETG.
- Use Studio only if changing the recipe, inspecting a custom slice, or
  resolving a compatibility warning.

This material-specific recommendation is case evidence, not a general rule that
all A1-mini profiles are safer or all X1 profiles are faster.

## Reusable guidance

- A profile's live X2D eligibility in MakerWorld/Handy is stronger workflow
  evidence than the source-printer field in its downloaded 3MF.
- Cloud compatibility does not erase retained process differences. Compare the
  settings that explain differing estimates before choosing between otherwise
  similar profiles.
- Identical profile titles and thumbnails cannot settle support state. Inspect
  actual global and object-level support settings when the wording is unclear.
- A downloaded 3MF proves the source geometry and settings, not the exact final
  cloud-generated X2D G-code.
