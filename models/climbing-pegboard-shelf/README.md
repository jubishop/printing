# Climbing pegboard shelf

An original, parametric shelf system for temporary use in two holes of Jubi's
wooden climbing pegboard. The shelf itself has not been designed yet. The first
artifact is a low-material gauge for calibrating the fit of one removable peg.

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
- Local modifications: initial parametric fit gauge based on measurements of
  the physical pegboard.

## Supplied measurements

- Both holes have the same measured diameter: 31.2 mm.
- Both holes have the same measured depth: 38.3 mm.
- Hole-center spacing has not been measured yet.

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
side-to-side movement. If it binds, reduce `peg_diameter` by increasing
`diametral_clearance` in 0.2 mm steps. If it is clearly loose, decrease the
clearance in 0.2 mm steps.

## Files

- Editable source: `source/pegboard-shelf.scad`
- First fit export: `exports/pegboard-fit-peg-30p8mm.stl`
- Local slicer project:
  `.local/models/climbing-pegboard-shelf/pegboard-fit-peg-30p8mm-pla.3mf`
  from the repository root. It remains ignored because it contains local
  printer and filament configuration.

OpenSCAD generated and mesh-checked the STL. Bambu Studio 02.08.02.61 sliced
the first fit gauge for the X2D with both nozzle diameters synchronized at
0.4 mm, the Textured PEI Plate, and Bambu PLA Pure assigned to the main nozzle
from AMS slot A3.

PLA is the selected material for the fit gauge and the planned shelf. Its
stiffness and clean print quality suit this light, temporary indoor use. The
finished shelf still needs a backplate, gussets, and a physical load test; the
two printed pegs must not carry the full bending load by themselves.

## Final shelf inputs still needed

- Distance between the nearest inner edges of the two holes.
- Desired shelf width and front-to-back depth.
- Clearance behind the pegboard.

The shelf should use a backplate that bears against the pegboard below the two
pegs. This changes the shelf's tipping force into compression against the board
instead of making the printed pegs resist the full bending load alone.
