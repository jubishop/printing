---
name: skillmill-rail-measurement
description: Treat 40 mm as a provisional Skillmill rail input and calibrate the clamp from physical fit tests.
type: feedback
---

# Skillmill rail measurement

Treat 40 mm as a provisional modeling input, not a verified rail diameter.

**Why:** The only direct field measurement was an approximate 125 mm
circumference taken with a fabric tape on 2026-08-08. That converts to about
39.79 mm, but neither the tape result nor the rounded 40 mm value is exact. The
first lined clamp's known result is more useful: its 42.1 mm modeled bore still
slid slightly on the rail.

**How to apply:** Keep the provisional input as a stable baseline while
iterating, and express each revision as a direct bore-diameter adjustment from
a physically tested part. Do not describe a calculated liner preload or exact
rail diameter unless a later measurement establishes it. The next test uses a
41.3 mm modeled bore, which is 0.8 mm narrower than the tested clamp.
