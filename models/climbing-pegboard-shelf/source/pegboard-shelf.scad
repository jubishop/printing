// Climbing pegboard shelf
// Original parametric design. Dimensions are millimetres.
//
// The first export is a low-material fit peg. It is not a climbing component.

part = "fit-peg"; // [fit-peg]

// Measurements supplied on 2026-09-03.
measured_hole_diameter = 31.2;
measured_hole_depth = 38.3;

// Start with a removable slip fit. Change this after the physical test rather
// than scaling the STL. The clearance is across the complete diameter.
diametral_clearance = 0.4;
rear_clearance = 1.5;

peg_diameter = measured_hole_diameter - diametral_clearance;
insertion_length = measured_hole_depth - rear_clearance;

// The fit gauge is a tube with a broad pull flange. The body wall is thick
// enough to stay round during an ordinary hand-fit test while using much less
// material than a solid peg.
tube_wall = 2.4;
tip_chamfer = 1.0;
flange_diameter = 42.0;
flange_thickness = 4.0;
flange_edge_chamfer = 0.8;
body_flange_overlap = 0.1;

$fn = 128;

assert(measured_hole_diameter > 0, "Hole diameter must be positive.");
assert(measured_hole_depth > 0, "Hole depth must be positive.");
assert(diametral_clearance >= 0, "Diametral clearance must not be negative.");
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

module chamfered_flange() {
    union() {
        cylinder(
            h = flange_edge_chamfer,
            d1 = flange_diameter - 2 * flange_edge_chamfer,
            d2 = flange_diameter
        );
        translate([0, 0, flange_edge_chamfer])
            cylinder(
                h = flange_thickness - 2 * flange_edge_chamfer,
                d = flange_diameter
            );
        translate([0, 0, flange_thickness - flange_edge_chamfer])
            cylinder(
                h = flange_edge_chamfer,
                d1 = flange_diameter,
                d2 = flange_diameter - 2 * flange_edge_chamfer
            );
    }
}

module fit_peg() {
    inner_diameter = peg_diameter - 2 * tube_wall;

    difference() {
        union() {
            chamfered_flange();

            // A small overlap produces one connected mesh instead of relying
            // on two solids that only touch at a coplanar face.
            translate([0, 0, flange_thickness - body_flange_overlap])
                cylinder(
                    h = insertion_length - tip_chamfer
                        + body_flange_overlap,
                    d = peg_diameter
                );

            translate([
                0,
                0,
                flange_thickness + insertion_length - tip_chamfer
            ])
                cylinder(
                    h = tip_chamfer,
                    d1 = peg_diameter,
                    d2 = peg_diameter - 2 * tip_chamfer
                );
        }

        // Leave a closed base inside the pull flange, but keep the top open so
        // the model has no bridge or support requirement.
        translate([0, 0, flange_thickness])
            cylinder(
                h = insertion_length + 0.01,
                d = inner_diameter
            );
    }
}

if (part == "fit-peg") {
    fit_peg();
} else {
    assert(false, str("Unknown part selector: ", part));
}
