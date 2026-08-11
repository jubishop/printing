# Skillmill rail catch-all tray

An original, parametric catch-all tray for the round upper rail on a Technogym
Skillmill. The 155 x 85 x 38 mm tray is intended for light objects such as a TV
remote, AirPods case, or keys. The rail mount and clamp print in PETG, while the
separate tray prints in PLA.

The clamp uses printed structural parts with common Ace-style metric hardware:

- A two-piece PETG circular saddle surrounds the rail.
- A removable M6 x 50 mm bolt, two washers, and a nylon-insert locknut form the
  hinge.
- An M6 x 30 mm bolt passes through smooth clearance holes into a captive M6
  nylon-insert locknut in the lower latch lug.
- A 1.6 mm split gap provides actual tightening travel.
- The PETG upper mount ends in a 72 x 32 x 5 mm shelf and broad backplate that
  carry the PLA tray.
- Four recessed M4 x 12 mm Phillips pan-head machine screws and captive M4
  nylon-insert locknuts fasten the tray to the mount while the shelf carries its
  vertical load.

This replaces the first prototype's printed screw and integral female thread,
which were physically tested and found to have inadequate engagement.

## Rail measurement and current size

On 2026-08-08 the rail circumference was measured with a fabric tape at about
125 mm. That calculates to 39.79 mm diameter, but the fabric-tape measurement
was approximate. The rail was never directly measured at 40 mm. The current
exports retain **40.0 mm as a provisional modeling input**, not a verified rail
dimension, so successive fit tests have a consistent calibration baseline.

The OpenSCAD source accepts either measurement:

```scad
rail_measurement_mode = "diameter"; // "diameter" or "circumference"
rail_circumference = 125.0;
rail_diameter = 40.0;
```

Only the value selected by `rail_measurement_mode` is used. Circumference is the
easier field measurement; diameter is useful for a known nominal tube size or
caliper measurement.

The first clamp used that provisional input, 0.8 mm of radial liner allowance,
and 0.25 mm of radial fit clearance, producing a 42.1 mm bore. Physical testing
found that it still slid slightly after the rubber liner was installed. The
current revision applies a direct -0.8 mm bore-diameter calibration, producing a
41.3 mm modeled bore. The 2026-08-10 physical test found that this bore and the
installed liner fit the rail perfectly. This validates the complete bore/liner
combination, not an exact bare-rail diameter or exact liner compression. Adjust
the source parameters rather than scaling an STL.

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

### Standard hardware strategy

The final prototype uses only M4-0.7 and M6-1.0 coarse metric threads. These are
ordinary hardware-drawer sizes rather than design-specific printed threads.
Ace's catalog includes the selected [M4 x 12 mm Phillips pan-head machine
screw](https://www.acehardware.com/departments/hardware/screws-and-anchors/machine-screws/5306410),
[M6 x 30 mm hex-head bolt](https://www.acehardware.com/departments/hardware/nuts-and-bolts/hex-bolts/5167499),
and [M6 x 50 mm hex-head bolt](https://www.acehardware.com/departments/hardware/nuts-and-bolts/hex-bolts/5167531).
Those pages establish that the sizes are standard catalog items, not that a
particular local store has them in stock.

The M8 latch from the preceding one-kit iteration was deliberately reduced to
M6. M6 already supplies far more clamp force than the PETG lugs need, while the
smaller clearance hole and locknut pocket leave appreciably more plastic around
the latch. Using M6 for both hinge and latch also removes a wrench size and an
entire nut/washer family from the shopping list.

### Complete hardware used by one final catch-all

| Quantity | Hardware | What it does |
| ---: | --- | --- |
| 1 | M6 x 30 mm hex-head bolt | Tightens the clamp's latch around the lined rail. |
| 1 | M6 nylon-insert locknut, about 10 mm across flats and 6 mm thick | Sits captive in the lower latch lug so it cannot turn. |
| 1 | M6 flat washer, about 12 mm outside diameter | Spreads the latch-bolt-head load across the PETG upper lug. |
| 1 | M6 x 50 mm hex-head bolt | Replaces the trapped printed pin and serves as the removable hinge axle. |
| 2 | M6 flat washers, about 12 mm outside diameter | Protect the PETG hinge ends under the bolt head and locknut. |
| 1 | M6 nylon-insert locknut | Holds the hinge bolt securely without requiring the hinge to be clamped solid. |
| 4 | M4 x 12 mm Phillips pan-head machine screws | Fasten the PLA tray's reinforced wall to the PETG backplate. |
| 4 | M4 nylon-insert locknuts, about 7 mm across flats and 5 mm thick | Load into captive pockets in the PETG backplate for the tray screws. |
| 1 | Soft rubber liner | Fills the modeled 0.8 mm radial allowance and supplies grip when compressed by the clamp. |

No M4 washers are used in the tray joint. Each M4 pan head sits in a 9.2 mm
round counterbore and is driven with an ordinary Phillips screwdriver, while
the PETG pockets capture the locknuts.

Useful installation tools are two 10 mm wrenches or sockets for the M6 hardware
and a Phillips #2 screwdriver for the recessed M4 tray screws.

### Latch hardware

- One M6 x 30 mm hex-head bolt
- One M6 nylon-insert locknut, approximately 10 mm across flats and 6 mm thick
- One M6 flat washer, approximately 12 mm outside diameter

The modeled latch dimensions are:

- Bolt clearance hole: 7.0 mm, including FDM hole allowance
- Captive-locknut pocket: 10.6 mm across flats x 6.6 mm deep
- Modeled bolt length: 30 mm

The small hardware-fit gauge tests the exact clearance hole and nut pocket. A
nut should enter with light finger pressure, sit fully below the top surface,
and resist turning without splitting the gauge.

The already-printed threaded clamp remains a superseded prototype. The final M6
latch geometry requires a newly printed lower saddle.

### Hinge hardware

- One M6 x 50 mm hex-head bolt
- Two M6 flat washers, approximately 12 mm outside diameter
- One M6 nylon-insert locknut

The printed hinge bore is 6.6 mm and the reinforced barrel is 13 mm outside
diameter. Put one washer under the bolt head and one under the locknut. Tighten
the locknut only enough to remove side-to-side play;
the hinge must still rotate freely. Unlike the latch nut, a nylon-insert nut is
appropriate here because it can remain secure without clamping the hinge solid.

This removable hardware replaces the original snap-barbed printed pin. The
first pin retained successfully but could not be removed without risking the
printed clamp, preventing the lower saddle from being reused with a different
upper.

### PLA tray attachment hardware

- Four M4 x 12 mm Phillips pan-head machine screws
- Four M4 nylon-insert locknuts, approximately 7 mm across flats and 5 mm thick
- No M4 washers

The screw heads recess into 9.2 mm counterbores from inside the tray. The
locknuts load into rear-opening captive pockets in the 8 mm PETG backplate.
M4 x 12 mm provides full locknut engagement and approximately 1.0 mm modeled
protrusion behind the mount. Do not substitute longer screws unless their
clearance behind the mount is checked.

## Files

Editable source:

- `source/skillmill-rail-catchall.scad`

Low-material test parts:

- `exports/skillmill-hardware-fit-gauge-m4-m6.stl`
- `exports/skillmill-fit-upper-right-40mm.stl`
- `exports/skillmill-fit-upper-left-40mm.stl`

Full tray parts:

- `exports/skillmill-petg-mount-upper-right-40mm.stl`
- `exports/skillmill-petg-mount-upper-left-40mm.stl`
- `exports/skillmill-catchall-lower-right-40mm.stl`
- `exports/skillmill-catchall-lower-left-40mm.stl`
- `exports/skillmill-pla-tray.stl`

Bambu Studio X2D projects:

- `exports/skillmill-hardware-fit-gauge-m4-m6.3mf` contains the one-part PETG
  hardware-fit gauge plate.
- `exports/skillmill-catchall-lower-right-40mm.3mf` contains the current 41.3 mm
  bore right-hand fit upper and matching lower saddle, with the corrected
  orientation and PETG/support-interface assignments used for the 2026-08-10
  tighter-bore retry.
- `exports/skillmill-catchall-petg-mount-right-40mm.3mf` contains the final
  right-hand PETG upper mount and matching lower saddle, including the removable
  hinge-bore support membranes and the support routing used for the first final
  mount attempt.

The projects were saved by Bambu Studio 2.7.1.62 on 2026-08-10. They contain
slice settings and model-render thumbnails but no generated G-code. The
embedded Bambu account designer identifier was removed before publication;
printer serials, session data, and local filesystem paths are not present.

The fit-upper and lower STLs are print-oriented: each stands on a flat clamp-end
face with the rail channel and M6 hinge bore vertical. The full PETG upper stands
on the +X side of its 72 mm tray backplate, which also leaves the hinge bore
vertical. Do not rotate these files back to the installed orientation shown in
the assembly renders. The source retains explicit `*-assembly` selectors for
geometry inspection, while the ordinary single-part selectors produce the
print-oriented exports.

Each suspended hinge knuckle contains a 0.4 mm removable membrane across the
6.6 mm bore at its first two layers. This turns the support-contact face into a
solid disk instead of an unsupported thin ring. After support removal, push the
membrane out with the M6 bolt or turn a 6 mm drill bit through it by hand. Do
not use a powered drill against the assembled clamp.

Preview:

- `renders/skillmill-catchall-assembly-40mm.png`
- `renders/skillmill-latch-hardware-detail.png`

Use matching left or right PETG upper/lower parts. The PLA tray is the same for
either handed mount. The fit-test upper mates with the same lower saddle and
manufactured latch/hinge hardware used by the full mount. The removable M6
hinge bolt allows the fit-test upper to be replaced by the full mount without
sacrificing the lower saddle.

The ignored local project
`.local/models/skillmill-fit-test-40mm-two-plate.3mf` contains the superseded
printed-screw geometry and must not be used for another print without replacing
its models and reslicing.

## Recommended validation workflow

### Step 1 - PETG hardware-fit gauge

Print `skillmill-hardware-fit-gauge-m4-m6.stl` after buying the hardware and
before another clamp:

- PETG, 0.20 mm layer height, 4 walls, 30% infill.
- Print with both hex pockets facing upward.
- No supports are required.
- The left station tests the M6 latch bolt and captive locknut pocket.
- The center station tests the M6 hinge-bolt clearance.
- The right station tests the M4 tray screw and captive locknut pocket.

If a locknut will not seat, increase its corresponding pocket-across-flats
parameter by 0.2 mm. If it spins freely, reduce that parameter by 0.2 mm. Do
not scale the entire gauge or clamp.

### Step 2 - PETG fit clamp

The 2026-08-10 fit test passed with the 41.3 mm modeled bore and installed
liner. For a replacement fit test:

- One `skillmill-fit-upper-right-40mm.stl`.
- One `skillmill-catchall-lower-right-40mm.stl`.
- The validated M6 latch bolt, washer, and captive locknut.
- The M6 hinge bolt, two washers, and nylon-insert locknut.

Recommended starting settings:

- Bambu Lab X2D, 0.4 mm hardened-steel nozzle, Textured PEI.
- PETG Basic or PETG HF.
- 0.20 mm layer height.
- 5 walls and 5 top/bottom shells.
- 30% gyroid or cross-hatch infill.
- 8 mm outer brim on both parts.
- Enable build-plate-only support beneath the suspended latch and hinge
  geometry. Use PETG for the support base and Bambu Support for PLA/PETG only
  at the interface.
- Paint or constrain support to those underside surfaces. Keep it out of the
  vertical rail channel and hinge bore, and block it inside the 7.0 mm latch
  hole and captive locknut pocket when possible. The horizontal latch hole can
  bridge its short span; clean and test it with the M6 hardware before assembly.

The 2026-08-10 retry failed because the earlier STLs retained assembly
orientation. Their minimum-Z features were curved and provided no coplanar bed
area, even though the first-layer camera view initially looked acceptable. The
current print-oriented exports replace those files and must be resliced from
scratch; do not reuse the failed job or its plate data.

### Step 3 - final PETG mount and PLA tray

After the gauge and fit clamp pass:

- Print the selected handed PETG mount and its matching PETG lower saddle.
- Print `skillmill-pla-tray.stl` separately in PLA, flat bottom on the plate.
- The PLA tray needs no supports.
- The PETG mount requires support around the clamp and bridge. Use PETG for the
  support base and Bambu Support for PLA/PETG only at the support interface
  after verifying the two-nozzle mapping in Bambu Studio.
- Keep support out of the 7.0 mm latch holes, latch locknut pocket, 6.6 mm hinge
  bore, four M4 clearance holes, four M4 head counterbores, and four M4
  locknut pockets when possible. Clean and test every hardware opening before
  assembly.
- The print-oriented PETG upper has 421.4 mm2 of planar contact on the side of
  its backplate. Use an 8 mm outer brim and build-plate-only tree support. Keep
  the generated 0.4 mm hinge membranes; they are intentional and removable.

No separate PLA screw plate is needed.

## Hardware installation and fit test

1. Confirm the M6 and M4 locknuts and both bolt diameters fit the gauge.
2. Press the M6 locknut into the bottom-opening hex pocket in the lower saddle.
3. Join the clamp halves with the M6 x 50 mm hinge bolt and one washer on each
   side. Tighten the nylon-insert nut only until side play is removed and verify
   that the hinge still pivots freely.
4. Press the four M4 locknuts into the rear-facing pockets in the PETG mount.
   Rest the PLA tray on the PETG shelf, align the four holes, and install the
   four M4 x 12 mm pan-head screws from inside the tray using a Phillips #2
   screwdriver.
   Tighten only until the tray is seated firmly against the backplate.
5. Install the liner around the stopped, unoccupied Skillmill.
6. Place the M6 washer under the latch-bolt head and pass the bolt downward
   through both lugs into the captive locknut.
7. Tighten only until the clamp cannot rotate under a gentle hand load. The
   latch gap must not bottom out.
8. Test stationary, then empty at walking speed, then with one light object.
9. Report whether the liner prevents rotation and how much latch gap remains.

Do not overtighten. The metal hardware can generate far more clamping force than
the PETG lugs need and can crush or split them if treated like a structural
machine joint.

## Geometry verification

OpenSCAD 2021.01 regenerated all eight current STLs with `--hardwarnings` and
reported each as a simple 3D object. A separate triangle-edge audit found no
open or non-manifold edges. Current print-oriented bounding boxes are:

- Each PETG mount upper: 66.15 x 111.8 x 72.0 mm.
- Each print-oriented lower: 33.15 x 93.8 x 32.0 mm.
- Each print-oriented fit upper: 33.15 x 93.8 x 32.0 mm.
- PLA tray: 155.0 x 85.0 x 38.0 mm, with 34.8 mm of usable wall height
  above the 3.2 mm floor.
- Hardware-fit gauge: 60.0 x 20.0 x 13.0 mm.

The rigid print-orientation transform preserves the structural geometry. Each
fit upper has 435.9 mm2 of coplanar first-layer area, each lower has 556.6 mm2,
and each full upper has 421.4 mm2. The print-only hinge membranes add 0.4 mm
closures that are removed after printing. The failed assembly-oriented fit
exports had zero coplanar first-layer area.

The source asserts clearance, bolt-length, and retained-wall requirements for
both hardware sizes. The M6 hinge retains 3.2 mm of PETG around its bore; the
M4 head counterbores retain at least 3 mm of PLA on every side; the M4 locknut
pockets leave 2.4 mm of PETG ahead of them; and the M6 latch locknut pocket
leaves 6.4 mm of PETG above it. The assembly render uses a 30 mm M6 reference
latch bolt with its washer and captive locknut, a 50 mm M6 reference hinge bolt
with two washers and a locknut, and four 12 mm M4 reference tray screws with
captive locknuts. Physical hardware fit and the 41.3 mm bore/liner rail grip are
validated. Support-removal quality for the new membranes and payload capacity
still require testing.

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
  structural mount with a mechanically fastened PLA tray on 2026-08-10. The
  hardware was first standardized around one M4/M6/M8 assortment, then refined
  to common M4/M6 Ace-style hardware later that day. After a layer-37 adhesion
  failure on 2026-08-10, the fit-upper and lower exports were rotated from
  assembly orientation onto verified planar clamp-end footprints. After a
  supported hinge face printed as loose rings, suspended hinge bores gained
  removable 0.4 mm membranes and the full upper gained a verified planar
  backplate-side print orientation.
- Tool versions: OpenSCAD 2021.01 generated and verified the STL exports;
  Bambu Studio 2.7.1.62 saved the documented X2D project archives.
- Upstream geometry: none.
- License: all rights reserved; no permission to redistribute is granted yet.
- Reference checked 2026-08-08: [Technogym Skillmill assembly manual](https://fitnesssuperstore.info/pdfs/Technogym%20Skillmill%20-%20The%20Curved%20Treadmill%20Assembly%20Manual.pdf).
- MakerWorld comparison checked 2026-08-08: [Drink Holder for THERUN Treadmill (and others)](https://makerworld.com/en/models/243012-drink-holder-for-therun-treadmill-and-others), CC BY-NC-SA 4.0. Its files and geometry were not copied.
- MakerWorld comparison checked 2026-08-08: [Clamp Rail system cup holder w/ lots of addons](https://makerworld.com/en/models/527070-clamp-rail-system-cup-holder-w-lots-of-addons), MakerWorld Standard Digital File License. Its files and geometry were not copied.

No third-party model or profile is stored in this directory.
