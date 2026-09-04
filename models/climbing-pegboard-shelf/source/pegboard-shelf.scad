// Climbing pegboard shelf
// Original parametric design. Dimensions are millimetres.
//
// The exports are low-material fit pegs. They are not climbing components.

part = "fit-peg"; // [fit-peg, spacing-gauge]
fit_variant = "fifth"; // [first, second, third, fourth, fifth]

// Measurements supplied on 2026-09-03.
measured_hole_diameter = 31.2;
measured_hole_depth = 38.3;

// The fourth reached the back at 39.2 mm. Lock the working insertion length
// at the proven 39.0 mm. The fifth's 32.0 mm diameter was confirmed a perfect
// individual fit on 2026-09-04.
locked_insertion_length = 39.0;
locked_peg_diameter = 32.0;
diameter_adjustment = fit_variant == "first" ? -0.4
    : fit_variant == "second" ? 0.0
    : fit_variant == "third" ? 0.4
    : fit_variant == "fourth" ? 0.6
    : 0.8;
depth_adjustment = fit_variant == "first" ? -1.5
    : fit_variant == "fourth" ? 0.9
    : 0.7;

peg_diameter = fit_variant == "fifth" ? locked_peg_diameter
    : measured_hole_diameter + diameter_adjustment;
insertion_length = fit_variant == "fifth" ? locked_insertion_length
    : measured_hole_depth + depth_adjustment;

// The fit gauge is a tube with a broad pull flange. The body wall is thick
// enough to stay round during an ordinary hand-fit test while using much less
// material than a solid peg.
tube_wall = 2.4;
tip_chamfer = 1.0;
flange_diameter = 42.0;
flange_thickness = 4.0;
flange_edge_chamfer = 0.8;
body_flange_overlap = 0.1;

// User's nearest-edge gap: rightmost edge of the left hole to leftmost edge
// of the right hole. This is not a measured center-to-center distance.
// Use the fitted CAD peg diameter to make a first empirical spacing trial;
// it is not proof that the physical hole diameter is exactly 32.0 mm.
spacing_inner_gap = 146.5;
spacing_center_distance = spacing_inner_gap + locked_peg_diameter;
spacing_bar_width = 24.0;
spacing_base_thickness = 8.0;

$fn = 128;

assert(measured_hole_diameter > 0, "Hole diameter must be positive.");
assert(measured_hole_depth > 0, "Hole depth must be positive.");
assert(
    fit_variant == "first"
        || fit_variant == "second"
        || fit_variant == "third"
        || fit_variant == "fourth"
        || fit_variant == "fifth",
    str("Unknown fit variant: ", fit_variant));
assert(peg_diameter > 0, "Peg diameter must be positive.");
assert(insertion_length > 0, "Insertion length must be positive.");
assert(2 * tube_wall < peg_diameter, "Tube wall leaves no hollow center.");
assert(2 * tip_chamfer < peg_diameter, "Tip chamfer is too large.");
assert(flange_diameter > measured_hole_diameter,
    "Flange must be larger than the pegboard hole.");
assert(2 * flange_edge_chamfer < flange_thickness,
    "Flange chamfers consume its thickness.");
assert(body_flange_overlap > 0 && body_flange_overlap < flange_thickness,
    "Body/flange overlap must be positive and smaller than the flange.");
assert(spacing_inner_gap > 0, "Spacing gap must be positive.");
assert(spacing_bar_width > 0 && spacing_bar_width < flange_diameter,
    "Connecting bar must be narrower than the pull flanges.");
assert(spacing_base_thickness >= flange_thickness,
    "Spacing gauge base must not be thinner than the single-peg flange.");

module chamfered_flange(thickness = flange_thickness) {
    union() {
        cylinder(
            h = flange_edge_chamfer,
            d1 = flange_diameter - 2 * flange_edge_chamfer,
            d2 = flange_diameter
        );
        translate([0, 0, flange_edge_chamfer])
            cylinder(
                h = thickness - 2 * flange_edge_chamfer,
                d = flange_diameter
            );
        translate([0, 0, thickness - flange_edge_chamfer])
            cylinder(
                h = flange_edge_chamfer,
                d1 = flange_diameter,
                d2 = flange_diameter - 2 * flange_edge_chamfer
            );
    }
}

module fit_peg(
    diameter = peg_diameter,
    length = insertion_length,
    base_thickness = flange_thickness
) {
    inner_diameter = diameter - 2 * tube_wall;

    difference() {
        union() {
            chamfered_flange(base_thickness);

            // A small overlap produces one connected mesh instead of relying
            // on two solids that only touch at a coplanar face.
            translate([0, 0, base_thickness - body_flange_overlap])
                cylinder(
                    h = length - tip_chamfer
                        + body_flange_overlap,
                    d = diameter
                );

            translate([
                0,
                0,
                base_thickness + length - tip_chamfer
            ])
                cylinder(
                    h = tip_chamfer,
                    d1 = diameter,
                    d2 = diameter - 2 * tip_chamfer
                );
        }

        // Leave a closed base inside the pull flange, but keep the top open so
        // the model has no bridge or support requirement.
        translate([0, 0, base_thickness])
            cylinder(
                h = length + 0.01,
                d = inner_diameter
            );
    }
}

module spacing_gauge() {
    union() {
        for (side = [-1, 1]) {
            translate([side * spacing_center_distance / 2, 0, 0])
                fit_peg(
                    diameter = locked_peg_diameter,
                    length = locked_insertion_length,
                    base_thickness = spacing_base_thickness
                );
        }

        // The bar and both flanges have the same board-contact plane.
        // Increasing base thickness therefore leaves 39 mm of usable peg.
        translate([-spacing_center_distance / 2, -spacing_bar_width / 2, 0])
            cube([
                spacing_center_distance,
                spacing_bar_width,
                spacing_base_thickness
            ]);
    }
}

if (part == "fit-peg") {
    fit_peg();
} else if (part == "spacing-gauge") {
    spacing_gauge();
} else {
    assert(false, str("Unknown part selector: ", part));
}
