# Skillmill rail catch-all tray

An original, parametric catch-all tray for the round upper rail on a Technogym
Skillmill. The 155 x 85 x 28 mm tray is intended for light objects such as a TV
remote, AirPods case, or keys.

The clamp is fully printed:

- A two-piece circular saddle surrounds the rail.
- A snap-retained printed pin forms the hinge.
- A coarse printed screw passes through the upper lug and engages a printed
  female thread in the lower lug.
- A 1.6 mm split gap provides actual tightening travel.

No metal fastener or nut is required. A soft liner is still strongly recommended
to protect the Skillmill's finish and resist rotation.

## Rail measurement and current size

On 2026-08-08 the rail circumference was measured with a fabric tape at about
125 mm. That calculates to 39.79 mm diameter and strongly indicates a nominal
40 mm tube. The first fit-test exports therefore use **40.0 mm diameter**.

The OpenSCAD source accepts either measurement:

```scad
rail_measurement_mode = "diameter"; // "diameter" or "circumference"
rail_circumference = 125.0;
rail_diameter = 40.0;
```

Only the value selected by `rail_measurement_mode` is used. Circumference is the
easier field measurement; diameter is useful for a known nominal tube size or
caliper measurement.

The clamp bore adds 0.8 mm radial liner allowance plus 0.25 mm radial fit
clearance. Adjust those parameters independently rather than scaling the STL.

## Files

Editable source:

- `source/skillmill-rail-catchall.scad`

Low-material fit-test parts:

- `exports/skillmill-fit-upper-right-40mm.stl`
- `exports/skillmill-fit-upper-left-40mm.stl`

Full tray parts:

- `exports/skillmill-catchall-upper-right-40mm.stl`
- `exports/skillmill-catchall-upper-left-40mm.stl`
- `exports/skillmill-catchall-lower-right-40mm.stl`
- `exports/skillmill-catchall-lower-left-40mm.stl`

Printed hardware:

- `exports/skillmill-clamp-screw-12x3-pla.stl`
- `exports/skillmill-hinge-pin-petg.stl`

Preview:

- `renders/skillmill-catchall-assembly-40mm.png`

Use matching left or right upper/lower parts. The fit-test upper mates with the
same lower saddle, screw, and hinge pin used by the full tray, so successful
test hardware can be reused.

## Recommended two-plate workflow

Two material plates make sense for this design.

A local, ready-to-review Bambu Studio fit-test project is saved at
`.local/models/skillmill-fit-test-40mm-two-plate.3mf`. It is intentionally
ignored by Git because it contains machine/profile metadata. Its two plates are:

- `PETG fit clamp`: right-hand fit upper, matching lower, and hinge pin.
- `PLA screws`: two vertically oriented screw copies.

The saved X2D project uses a Textured PEI plate, 0.4 mm nozzles, 0.16 mm
Standard process, 6 walls, 5 top/bottom shells, 30% grid infill, and 40 mm/s
outer walls. Tree Hybrid support is enabled globally; it is generated for the
PETG clamp features but not for the screws. PETG remains the support base while
Bambu Support for PLA/PETG is used only for the zero-gap interface through the
auxiliary nozzle.

Final local slice checks on 2026-08-08:

- PETG fit clamp: 60.65 g, approximately 3 h 19 min, including the support
  interface and prime tower, with the parts separated and the earlier layer-one
  path conflict resolved.
- PLA screws: 10.81 g, approximately 39 min 46 s, with no generated support.

These are slicer estimates, not completed print results. The PETG fit-clamp
plate was sent to the X2D at 22:43 PDT on 2026-08-08; its outcome is recorded in
`prints/2026-08-08-skillmill-40mm-fit-clamp.md`.

### Plate 1 - PETG structural parts

For the first fit test:

- One `skillmill-fit-upper-right-40mm.stl`.
- One `skillmill-catchall-lower-right-40mm.stl`.
- One `skillmill-hinge-pin-petg.stl`.

After the fit is confirmed, print only the matching full upper tray and reuse
the lower saddle and pin.

Recommended starting settings:

- Bambu Lab X2D, 0.4 mm hardened-steel nozzle, Textured PEI.
- PETG Basic.
- 0.20 mm layer height.
- 5 walls and 5 top/bottom shells.
- 30% gyroid or cross-hatch infill.
- Print the hinge pin vertically on its flat head at 0.16 mm layer height and
  100% infill.

The full upper tray requires support around the integrated clamp and bridge.
Use PETG for support base and Bambu Support for PLA/PETG only at the interface
after verifying the two-nozzle mapping in Bambu Studio. Do not use support on
the printed screw threads.

### Plate 2 - PLA screws

- Print two copies of `skillmill-clamp-screw-12x3-pla.stl`, vertically with the
  knob on the bed.
- PLA Basic, 0.16 mm layer height, 6 walls, 100% infill.
- Slow the thread's outer wall to about 40 mm/s if the selected profile would
  otherwise print it faster.

PLA is recommended for the screw because it prints sharper threads than PETG.
PLA running in the PETG female thread is also less likely to gall or bind than
PETG-on-PETG. The second copy is a spare and provides a direct consistency
check.

## Printed thread and hinge details

- Nominal thread: custom coarse 12 mm major diameter, 3 mm pitch.
- The exported screw is slightly undersized and the female groove is oversized
  for FDM clearance; it is not an ISO M12 fastener.
- Female thread engagement: approximately four turns.
- Screw tip is tapered to help find the first thread.
- Hinge pin: 5.0 mm shaft in a 5.5 mm bore with a split snap barb.

Run the screw through the lower saddle several times before installing the
clamp. Stop if it cross-threads; back it out, remove any stringing, and restart.
Do not lubricate unless the lubricant is known to be safe for both PLA and PETG.

## Fit-test sequence

1. Print the right-hand fit upper, matching lower, hinge pin, and two screws.
2. Test the screw in the lower saddle off the treadmill.
3. Add approximately 0.8 mm EPDM, silicone, or TPU liner pads.
4. Assemble the empty clamp on the stopped, unoccupied Skillmill.
5. Tighten only until the clamp cannot rotate under a gentle hand load. The
   latch gap must not bottom out.
6. Report whether the halves close, whether the screw turns cleanly, and how
   much latch gap remains. Adjust the source parameters before printing the tray
   if needed.

## Geometry verification

OpenSCAD 2021.01 rendered all eight 40 mm STLs without a CGAL error. Bambu
Studio 2.7.1.62 reports every export as one manifold part:

- Each full upper: 155.0 x 163.6 x 66.55 mm.
- Each lower: 32.0 x 92.6 x 32.55 mm.
- Each fit upper: 32.0 x 92.6 x 32.55 mm.
- Screw: 24.0 x 24.0 x 38.0 mm.
- Hinge pin: 9.0 x 9.0 x 38.6 mm.

Exact mesh checks show no nominal collision between the upper/lower clamp halves
or between the installed hinge pin and clamp. The coarse thread includes
deliberately generous printable clearance, but it still requires a physical
fit test because FDM thread behavior depends on filament, extrusion, and seam
quality.

This verifies geometry integrity, X2D build-volume fit, the saved fit-test plate
arrangement, and intended PETG/PLA object assignment. It does not verify physical
rail fit, printed thread fit, support-removal quality, or load capacity.

## Safety limits for the prototype

- Mount the tray outboard and rearward so it does not reduce the usable hand
  grip, block controls, or project into the running envelope.
- Test stationary, then empty at walking speed, then with one light object.
- Keep the initial payload below 500 g.
- Do not use it for drinks, phones, weights, or anything whose fall could enter
  the moving belt until the printed prototype has been validated.
- Do not overtighten against the coated rail.

## Provenance and licensing

- Model and source: original work created for this repository on 2026-08-08.
- Upstream geometry: none.
- License: all rights reserved; no permission to redistribute is granted yet.
- Reference checked 2026-08-08: [Technogym Skillmill assembly manual](https://fitnesssuperstore.info/pdfs/Technogym%20Skillmill%20-%20The%20Curved%20Treadmill%20Assembly%20Manual.pdf).
- MakerWorld comparison checked 2026-08-08: [Drink Holder for THERUN Treadmill (and others)](https://makerworld.com/en/models/243012-drink-holder-for-therun-treadmill-and-others), CC BY-NC-SA 4.0. Its files and geometry were not copied.
- MakerWorld comparison checked 2026-08-08: [Clamp Rail system cup holder w/ lots of addons](https://makerworld.com/en/models/527070-clamp-rail-system-cup-holder-w-lots-of-addons), MakerWorld Standard Digital File License. Its files and geometry were not copied.

No third-party model or profile is stored in this directory.
