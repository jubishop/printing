# Skillmill rail catch-all tray

An original, parametric catch-all tray for the round upper rail on a Technogym
Skillmill. The 155 x 85 x 28 mm tray is intended for light objects such as a TV
remote, AirPods case, or keys. The rail mount and clamp print in PETG, while the
separate tray prints in PLA.

The clamp uses printed structural parts with manufactured latch hardware:

- A two-piece PETG circular saddle surrounds the rail.
- A removable M5 bolt, two washers, and a nylon-insert lock nut form the hinge.
- A manufactured M8 or 5/16 inch bolt passes through smooth clearance holes.
- A matching standard hex nut sits in a bottom-loading captive pocket in the
  lower lug, so the nut cannot rotate while the bolt is tightened.
- A 1.6 mm split gap provides actual tightening travel.
- The PETG upper mount ends in a 72 x 32 x 5 mm shelf and broad backplate that
  carry the PLA tray.
- Four recessed M4 button-head screws and captive M4 nuts fasten the tray to the
  mount while the shelf carries its vertical load.

This replaces the first prototype's printed screw and integral female thread,
which were physically tested and found to have inadequate engagement.

## Rail measurement and current size

On 2026-08-08 the rail circumference was measured with a fabric tape at about
125 mm. That calculates to 39.79 mm diameter and strongly indicates a nominal
40 mm tube. The current exports therefore use **40.0 mm diameter**.

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
The first 40 mm clamp has a 42.1 mm bore and was loose when tested without the
liner; test it again with the ordered liner before changing the rail diameter.

## Why the first printed screw failed

The first design used a nominal 12 mm x 3 mm-pitch printed thread, but it applied
clearance in both directions:

- The male screw was scaled to `12.0 * 0.94 = 11.28 mm` major diameter.
- The female cutting thread was enlarged to `12.0 + 2 * 0.40 = 12.80 mm`.
- With only 1.2 mm thread depth, the female thread's inward crest was 10.40 mm
  diameter.
- The ideal male/female radial overlap was therefore only
  `(11.28 - 10.40) / 2 = 0.44 mm`.

That 0.44 mm theoretical engagement was too small to survive ordinary FDM
rounding and dimensional variation across the PETG female thread and PLA male
thread. The fully solid screws printed cleanly but slid through the lower lug
without catching. Printing the same screw again would not correct the modeled
clearance error.

A separately printed bolt and nut would make the nut replaceable and easier to
calibrate, but it would still depend on printed thread accuracy. Manufactured
hardware removes that failure mode and is the more reliable choice for a tray
cantilevered from the rail.

## Why the tray and mount are separate

The first full upper combined the clamp, bridge, and tray into one PETG print.
The current design separates those functions instead of relying on a weak
PLA-to-PETG fused interface:

- The complete rail clamp, bridge, tray shelf, and backplate print in PETG.
- The tray prints upright in PLA with a flat bottom and no support requirement.
- The tray sits directly on the PETG shelf, so its weight does not hang from the
  M4 screws or pull against the PLA wall.
- Four M4 screws clamp the tray's reinforced near wall against the PETG
  backplate and resist pull-off and twisting.

The materials are joined only with mechanical fasteners. They do not need to
bond to one another during printing.

## Hardware specification

### Complete purchase list for one final catch-all

| Quantity | Hardware | What it does |
| ---: | --- | --- |
| 1 | M8 x 30 mm hex-head bolt | Tightens the clamp's latch around the lined rail. |
| 1 | Standard M8 hex nut, about 13 mm across flats and 6.5 mm thick | Sits captive in the lower latch lug so it cannot turn. |
| 1 | M8 flat washer, 16-18 mm outside diameter | Spreads the latch-bolt-head load across the PETG upper lug. |
| 1 | M5 x 45 mm hex-head bolt | Replaces the trapped printed pin and serves as the removable hinge axle. |
| 2 | M5 flat washers, about 10 mm outside diameter | Protect the PETG hinge ends under the bolt head and lock nut. |
| 1 | M5 nylon-insert lock nut | Holds the hinge bolt securely without requiring the hinge to be clamped solid. |
| 4 | M4 x 10 mm button-head socket screws | Fasten the PLA tray's reinforced wall to the PETG backplate. |
| 4 | Standard M4 hex nuts, about 7 mm across flats and 3.2 mm thick | Load into captive pockets in the PETG backplate for the tray screws. |
| 1 | Soft rubber liner, already ordered | Fills the modeled 0.8 mm radial allowance, adds grip, and stops the clamp rotating on the rail. |

No M4 washers are needed: each button head sits in a flat-bottomed recess in the
reinforced PLA wall, and the PETG pockets capture the nuts. The modeled M4
button head is approximately 7.6 mm diameter x 2.2 mm high; ordinary ISO 7380-1
button-head socket screws are the intended form.

You need only one latch hardware system. The preferred list above is metric.
If buying M8 locally is inconvenient, replace all three M8 latch items with the
matched 5/16-inch set described below; do not mix an M8 bolt with a 5/16-inch
nut.

Useful installation tools, if not already owned, are a 13 mm wrench or socket
for the M8 latch, two 8 mm wrenches or sockets for the M5 hinge, and a 2.5 mm
hex key for typical M4 button-head screws.

### Latch hardware

The same printed geometry supports either of these matched sets:

#### Preferred metric set

- One M8 x 30 mm hex-head bolt
- One standard M8 hex nut, approximately 13 mm across flats and 6.5 mm thick
- One M8 flat washer, approximately 16-18 mm outside diameter

#### U.S. hardware-store alternative

- One 5/16-18 x 1-1/4 inch hex-head bolt
- One standard 5/16-18 hex nut, 1/2 inch across flats
- One 5/16 inch flat washer, approximately 11/16-3/4 inch outside diameter

For the latch, use a regular full-height hex nut, not a wing nut, flange nut,
coupling nut, or nylon-insert lock nut; those do not match the captive pocket.
Zinc-plated or stainless steel is suitable. The modeled dimensions are:

- Bolt clearance hole: 9.2 mm, including FDM hole allowance
- Captive-nut pocket: 13.6 mm across flats x 7.2 mm deep
- Modeled bolt length: 30 mm

The small hardware-fit gauge tests the exact clearance hole and nut pocket. A
nut should enter with light finger pressure, sit fully below the top surface,
and resist turning without splitting the gauge.

The already-printed threaded clamp can be tested temporarily with an external
nut rather than the captive pocket, but it needs a longer M8 x 35 mm or
5/16-18 x 1-1/2 inch bolt. That is only a rough clamp/liner test; the redesigned
lower saddle is required for the final captive-nut configuration. The longer
bolt is optional and is not used in the final assembly; the 30 mm bolt is the
correct final M8 length.

### Hinge hardware

- One M5 x 45 mm hex-head bolt
- Two M5 flat washers, approximately 10 mm outside diameter
- One M5 nylon-insert lock nut

The printed hinge bore is 5.5 mm. Put one washer under the bolt head and one
under the lock nut. Tighten the lock nut only enough to remove side-to-side play;
the hinge must still rotate freely. Unlike the latch nut, a nylon-insert nut is
appropriate here because it can remain secure without clamping the hinge solid.

This removable hardware replaces the original snap-barbed printed pin. The
first pin retained successfully but could not be removed without risking the
printed clamp, preventing the lower saddle from being reused with a different
upper.

### PLA tray attachment hardware

- Four M4 x 10 mm button-head socket screws
- Four standard M4 hex nuts, approximately 7 mm across flats and 3.2 mm thick
- No M4 washers

The screw heads recess into the tray from the inside. The nuts load into
rear-opening captive pockets in the PETG backplate. M4 x 10 mm provides full
nut engagement with the modeled recesses without excessive protrusion; do not
substitute longer screws unless their clearance behind the mount is checked.

## Files

Editable source:

- `source/skillmill-rail-catchall.scad`

Low-material test parts:

- `exports/skillmill-hardware-fit-gauge-m8-5-16.stl`
- `exports/skillmill-fit-upper-right-40mm.stl`
- `exports/skillmill-fit-upper-left-40mm.stl`

Full tray parts:

- `exports/skillmill-petg-mount-upper-right-40mm.stl`
- `exports/skillmill-petg-mount-upper-left-40mm.stl`
- `exports/skillmill-catchall-lower-right-40mm.stl`
- `exports/skillmill-catchall-lower-left-40mm.stl`
- `exports/skillmill-pla-tray.stl`

Preview:

- `renders/skillmill-catchall-assembly-40mm.png`
- `renders/skillmill-latch-hardware-detail.png`

Use matching left or right PETG upper/lower parts. The PLA tray is the same for
either handed mount. The fit-test upper mates with the same lower saddle and
manufactured latch/hinge hardware used by the full mount. The removable M5
hinge bolt allows the fit-test upper to be replaced by the full mount without
sacrificing the lower saddle.

The ignored local project
`.local/models/skillmill-fit-test-40mm-two-plate.3mf` contains the superseded
printed-screw geometry and must not be used for another print without replacing
its models and reslicing.

## Recommended validation workflow

### Step 1 - PETG hardware-fit gauge

Print `skillmill-hardware-fit-gauge-m8-5-16.stl` before another clamp:

- PETG, 0.20 mm layer height, 4 walls, 30% infill.
- Print with the hex pocket facing upward.
- No supports are required.
- Test the exact nut and bolt bought for the project.

If the nut will not seat, increase `latch_nut_pocket_across_flats` by 0.2 mm.
If it spins freely, reduce that parameter by 0.2 mm. Do not scale the entire
gauge or clamp.

### Step 2 - PETG fit clamp

For the next fit test:

- One `skillmill-fit-upper-right-40mm.stl`.
- One `skillmill-catchall-lower-right-40mm.stl`.
- The validated manufactured latch bolt, washer, and captive nut.
- The M5 hinge bolt, two washers, and nylon-insert lock nut.

Recommended starting settings:

- Bambu Lab X2D, 0.4 mm hardened-steel nozzle, Textured PEI.
- PETG Basic or PETG HF.
- 0.20 mm layer height.
- 5 walls and 5 top/bottom shells.
- 30% gyroid or cross-hatch infill.

### Step 3 - final PETG mount and PLA tray

After the gauge and fit clamp pass:

- Print the selected handed PETG mount and its matching PETG lower saddle.
- Print `skillmill-pla-tray.stl` separately in PLA, flat bottom on the plate.
- The PLA tray needs no supports.
- The PETG mount requires support around the clamp and bridge. Use PETG for the
  support base and Bambu Support for PLA/PETG only at the support interface
  after verifying the two-nozzle mapping in Bambu Studio.
- Keep support out of the 9.2 mm latch holes, latch nut pocket, 5.5 mm hinge
  bore, four M4 clearance holes, and four M4 nut pockets when possible. Clean
  and test every hardware opening before assembly.

No separate PLA screw plate is needed.

## Hardware installation and fit test

1. Confirm the latch nut fits the printed gauge.
2. Press the latch nut into the bottom-opening hex pocket in the lower saddle.
3. Join the clamp halves with the M5 hinge bolt and one washer on each side.
   Tighten the nylon-insert nut only until side play is removed and verify that
   the hinge still pivots freely.
4. Press the four standard M4 nuts into the rear-facing pockets in the PETG
   mount. Rest the PLA tray on the PETG shelf, align the four holes, and install
   the four M4 x 10 mm button-head screws from inside the tray. Tighten only
   until the tray is seated firmly against the backplate.
5. Install the liner around the stopped, unoccupied Skillmill.
6. Place the latch washer under the M8 or 5/16 inch bolt head and pass the bolt
   downward through both
   lugs into the captive nut.
7. Tighten only until the clamp cannot rotate under a gentle hand load. The
   latch gap must not bottom out.
8. Test stationary, then empty at walking speed, then with one light object.
9. Report whether the liner prevents rotation and how much latch gap remains.

Do not overtighten. The metal hardware can generate far more clamping force than
the PETG lugs need and can crush or split them if treated like a structural
machine joint.

## Geometry verification

OpenSCAD 2021.01 rendered all eight current STLs with `--hardwarnings`, without
a CGAL error, and reported each as a simple 3D object:

- Each PETG mount upper: 72.0 x 112.6 x 62.55 mm.
- Each lower: 32.0 x 92.6 x 32.55 mm.
- Each fit upper: 32.0 x 92.6 x 32.55 mm.
- PLA tray: 155.0 x 85.0 x 28.0 mm.
- Hardware-fit gauge: 20.0 x 20.0 x 13.0 mm.

The source asserts clearance and retained-wall requirements for the M8 latch
and M4 tray hardware, plus sufficient modeled screw length for full M4 nut
engagement. The assembly render uses a 30 mm M8 reference latch bolt with its
washer and captive nut, a 45 mm M5 reference hinge bolt with two washers and a
nut, and four 10 mm M4 reference tray screws with captive nuts. Physical
hardware fit, rail grip, support-removal quality, and payload capacity still
require testing.

## Safety limits for the prototype

- Mount the tray outboard and rearward so it does not reduce the usable hand
  grip, block controls, or project into the running envelope.
- Test stationary, then empty at walking speed, then with one light object.
- Keep the initial payload below 500 g.
- Do not use it for drinks, phones, weights, or anything whose fall could enter
  the moving belt until the printed prototype has been validated.
- Do not overtighten against the coated rail or PETG lugs.

## Provenance and licensing

- Model and source: original work created for this repository on 2026-08-08,
  revised for manufactured latch hardware on 2026-08-09, and split into a PETG
  structural mount with a mechanically fastened PLA tray on 2026-08-10.
- Upstream geometry: none.
- License: all rights reserved; no permission to redistribute is granted yet.
- Reference checked 2026-08-08: [Technogym Skillmill assembly manual](https://fitnesssuperstore.info/pdfs/Technogym%20Skillmill%20-%20The%20Curved%20Treadmill%20Assembly%20Manual.pdf).
- MakerWorld comparison checked 2026-08-08: [Drink Holder for THERUN Treadmill (and others)](https://makerworld.com/en/models/243012-drink-holder-for-therun-treadmill-and-others), CC BY-NC-SA 4.0. Its files and geometry were not copied.
- MakerWorld comparison checked 2026-08-08: [Clamp Rail system cup holder w/ lots of addons](https://makerworld.com/en/models/527070-clamp-rail-system-cup-holder-w-lots-of-addons), MakerWorld Standard Digital File License. Its files and geometry were not copied.

No third-party model or profile is stored in this directory.
