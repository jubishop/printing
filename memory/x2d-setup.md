---
name: x2d-setup
description: Stable Bambu Lab X2D hardware capabilities and verification boundaries
type: user
---

# X2D setup

Jubi uses Bambu Studio and Bambu Handy with a Bambu Lab X2D and 0.4 mm
hardened-steel nozzles.

The left/main nozzle can draw object filament from the AMS. The right/auxiliary
nozzle can use an external spool. One verified job used Bambu PETG Basic from
AMS A4 through the main nozzle and Bambu Support for PLA/PETG from the external
feed through the auxiliary nozzle, but that routing is a case history rather
than a standing default.

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

Jubi wants hands-on Computer Use help for consequential Bambu Studio setup and a
complete verification pass before a print is sent. See [[makerworld-workflow]].
