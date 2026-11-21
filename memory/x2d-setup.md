---
name: x2d-setup
description: Stable Bambu Lab X2D hardware capabilities and verification boundaries
type: user
---

# X2D setup

Jubi uses Bambu Studio and Bambu Handy with a Bambu Lab X2D and 0.4 mm
hardened-steel nozzles.

The left/main nozzle can draw object filament from the AMS. The right/auxiliary
nozzle can use an external spool. The dedicated support filament is Bambu
Support For PLA/PETG on the external feed through the auxiliary nozzle, and
`AGENTS.md` has required it for the support interfaces of every supported
print since 2026-11-20, after the
[Harry Potter trio](../prints/2026-11-19-harry-potter-trio.md)'s same-PLA
interfaces proved very hard to remove. Object filament and AMS slots vary by
print.

Before every print, verify:

- The active printer and nozzle configuration.
- The installed build plate and the plate selected in the profile.
- Current AMS/external-spool inventory and material condition.
- Object, support-base, and support-interface material assignments.
- The mapping shown immediately before printing.

Do not treat an AMS slot recorded in an older print as current inventory. Do not
infer active material from an embedded `default_filament_profile` or similar
provenance field; confirm the project assignments, sliced preview, print
mapping, and print history.

Jubi wants hands-on desktop-app help for consequential Bambu Studio setup and a
complete verification pass before a print is sent. See [[makerworld-workflow]].
