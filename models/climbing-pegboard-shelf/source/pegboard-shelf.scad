// Climbing pegboard shelf
// Original parametric design. Dimensions are millimetres.
//
// The fit exports are low-material gauges. The shelf is a light-duty accessory.
// None of these parts are climbing components.

part = "fit-peg"; // [fit-peg, spacing-gauge, shelf, installed-preview]
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

// Final shelf draft. Installed coordinates use X across the pegboard, Y out
// from the wall, and Z up. The 5 mm overhang is measured past the outside of
// each fitted 32 mm peg body, so the shelf width closely follows the proven
// two-peg gauge rather than becoming unnecessarily wide.
shelf_side_overhang = 5.0;
shelf_width = spacing_center_distance
    + locked_peg_diameter
    + 2 * shelf_side_overhang;
shelf_depth = 100.0; // pegboard contact plane to front face
shelf_deck_thickness = 8.0;
shelf_lip_height = 12.0;
shelf_lip_thickness = 3.2;
shelf_lip_overlap = 0.2;
shelf_front_corner_radius = 12.0;
shelf_lower_side_radius = 3.0;
shelf_backplate_thickness = spacing_base_thickness;

// The board ends 17 mm below the lower edge of each hole. Align the shelf's
// bottom face with that board edge. With an 8 mm deck and a 32 mm fitted peg,
// the resulting peg axis is 25 mm above the shelf surface.
hole_bottom_to_board_edge = 17.0;
shelf_peg_center_height = -shelf_deck_thickness
    + hole_bottom_to_board_edge
    + locked_peg_diameter / 2;
shelf_center_backwall_height = shelf_peg_center_height;

// Non-printing reference board used only by the installed preview.
preview_board_width = 280.0;
preview_board_depth = locked_insertion_length;
preview_board_height = 110.0;
preview_hole_clearance = 0.4;

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
assert(shelf_side_overhang > 0, "Shelf must extend past both fitted pegs.");
assert(shelf_depth > shelf_backplate_thickness + shelf_lip_thickness,
    "Shelf is too shallow for its backplate and front lip.");
assert(shelf_deck_thickness > 0, "Shelf deck thickness must be positive.");
assert(shelf_lip_height > 0 && shelf_lip_thickness > 0,
    "Shelf lip dimensions must be positive.");
assert(shelf_lip_overlap > 0
        && shelf_lip_overlap < shelf_deck_thickness,
    "Shelf lip overlap must stay inside the deck.");
assert(shelf_front_corner_radius > shelf_lip_thickness,
    "Front corner radius must exceed the lip thickness.");
assert(2 * shelf_front_corner_radius < shelf_width
        && 2 * shelf_front_corner_radius < shelf_depth,
    "Front corner radius is too large for the shelf.");
assert(shelf_lower_side_radius > 0
        && shelf_lower_side_radius < shelf_deck_thickness,
    "Lower side radius must fit within the deck thickness.");
assert(hole_bottom_to_board_edge > shelf_deck_thickness,
    "Hole must sit above the aligned shelf bottom.");
assert(shelf_peg_center_height - flange_diameter / 2
        < shelf_lip_height,
    "Peg flange must overlap the rear lip.");
assert(shelf_peg_center_height - flange_diameter / 2
        > -shelf_deck_thickness,
    "Peg flange must stay above the aligned board edge.");
assert(shelf_center_backwall_height > shelf_lip_height,
    "Raised center backwall must extend above the retaining lip.");
assert(shelf_center_backwall_height <= shelf_peg_center_height,
    "Raised center backwall must not extend above the peg axes.");

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

module rounded_front_outline_2d(width, depth, radius) {
    union() {
        translate([-width / 2, 0])
            square([width, depth - radius]);

        translate([
            -width / 2 + radius,
            depth - radius
        ])
            square([width - 2 * radius, radius]);

        for (side = [-1, 1]) {
            translate([
                side * (width / 2 - radius),
                depth - radius
            ])
                circle(r = radius);
        }
    }
}

module rounded_lower_side_profile_2d(width, height, radius) {
    union() {
        translate([-width / 2 + radius, 0])
            square([width - 2 * radius, height]);

        translate([-width / 2, radius])
            square([width, height - radius]);

        for (side = [-1, 1]) {
            translate([side * (width / 2 - radius), radius])
                circle(r = radius);
        }
    }
}

module rounded_lower_front_profile_2d(depth, height, radius) {
    union() {
        square([depth - radius, height]);

        translate([0, radius])
            square([depth, height - radius]);

        translate([depth - radius, radius])
            circle(r = radius);
    }
}

module rounded_shelf_deck() {
    intersection() {
        translate([0, 0, -shelf_deck_thickness])
            linear_extrude(height = shelf_deck_thickness)
                rounded_front_outline_2d(
                    shelf_width,
                    shelf_depth,
                    shelf_front_corner_radius
                );

        // Round the two long lower side edges. The generous center of the
        // underside remains flat and level with the pegboard's bottom.
        translate([
            0,
            shelf_depth + 0.01,
            -shelf_deck_thickness
        ])
            rotate([90, 0, 0])
                linear_extrude(height = shelf_depth + 0.02)
                    rounded_lower_side_profile_2d(
                        shelf_width,
                        shelf_deck_thickness,
                        shelf_lower_side_radius
                    );

        // Round the exposed lower front edge. The rear contact edge stays
        // square and flat against the pegboard backing.
        translate([
            -shelf_width / 2 - 0.01,
            0,
            -shelf_deck_thickness
        ])
            rotate([90, 0, 90])
                linear_extrude(height = shelf_width + 0.02)
                    rounded_lower_front_profile_2d(
                        shelf_depth,
                        shelf_deck_thickness,
                        shelf_lower_side_radius
                    );
    }
}

module rounded_rear_backplate() {
    backplate_height = shelf_deck_thickness + shelf_lip_height;

    intersection() {
        translate([
            -shelf_width / 2,
            0,
            -shelf_deck_thickness
        ])
            cube([
                shelf_width,
                shelf_backplate_thickness,
                backplate_height
            ]);

        translate([
            0,
            shelf_backplate_thickness + 0.01,
            -shelf_deck_thickness
        ])
            rotate([90, 0, 0])
                linear_extrude(
                    height = shelf_backplate_thickness + 0.02
                )
                    rounded_lower_side_profile_2d(
                        shelf_width,
                        backplate_height,
                        shelf_lower_side_radius
                    );

    }
}

module final_shelf() {
    union() {
        // Full-depth platform. Its outside depth is measured from the
        // pegboard contact plane to the front face.
        rounded_shelf_deck();

        // This rear lip spans from the shelf bottom to 12 mm above its top.
        // When installed, its lower edge aligns with the pegboard's lower edge
        // and the wood below both holes becomes the load-bearing back support.
        rounded_rear_backplate();

        // Raise only the wall between the peg centerlines. Its 25 mm top is
        // level with the peg axes, giving each circular flange 21 mm of
        // vertical overlap. The rounded full-width backplate carries the load
        // below the deck surface, so this added section starts at the deck.
        translate([
            -spacing_center_distance / 2,
            0,
            0
        ])
            cube([
                spacing_center_distance,
                shelf_backplate_thickness,
                shelf_center_backwall_height
            ]);

        // The side and front rim follows the same rounded outline as the deck.
        // The inner radius is offset by the lip thickness for a uniform wall.
        translate([0, 0, -shelf_lip_overlap])
            linear_extrude(
                height = shelf_lip_height + shelf_lip_overlap
            )
                difference() {
                    rounded_front_outline_2d(
                        shelf_width,
                        shelf_depth,
                        shelf_front_corner_radius
                    );

                    translate([0, shelf_backplate_thickness])
                        rounded_front_outline_2d(
                            shelf_width - 2 * shelf_lip_thickness,
                            shelf_depth
                                - shelf_backplate_thickness
                                - shelf_lip_thickness,
                            shelf_front_corner_radius
                                - shelf_lip_thickness
                        );
                }

        // Reuse the exact proven peg and flange geometry. Each circular flange
        // overlaps the rear lip, making a continuous vertical load path from
        // the hole to the shelf. Rotation makes the tubes point into the board
        // while retaining the proven 39 mm insertion length.
        for (side = [-1, 1]) {
            translate([
                side * spacing_center_distance / 2,
                shelf_backplate_thickness,
                shelf_peg_center_height
            ])
                rotate([90, 0, 0])
                    fit_peg(
                        diameter = locked_peg_diameter,
                        length = locked_insertion_length,
                        base_thickness = shelf_backplate_thickness
                    );
        }

    }
}

module installed_preview() {
    color([0.95, 0.72, 0.10])
        final_shelf();

    // Reference board only. Its lower edge is aligned to the shelf bottom,
    // and the two cutouts expose the confirmed peg position and spacing.
    color([0.78, 0.60, 0.38])
        difference() {
            translate([
                -preview_board_width / 2,
                -preview_board_depth,
                -shelf_deck_thickness
            ])
                cube([
                    preview_board_width,
                    preview_board_depth,
                    preview_board_height
                ]);

            for (side = [-1, 1]) {
                translate([
                    side * spacing_center_distance / 2,
                    0.1,
                    shelf_peg_center_height
                ])
                    rotate([90, 0, 0])
                        cylinder(
                            h = preview_board_depth + 0.2,
                            d = locked_peg_diameter + preview_hole_clearance
                        );
            }
        }
}

if (part == "fit-peg") {
    fit_peg();
} else if (part == "spacing-gauge") {
    spacing_gauge();
} else if (part == "shelf") {
    final_shelf();
} else if (part == "installed-preview") {
    installed_preview();
} else {
    assert(false, str("Unknown part selector: ", part));
}
