---
name: skillmill-rail-measurement
description: Keep 40 mm provisional while using the physically validated 41.3 mm bore and installed liner.
type: feedback
---

# Skillmill rail measurement

Treat 40 mm as a provisional modeling input, not a verified rail diameter.

The 41.3 mm modeled bore with the installed 0.8 mm liner is physically
validated for this Skillmill rail. Keep 40 mm as a provisional modeling input,
not a verified bare-rail diameter.

**Why:** The only direct field measurement was an approximate 125 mm
circumference taken with a fabric tape on 2026-08-08. That converts to about
39.79 mm, but neither the tape result nor the rounded 40 mm value is exact. The
first lined clamp's known result is more useful: its 42.1 mm modeled bore still
slid slightly on the rail. The next revision reduced the modeled bore by 0.8 mm
to 41.3 mm. On 2026-08-10, the user reported that this revision fit the lined
rail perfectly.

**How to apply:** Keep the provisional input as a stable baseline while
iterating, and express any later revision as a direct bore-diameter adjustment
from a physically tested part. Use 41.3 mm as the validated finished-bore target
when the same liner is used. Do not describe a calculated liner preload or
exact rail diameter unless a later measurement establishes it.
