# Climbing pegboard shelf

An original, parametric shelf system for temporary use in two holes of Jubi's
wooden climbing pegboard. Five single-peg gauges established the individual
fit, and the first two-peg gauge confirmed the spacing. The repository now also
contains the first full-shelf CAD draft; it has not been printed or load-tested.

This is not climbing equipment. The eventual shelf is only for light,
stationary objects while the climbing pegboard is unoccupied. Remove every
shelf component before anyone uses the pegboard.

The user-specified maximum combined object load is **2 lb (0.91 kg)**. This is
a design limit, not a tested load rating. The finished shelf must be physically
tested before use, and the load must remain stationary and reasonably close to
the pegboard.

## Provenance and license

- Creator: Jubi, with OpenAI Codex modeling assistance.
- Source: original design; no third-party model or profile was used.
- Source URL and profile ID: not applicable.
- License: all rights reserved pending Jubi's choice of a publication license.
- Created: 2026-09-03.
- Local modifications: five single-peg variants, one rigid two-peg spacing
  gauge, and one full-shelf draft based on the completed fit tests.
- Latest model update: 2026-09-04, using OpenSCAD 2021.01.

## Supplied measurements

- Both holes have the same measured diameter: 31.2 mm.
- Both holes have the same measured depth: 38.3 mm.
- Approximate nearest-edge gap: 146.5 mm, supplied on 2026-09-04. This is the
  minimum distance from the rightmost edge of the left hole to the leftmost
  edge of the right hole, measured with calipers.
- Physical center-to-center spacing has not been measured directly. The first
  spacing gauge uses a trial CAD center spacing of 178.5 mm.
- The first connected gauge fit both holes on its first trial, confirming that
  178.5 mm modeled center spacing for the final shelf.
- The lower edge of each hole is 17 mm above the pegboard's lower edge.

The plywood holes may be slightly oval or tapered, and the 31.2 mm measurement
is approximate. Do not force a gauge that starts to bind.

## First fit gauge

The first gauge uses:

- 30.8 mm outside diameter, giving 0.4 mm diametral clearance.
- 36.8 mm insertion length, leaving 1.5 mm before the measured rear limit.
- 2.4 mm modeled tube wall.
- 1.0 mm lead-in chamfer.
- 42.0 x 4.0 mm pull flange.

Print it upright with the flange on the build plate. It needs no support. Use
the same printer, nozzle, filament type, and dimensional compensation intended
for the next peg iteration. Do not scale the STL; change the parameters in the
OpenSCAD source and regenerate it.

Success means the gauge enters to the flange with ordinary hand pressure,
slides out without tools, does not scrape or mark the plywood, and has little
side-to-side movement. If it binds, create a new variant with 0.2 mm less
outside diameter. If it is clearly loose, increase the next diameter in
0.2 mm steps. Preserve each earlier variant for comparison.

The first gauge entered fully, so 36.8 mm is not too long. It remained
noticeably wiggly, and the test did not establish whether the hole continues
past the gauge tip.

## Second fit gauge

The second gauge changes only the two unresolved fit dimensions:

- 31.2 mm outside diameter, giving zero nominal diametral clearance.
- 39.0 mm insertion length, extending 0.7 mm past the measured hole depth.
- The same 2.4 mm tube wall, 1.0 mm lead-in chamfer, and 42.0 x 4.0 mm pull
  flange.

The deliberate depth overtravel makes rear contact visible: if the 38.3 mm
measurement is close, the flange should remain slightly away from the board
when the tip reaches the back. Do not force the gauge if its larger diameter
starts to bind.

The second gauge confirmed that 39.0 mm is a good insertion length. Its
31.2 mm body still had noticeable side-to-side movement.

## Third fit gauge

The third gauge changes only the remaining unresolved dimension:

- 31.6 mm outside diameter, 0.4 mm larger than the second gauge and nominally
  0.4 mm larger than the approximate measured hole diameter.
- The proven 39.0 mm insertion length.
- The same 2.4 mm tube wall, 1.0 mm lead-in chamfer, and 42.0 x 4.0 mm pull
  flange.

This is an empirical fit test because the first two printed gauges were looser
than their modeled dimensions suggested. Do not force the third gauge if it
starts to bind.

The third gauge was closer, but its 31.6 mm body still needed a tighter fit.
The user also requested a small depth increase from its 39.0 mm insertion
length.

## Fourth fit gauge

The fourth gauge changes both dimensions by the requested 0.2 mm:

- 31.8 mm outside diameter.
- 39.2 mm insertion length.
- The same 2.4 mm tube wall, 1.0 mm lead-in chamfer, and 42.0 x 4.0 mm pull
  flange.

The 31.8 mm modeled diameter is nominally 0.6 mm larger than the approximate
hole measurement. Do not force it if it starts to bind.

The fourth gauge reached the back before the flange seated against the board.
The user confirmed that the earlier 39.0 mm insertion length was correct.
**The insertion length is now locked at 39.0 mm.**

## Fifth fit gauge

The fifth gauge tests the next diameter while restoring the proven depth:

- 32.0 mm outside diameter, 0.2 mm larger than the fourth gauge.
- 39.0 mm insertion length, 0.2 mm shorter than the fourth gauge.
- The same 2.4 mm tube wall, 1.0 mm lead-in chamfer, and 42.0 x 4.0 mm pull
  flange.

The modeled diameter is nominally 0.8 mm larger than the approximate hole
measurement. This is an empirical fit test. Do not force it if it binds.

The user reported that the fifth gauge fit perfectly. The fitted model
dimensions are now locked at **32.0 mm diameter and 39.0 mm insertion length**.
This does not establish an exact measured diameter for the physical holes.

## First two-peg spacing gauge

The two-peg gauge retains the fitted peg geometry and adds a stiff connecting
bar. It tests simultaneous insertion before the full shelf is designed.

- Modeled gap between nearest peg surfaces: 146.5 mm.
- Trial center-to-center spacing: 178.5 mm (146.5 + the fitted CAD diameter
  of 32.0 mm). This is a starting model choice, not a confirmed hole-center
  measurement; print-size error and approximate caliper readings remain.
- Each peg: 32.0 mm outside diameter, 39.0 mm usable insertion length,
  2.4 mm tube wall, and 1.0 mm tip chamfer.
- Connecting bar: 24.0 mm wide and 8.0 mm thick.
- Both pull flanges are also 8.0 mm thick. Their board-contact faces are level
  with the bar, so the full 39.0 mm of each peg remains usable.
- Overall envelope: 220.5 x 42.0 x 47.0 mm.

Print the bar and flanges flat on the plate, with both pegs upright. There are
no support requirements. The prepared PLA slice retains the same process
settings as the successful fifth peg: 0.20 mm layers, 2 walls, 15% grid,
auto brim, and unchanged dimensional compensation. Its estimate is 1 hour
12 minutes 25 seconds, 40.22 g, and 13.48 m.

The user confirmed the machine was ready on 2026-09-04. Studio sent the gauge
at 08:45 PDT after a fresh live preflight, with PLA from AMS A3 assigned to the
main 0.4 mm nozzle and all three calibration controls explicitly `Auto`.
Device-page readback confirmed the exact job active at 0/235 layers, with an
initial estimated finish of 09:57 PDT. The user later reported that the gauge
nailed the simultaneous fit on the first trial.

Both pegs entered together successfully, so no spacing adjustment is needed.
This gauge confirmed fit and alignment only; it did not test the strength or
load capacity of the eventual shelf.

To regenerate the spacing gauge from the repository root:

```sh
openscad --hardwarnings -D 'part="spacing-gauge"' \
  -o models/climbing-pegboard-shelf/exports/pegboard-spacing-gauge-gap146p5-cc178p5mm.stl \
  models/climbing-pegboard-shelf/source/pegboard-shelf.scad
```

The default source output remains the fifth single peg. Earlier variants are
available through `fit_variant`, with `part="fit-peg"`.

## Full shelf draft

The first full-shelf model uses the completed fit data and the final requested
envelope:

- Width: 220.5 mm. This is 5 mm beyond the outside of each 32 mm peg body and
  matches the total width of the successful spacing gauge's 42 mm flanges.
- Depth: 100 mm from the pegboard contact plane to the front face.
- Deck: 6 mm thick.
- Retaining lip: 12 mm above the deck and 3.2 mm thick on both sides and the
  front.
- Rear lip: 8 mm thick, spanning from the shelf bottom to 12 mm above the deck.
- Pegs: the proven 32 mm outside diameter, 39 mm insertion length, 2.4 mm tube
  wall, 1 mm tip chamfer, and 178.5 mm center spacing.
- Peg flanges: 42 mm diameter and 8 mm thick, integrated into the rear lip.

The shelf bottom aligns with the pegboard's lower edge. Because the hole bottom
is 17 mm above that edge, each peg axis sits 27 mm above the shelf surface:
`-6 + 17 + 16 = 27 mm`. The rear lip bears on the wood below the holes and
overlaps both circular peg flanges. This creates the short vertical load path
that the earlier backplate and underside-gusset concept needed, without large
braces hanging below the board. The side and front lips also stiffen the deck.

The printable shelf export is one connected, watertight mesh with consistent
face orientation and 4,220 triangles. Its installed bounds are 220.5 mm wide,
100 mm forward of the wall, 39 mm behind the wall for the pegs, and 54 mm tall.
It remains an unprinted draft with a proposed maximum stationary load of 2 lb;
that limit must be confirmed by a cautious physical load test.

To regenerate the printable shelf from the repository root:

```sh
openscad --hardwarnings -D 'part="shelf"' \
  -o models/climbing-pegboard-shelf/exports/pegboard-shelf-220p5x100-lip12mm.stl \
  models/climbing-pegboard-shelf/source/pegboard-shelf.scad
```

`part="installed-preview"` adds a non-printing reference board for the assembly
render. Never export that preview scene as the printable shelf.

## Files

- Editable source: `source/pegboard-shelf.scad`
- First fit export: `exports/pegboard-fit-peg-30p8mm.stl`
- Second fit export: `exports/pegboard-fit-peg-31p2x39p0mm.stl`
- Second fit render: `renders/pegboard-fit-peg-31p2x39p0mm.png`
- Third fit export: `exports/pegboard-fit-peg-31p6x39p0mm.stl`
- Third fit render: `renders/pegboard-fit-peg-31p6x39p0mm.png`
- Fourth fit export: `exports/pegboard-fit-peg-31p8x39p2mm.stl`
- Fourth fit render: `renders/pegboard-fit-peg-31p8x39p2mm.png`
- Fifth fit export: `exports/pegboard-fit-peg-32p0x39p0mm.stl`
- Fifth fit render: `renders/pegboard-fit-peg-32p0x39p0mm.png`
- Spacing-gauge export: `exports/pegboard-spacing-gauge-gap146p5-cc178p5mm.stl`
- Spacing-gauge render: `renders/pegboard-spacing-gauge-gap146p5-cc178p5mm.png`
- Full-shelf export: `exports/pegboard-shelf-220p5x100-lip12mm.stl`
- Full-shelf open/rear render:
  `renders/pegboard-shelf-220p5x100-lip12mm-front.png`
- Full-shelf installed render:
  `renders/pegboard-shelf-220p5x100-lip12mm-installed.png`
- Local slicer project:
  `.local/models/climbing-pegboard-shelf/pegboard-fit-peg-30p8mm-pla.3mf`
  from the repository root. It remains ignored because it contains local
  printer and filament configuration.
- Second local slicer project:
  `.local/models/climbing-pegboard-shelf/pegboard-fit-peg-31p2x39p0mm-pla.3mf`.
- Third local slicer project:
  `.local/models/climbing-pegboard-shelf/pegboard-fit-peg-31p6x39p0mm-pla.3mf`.
- Fourth local slicer project:
  `.local/models/climbing-pegboard-shelf/pegboard-fit-peg-31p8x39p2mm-pla.3mf`.
- Fifth local slicer project:
  `.local/models/climbing-pegboard-shelf/pegboard-fit-peg-32p0x39p0mm-pla.3mf`.
- Spacing-gauge local slicer project:
  `.local/models/climbing-pegboard-shelf/pegboard-spacing-gauge-gap146p5-cc178p5mm-pla.3mf`.

OpenSCAD generated and mesh-checked the STL. Bambu Studio 02.08.02.61 sliced
the first fit gauge for the X2D with both nozzle diameters synchronized at
0.4 mm, the Textured PEI Plate, and Bambu PLA Pure assigned to the main nozzle
from AMS slot A3.

The second gauge is sliced with the same printer, plate, nozzle, and PLA A3
routing. Its estimate is 41 minutes 10 seconds, 12.10 g, and 4.06 m. Bambu
Studio sent it to the printer at 17:31 PDT on 2026-09-03 after all three
available calibration controls were freshly verified as `Auto`.

The third gauge uses the same verified setup. Its estimate is 41 minutes
41 seconds, 12.22 g, and 4.10 m. Bambu Studio sent it to the printer at
19:38 PDT on 2026-09-03 after all three available calibration controls were
freshly verified as `Auto`.

The fourth gauge also uses that setup. Its estimate is 41 minutes 54 seconds,
12.32 g, and 4.13 m. Bambu Studio sent it to the printer at 21:42 PDT on
2026-09-03 after all three available calibration controls were freshly
verified as `Auto`.

The fifth gauge retains the same printer and process settings. Its estimate
is 41 minutes 22 seconds, 12.33 g, and 4.14 m. Bambu Studio sent it at
07:12 PDT on 2026-09-04 with PLA mapped to AMS A3 and all three calibration
controls freshly verified as `Auto`.

PLA is the selected material for the fit gauge and the planned shelf. Its
stiffness and clean print quality suit this light, temporary indoor use. The
draft now uses the board-edge-aligned rear lip and integrated peg flanges as
its back support. It still needs slice review and a physical load test.

## Work remaining before use

- Review and approve the shelf shape and dimensions.
- Choose a print orientation and inspect the complete slice and supports.
- Print the shelf in PLA, confirm that both pegs still fit, and perform a
  cautious load test before placing ordinary objects on it.
