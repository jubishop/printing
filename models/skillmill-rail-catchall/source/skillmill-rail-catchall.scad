// Skillmill rail catch-all tray
// Original parametric design. Dimensions are millimetres.

// Select one export at a time. Single fit-upper and lower exports are rotated
// onto a flat clamp-end face for printing; assembly selectors retain the
// installed orientation used by the preview renders.
// "assembly-right", "assembly-left", "fit-assembly-right",
// "upper-right", "upper-left", "upper-right-assembly", "upper-left-assembly",
// "lower-right", "lower-left", "fit-upper-right", "fit-upper-left",
// "lower-right-assembly", "lower-left-assembly",
// "fit-upper-right-assembly", "fit-upper-left-assembly",
// "tray-pla", or "hardware-fit-gauge"
part = "assembly-right";

// Choose either input mode. Circumference is easiest with a fabric tape;
// diameter is useful for a known nominal tube size or when using calipers.
rail_measurement_mode = "diameter"; // [circumference, diameter]
rail_circumference = 125.0;
rail_diameter = 40.0; // provisional baseline, not a direct measurement

effective_rail_diameter = rail_measurement_mode == "circumference"
    ? rail_circumference / 3.141592653589793
    : rail_diameter;

assert(
    rail_measurement_mode == "circumference"
        || rail_measurement_mode == "diameter",
    "rail_measurement_mode must be circumference or diameter."
);

// Space for a soft, non-marking liner between the printed clamp and rail.
// The diameter adjustment is empirical: it tightens the next test relative to
// the already-printed clamp without claiming the rail diameter is exact.
liner_thickness = 0.8;
radial_fit_clearance = 0.25;
bore_diameter_adjustment = -0.8;

assert(
    radial_fit_clearance >= 0,
    "radial_fit_clearance must not be negative."
);
assert(
    effective_rail_diameter + 2 * liner_thickness
            + 2 * radial_fit_clearance + bore_diameter_adjustment > 0,
    "The adjusted clamp bore must have a positive diameter."
);

clamp_width = 32;
clamp_wall = 6;
split_gap = 1.6; // closing travel available at the bolted latch

tray_length = 155;
tray_depth = 85;
tray_height = 38;
tray_floor = 3.2;
tray_wall = 2.8;
tray_corner_radius = 9;

tray_mount_width = 72;
tray_mount_height = 27;
tray_mount_pad_thickness = 6.5;
tray_mount_plate_thickness = 8;
tray_mount_shelf_depth = 32;
tray_mount_shelf_thickness = 5;
tray_mount_hole_x = 24;
tray_mount_hole_z_offsets = [9, 18];
tray_fastener_diameter = 4.0;
tray_fastener_clearance_diameter = 4.6;
tray_fastener_length = 12;
tray_fastener_head_diameter = 8.0;
tray_fastener_head_height = 3.1;
tray_fastener_head_access_diameter = 9.2;
tray_fastener_head_recess_depth = 3.4;
tray_nut_across_flats = 7.0;
tray_nut_pocket_across_flats = 7.6;
tray_nut_pocket_rotation = 0;
tray_nut_thickness = 5.0;
tray_nut_pocket_depth = 5.6;

hinge_hole_diameter = 6.6;
hinge_bolt_diameter = 6.0;
hinge_bolt_length = 50;
hinge_bolt_head_across_flats = 10.0;
hinge_bolt_head_height = 4.0;
hinge_washer_outer_diameter = 12;
hinge_washer_thickness = 1.6;
hinge_nut_across_flats = 10.0;
hinge_nut_thickness = 6.0;

latch_bolt_diameter = 6.0;
latch_bolt_clearance_diameter = 7.0;
latch_nut_across_flats = 10.0;
latch_nut_pocket_across_flats = 10.6;
latch_nut_thickness = 6.0;
latch_nut_pocket_depth = 6.6;
latch_bolt_length = 30;
latch_bolt_head_across_flats = 10.0;
latch_bolt_head_height = 4.0;
latch_washer_outer_diameter = 12;
latch_washer_thickness = 1.6;
latch_upper_height = 10;
latch_lower_height = 13;
latch_lug_width = 24;
latch_lug_length = 28;

assert(
    latch_bolt_clearance_diameter > latch_bolt_diameter,
    "The latch bolt clearance hole must be larger than the bolt."
);
assert(
    latch_nut_pocket_across_flats > latch_nut_across_flats,
    "The captive-nut pocket must be larger than the nut."
);
assert(
    latch_nut_pocket_depth > latch_nut_thickness,
    "The captive-nut pocket must be deeper than the nut."
);
assert(
    latch_lug_width
        - latch_nut_pocket_across_flats / cos(30) >= 6,
    "The captive-nut pocket must leave at least 3 mm per side."
);
assert(
    latch_lower_height - latch_nut_pocket_depth >= 4,
    "The captive-nut pocket must leave at least a 4 mm roof."
);
assert(
    latch_bolt_length >= latch_upper_height + split_gap
        + latch_lower_height + latch_washer_thickness + 2,
    "The bolt must protrude at least 2 mm below the lower lug."
);
assert(
    hinge_bolt_length >= clamp_width + 2 * hinge_washer_thickness
        + hinge_nut_thickness + 2,
    "The hinge bolt must pass both washers and the nut."
);
assert(
    tray_mount_pad_thickness - tray_fastener_head_recess_depth >= 3,
    "The PLA tray must retain at least 3 mm behind each screw head."
);
assert(
    tray_fastener_head_access_diameter
        >= tray_fastener_head_diameter + 0.8,
    "The M4 pan-head counterbore must provide at least 0.4 mm radial clearance."
);
assert(
    tray_fastener_head_recess_depth >= tray_fastener_head_height + 0.2,
    "The M4 pan head must sit at least 0.2 mm below the tray surface."
);
assert(
    tray_mount_plate_thickness - tray_nut_pocket_depth >= 2,
    "The PETG backplate must retain at least 2 mm ahead of each nut."
);
assert(
    tray_fastener_length
        >= tray_mount_pad_thickness - tray_fastener_head_recess_depth
            + tray_mount_plate_thickness - tray_nut_pocket_depth
            + tray_nut_thickness + 0.5,
    "The tray screws must fully engage the captive locknuts."
);
assert(
    tray_mount_width / 2 - tray_mount_hole_x
        >= tray_fastener_head_access_diameter / 2 + 3,
    "The tray screw-head counterbores must retain at least a 3 mm side margin."
);
assert(
    min(tray_mount_hole_z_offsets)
            >= tray_fastener_head_access_diameter / 2 + 3
        && tray_mount_height - max(tray_mount_hole_z_offsets)
            >= tray_fastener_head_access_diameter / 2 + 3,
    "The tray screw-head counterbores must retain 3 mm top and bottom margins."
);
assert(
    tray_mount_hole_z_offsets[1] - tray_mount_hole_z_offsets[0]
            - tray_nut_pocket_across_flats >= 1,
    "The rotated M4 locknut pockets must retain at least 1 mm between them."
);

$fn = 96;

clamp_inner_radius =
    effective_rail_diameter / 2 + liner_thickness + radial_fit_clearance
        + bore_diameter_adjustment / 2;
clamp_outer_radius = clamp_inner_radius + clamp_wall;

hinge_barrel_radius = 6.5;
hinge_y = clamp_outer_radius + hinge_barrel_radius + 1.5;
hinge_center_knuckle = 12;
hinge_knuckle_gap = 0.7;
hinge_outer_knuckle =
    (clamp_width - hinge_center_knuckle - 2 * hinge_knuckle_gap) / 2;

assert(
    hinge_barrel_radius - hinge_hole_diameter / 2 >= 3,
    "The hinge barrel must retain at least 3 mm around the M6 bore."
);
latch_bolt_y = -clamp_outer_radius - 14;

tray_near_y = clamp_outer_radius - 1.5;
tray_bottom_z = clamp_outer_radius + 6;

module rounded_rectangle_2d(size, radius) {
    offset(r = radius)
        square([size[0] - 2 * radius, size[1] - 2 * radius], center = true);
}

module rail_ring() {
    rotate([0, 90, 0])
        difference() {
            cylinder(h = clamp_width, r = clamp_outer_radius, center = true);
            cylinder(h = clamp_width + 2, r = clamp_inner_radius, center = true);
        }
}

module upper_saddle() {
    intersection() {
        rail_ring();
        translate([
            -clamp_width,
            -2 * clamp_outer_radius,
            split_gap / 2
        ])
            cube([
                2 * clamp_width,
                4 * clamp_outer_radius,
                2 * clamp_outer_radius
            ]);
    }
}

module lower_saddle() {
    intersection() {
        rail_ring();
        translate([-clamp_width, -2 * clamp_outer_radius, -2 * clamp_outer_radius])
            cube([
                2 * clamp_width,
                4 * clamp_outer_radius,
                2 * clamp_outer_radius - split_gap / 2
            ]);
    }
}

module upper_hinge() {
    difference() {
        union() {
            translate([-hinge_center_knuckle / 2, hinge_y, 0])
                rotate([0, 90, 0])
                    cylinder(h = hinge_center_knuckle, r = hinge_barrel_radius);

            translate([
                -hinge_center_knuckle / 2,
                clamp_outer_radius - 2,
                0
            ])
                cube([
                    hinge_center_knuckle,
                    hinge_y - clamp_outer_radius + 2,
                    hinge_barrel_radius
                ]);
        }

        translate([
            -hinge_center_knuckle / 2 - 1,
            hinge_y,
            0
        ])
            rotate([0, 90, 0])
                cylinder(
                    h = hinge_center_knuckle + 2,
                    d = hinge_hole_diameter
                );
    }
}

module lower_hinge_knuckle(x_start, length) {
    difference() {
        union() {
            translate([x_start, hinge_y, 0])
                rotate([0, 90, 0])
                    cylinder(h = length, r = hinge_barrel_radius);

            translate([
                x_start,
                clamp_outer_radius - 2,
                -hinge_barrel_radius
            ])
                cube([
                    length,
                    hinge_y - clamp_outer_radius + 2,
                    hinge_barrel_radius
                ]);
        }

        translate([x_start - 1, hinge_y, 0])
            rotate([0, 90, 0])
                cylinder(h = length + 2, d = hinge_hole_diameter);
    }
}

module lower_hinge() {
    lower_hinge_knuckle(-clamp_width / 2, hinge_outer_knuckle);
    lower_hinge_knuckle(
        hinge_center_knuckle / 2 + hinge_knuckle_gap,
        hinge_outer_knuckle
    );
}

module hex_prism(across_flats, height, rotation = 30) {
    rotate([0, 0, rotation])
        cylinder(
            h = height,
            d = across_flats / cos(30),
            $fn = 6
        );
}

// Visual reference for the standard M4 Phillips pan-head machine screws.
// The printable tray uses only the matching round clearance and head recess.
module pan_head(diameter, height) {
    difference() {
        cylinder(h = height, d1 = diameter, d2 = diameter * 0.72);

        translate([-diameter / 2, -0.35, height - 0.65])
            cube([diameter, 0.7, 0.75]);
        translate([-0.35, -diameter / 2, height - 0.65])
            cube([0.7, diameter, 0.75]);
    }
}

module upper_latch() {
    difference() {
        translate([
            -latch_lug_width / 2,
            -clamp_outer_radius - latch_lug_length + 2,
            split_gap / 2
        ])
            cube([latch_lug_width, latch_lug_length, latch_upper_height]);

        translate([0, latch_bolt_y, split_gap / 2 - 1])
            cylinder(
                h = latch_upper_height + 2,
                d = latch_bolt_clearance_diameter
            );
    }
}

module lower_latch() {
    difference() {
        translate([
            -latch_lug_width / 2,
            -clamp_outer_radius - latch_lug_length + 2,
            -latch_lower_height - split_gap / 2
        ])
            cube([latch_lug_width, latch_lug_length, latch_lower_height]);

        // Smooth through-hole for the M6 manufactured latch bolt.
        translate([
            0,
            latch_bolt_y,
            -latch_lower_height - split_gap / 2 - 1
        ])
            cylinder(
                h = latch_lower_height + 2,
                d = latch_bolt_clearance_diameter
            );

        // Bottom-opening hex pocket captures the M6 nylon-insert locknut so
        // only the bolt head needs a wrench during installation and tightening.
        translate([
            0,
            latch_bolt_y,
            -latch_lower_height - split_gap / 2 - 0.1
        ])
            hex_prism(
                latch_nut_pocket_across_flats,
                latch_nut_pocket_depth + 0.1
            );
    }
}

module hardware_fit_gauge() {
    gauge_length = 60;
    gauge_depth = 20;
    gauge_height = latch_lower_height;

    difference() {
        translate([-gauge_length / 2, -gauge_depth / 2, 0])
            cube([gauge_length, gauge_depth, gauge_height]);

        // Left station: M6 latch-bolt clearance and captive locknut pocket.
        translate([-20, 0, -1])
            cylinder(
                h = gauge_height + 2,
                d = latch_bolt_clearance_diameter
            );

        translate([
            -20,
            0,
            gauge_height - latch_nut_pocket_depth
        ])
            hex_prism(
                latch_nut_pocket_across_flats,
                latch_nut_pocket_depth + 0.1
            );

        // Center station: M6 hinge-bolt clearance.
        translate([0, 0, -1])
            cylinder(h = gauge_height + 2, d = hinge_hole_diameter);

        // Right station: M4 tray-screw clearance and captive locknut pocket.
        translate([20, 0, -1])
            cylinder(
                h = gauge_height + 2,
                d = tray_fastener_clearance_diameter
            );

        translate([20, 0, gauge_height - tray_nut_pocket_depth])
            hex_prism(
                tray_nut_pocket_across_flats,
                tray_nut_pocket_depth + 0.1,
                tray_nut_pocket_rotation
            );
    }
}

module tray_shell() {
    difference() {
        translate([0, tray_near_y + tray_depth / 2, tray_bottom_z])
            linear_extrude(height = tray_height)
                rounded_rectangle_2d(
                    [tray_length, tray_depth],
                    tray_corner_radius
                );

        translate([
            0,
            tray_near_y + tray_depth / 2,
            tray_bottom_z + tray_floor
        ])
            linear_extrude(height = tray_height + 1)
                rounded_rectangle_2d(
                    [
                        tray_length - 2 * tray_wall,
                        tray_depth - 2 * tray_wall
                    ],
                    tray_corner_radius - tray_wall
                );
    }
}

module tray_mount_pad() {
    translate([
        -tray_mount_width / 2,
        tray_near_y,
        tray_bottom_z
    ])
        cube([
            tray_mount_width,
            tray_mount_pad_thickness,
            tray_mount_height
        ]);
}

module tray_mount_holes() {
    tray_inner_face_y = tray_near_y + tray_mount_pad_thickness;

    for (
        x = [-tray_mount_hole_x, tray_mount_hole_x],
        z_offset = tray_mount_hole_z_offsets
    ) {
        z = tray_bottom_z + z_offset;

        // M4 clearance hole through the reinforced PLA wall.
        translate([x, tray_inner_face_y + 1, z])
            rotate([90, 0, 0])
                cylinder(
                    h = tray_mount_pad_thickness + 2,
                    d = tray_fastener_clearance_diameter
                );

        // Round counterbore recesses a standard M4 Phillips pan head so only a
        // screwdriver, rather than a thin-wall socket, is needed in the tray.
        translate([x, tray_inner_face_y + 0.1, z])
            rotate([90, 0, 0])
                cylinder(
                    h = tray_fastener_head_recess_depth + 0.1,
                    d = tray_fastener_head_access_diameter
                );
    }
}

module pla_tray() {
    difference() {
        union() {
            tray_shell();
            tray_mount_pad();
        }
        tray_mount_holes();
    }
}

module tray_mount_bracket() {
    backplate_y = tray_near_y - tray_mount_plate_thickness;

    difference() {
        union() {
            // The shelf carries the tray's vertical load and keeps that load
            // out of the M4 fasteners and PLA wall.
            translate([
                -tray_mount_width / 2,
                tray_near_y - 0.2,
                tray_bottom_z - tray_mount_shelf_thickness
            ])
                cube([
                    tray_mount_width,
                    tray_mount_shelf_depth + 0.2,
                    tray_mount_shelf_thickness
                ]);

            // Broad rear plate resists pull-off and twisting.
            translate([
                -tray_mount_width / 2,
                backplate_y,
                tray_bottom_z - tray_mount_shelf_thickness
            ])
                cube([
                    tray_mount_width,
                    tray_mount_plate_thickness + 0.2,
                    tray_mount_height + tray_mount_shelf_thickness
                ]);
        }

        for (
            x = [-tray_mount_hole_x, tray_mount_hole_x],
            z_offset = tray_mount_hole_z_offsets
        ) {
            z = tray_bottom_z + z_offset;

            // M4 clearance hole through the PETG backplate.
            translate([x, tray_near_y + 1, z])
                rotate([90, 0, 0])
                    cylinder(
                        h = tray_mount_plate_thickness + 2,
                        d = tray_fastener_clearance_diameter
                    );

            // Rear-opening captive pocket for the supplied M4 locknut.
            translate([x, backplate_y - 0.1, z])
                rotate([-90, 0, 0])
                    hex_prism(
                        tray_nut_pocket_across_flats,
                        tray_nut_pocket_depth + 0.1,
                        tray_nut_pocket_rotation
                    );
        }
    }
}

module clamp_to_mount_bridge() {
    // Broad saddle plus two ribs transfer tray torque into the clamp.
    hull() {
        translate([
            -clamp_width / 2,
            -7,
            clamp_outer_radius - 3
        ])
            cube([clamp_width, 14, 4]);

        translate([
            -clamp_width / 2,
            tray_near_y + 5,
            tray_bottom_z - tray_mount_shelf_thickness
        ])
            cube([clamp_width, 18, tray_mount_shelf_thickness]);
    }

    for (x = [-clamp_width / 2, clamp_width / 2 - 4]) {
        hull() {
            translate([x, 4, clamp_outer_radius - 1])
                cube([4, 6, 4]);
            translate([x, tray_near_y + 28, tray_bottom_z])
                translate([0, 0, -tray_mount_shelf_thickness])
                    cube([4, 6, tray_mount_shelf_thickness]);
        }
    }
}

module upper_mount() {
    union() {
        upper_saddle();
        upper_hinge();
        upper_latch();
        clamp_to_mount_bridge();
        tray_mount_bracket();
    }
}

module upper_fit_test() {
    union() {
        upper_saddle();
        upper_hinge();
        upper_latch();
    }
}

module lower_clamp() {
    union() {
        lower_saddle();
        lower_hinge();
        lower_latch();
    }
}

// The installed clamp axis is X. Standing a single clamp part on its +X end
// converts the annular end face into a broad, coplanar bed footprint while
// leaving the rail channel and M6 hinge bore vertical. The previous exports
// retained assembly orientation and touched the plate only at curved tangent
// surfaces, which caused the 2026-08-10 fit print to detach at layer 37.
module orient_clamp_end_on_bed() {
    translate([0, 0, clamp_width / 2])
        rotate([0, 90, 0])
            children();
}

// The full upper is wider than the clamp because of its 72 mm tray backplate.
// Stand it on the backplate's +X side instead of forcing the clamp end through
// the plate. This preserves the strong end-on layer direction, provides about
// 421 mm2 of planar contact, and leaves the hinge bore vertical.
module orient_mount_side_on_bed() {
    translate([0, 0, tray_mount_width / 2])
        rotate([0, 90, 0])
            children();
}

module left_handed_upper() {
    mirror([0, 1, 0]) upper_mount();
}

module left_handed_lower() {
    mirror([0, 1, 0]) lower_clamp();
}

module left_handed_fit_test() {
    mirror([0, 1, 0]) upper_fit_test();
}

module installed_latch_hardware() {
    upper_top_z = split_gap / 2 + latch_upper_height;
    lower_bottom_z = -split_gap / 2 - latch_lower_height;
    bolt_under_head_z = upper_top_z + latch_washer_thickness;

    // Bolt shaft.
    translate([0, latch_bolt_y, bolt_under_head_z])
        rotate([180, 0, 0])
            cylinder(h = latch_bolt_length, d = latch_bolt_diameter);

    // Top washer.
    translate([0, latch_bolt_y, upper_top_z])
        difference() {
            cylinder(
                h = latch_washer_thickness,
                d = latch_washer_outer_diameter
            );
            translate([0, 0, -0.1])
                cylinder(
                    h = latch_washer_thickness + 0.2,
                    d = latch_bolt_clearance_diameter
                );
        }

    // Hex bolt head.
    translate([0, latch_bolt_y, bolt_under_head_z])
        hex_prism(
            latch_bolt_head_across_flats,
            latch_bolt_head_height
        );

    // Captive M6 nylon-insert locknut seated in the bottom pocket.
    translate([0, latch_bolt_y, lower_bottom_z])
        hex_prism(latch_nut_across_flats, latch_nut_thickness);
}

module installed_hinge_hardware() {
    hinge_left_x = -clamp_width / 2;
    hinge_right_x = clamp_width / 2;
    bolt_under_head_x = hinge_left_x - hinge_washer_thickness;

    // Bolt shaft.
    translate([bolt_under_head_x, hinge_y, 0])
        rotate([0, 90, 0])
            cylinder(h = hinge_bolt_length, d = hinge_bolt_diameter);

    // Washer under the bolt head.
    translate([hinge_left_x - hinge_washer_thickness, hinge_y, 0])
        rotate([0, 90, 0])
            difference() {
                cylinder(
                    h = hinge_washer_thickness,
                    d = hinge_washer_outer_diameter
                );
                translate([0, 0, -0.1])
                    cylinder(
                        h = hinge_washer_thickness + 0.2,
                        d = hinge_hole_diameter
                    );
            }

    // Hex bolt head.
    translate([bolt_under_head_x, hinge_y, 0])
        rotate([0, -90, 0])
            hex_prism(
                hinge_bolt_head_across_flats,
                hinge_bolt_head_height
            );

    // Washer and nylon-insert nut on the removable end.
    translate([hinge_right_x, hinge_y, 0])
        rotate([0, 90, 0])
            difference() {
                cylinder(
                    h = hinge_washer_thickness,
                    d = hinge_washer_outer_diameter
                );
                translate([0, 0, -0.1])
                    cylinder(
                        h = hinge_washer_thickness + 0.2,
                        d = hinge_hole_diameter
                    );
            }

    translate([hinge_right_x + hinge_washer_thickness, hinge_y, 0])
        rotate([0, 90, 0])
            hex_prism(hinge_nut_across_flats, hinge_nut_thickness);
}

module installed_tray_hardware() {
    tray_inner_face_y = tray_near_y + tray_mount_pad_thickness;
    bolt_under_head_y =
        tray_inner_face_y - tray_fastener_head_recess_depth;
    backplate_y = tray_near_y - tray_mount_plate_thickness;

    for (
        x = [-tray_mount_hole_x, tray_mount_hole_x],
        z_offset = tray_mount_hole_z_offsets
    ) {
        z = tray_bottom_z + z_offset;

        // M4 screw shaft points from inside the PLA tray into the PETG mount.
        translate([x, bolt_under_head_y, z])
            rotate([90, 0, 0])
                cylinder(
                    h = tray_fastener_length,
                    d = tray_fastener_diameter
                );

        // Recessed Phillips pan head, accessible from inside the tray.
        translate([x, bolt_under_head_y, z])
            rotate([-90, 0, 0])
                pan_head(
                    tray_fastener_head_diameter,
                    tray_fastener_head_height
                );

        // Captive M4 nylon-insert locknut loaded from the rear.
        translate([x, backplate_y, z])
            rotate([-90, 0, 0])
                hex_prism(
                    tray_nut_across_flats,
                    tray_nut_thickness,
                    tray_nut_pocket_rotation
                );
    }
}

module reference_rail() {
    rotate([0, 90, 0])
        cylinder(
            h = tray_length + 80,
            r = effective_rail_diameter / 2,
            center = true
        );
}

if (part == "assembly" || part == "assembly-right") {
    %color([0.12, 0.12, 0.12, 0.55]) reference_rail();
    color("#E7B64A") upper_mount();
    color("#4E6A78") lower_clamp();
    color("#30343B") pla_tray();
    color("#D8D8D8") installed_latch_hardware();
    color("#8AA3B0") installed_hinge_hardware();
    color("#D8D8D8") installed_tray_hardware();
} else if (part == "assembly-left") {
    %color([0.12, 0.12, 0.12, 0.55]) reference_rail();
    color("#E7B64A") left_handed_upper();
    color("#4E6A78") left_handed_lower();
    color("#30343B") mirror([0, 1, 0]) pla_tray();
    color("#D8D8D8") mirror([0, 1, 0]) installed_latch_hardware();
    color("#8AA3B0") mirror([0, 1, 0]) installed_hinge_hardware();
    color("#D8D8D8") mirror([0, 1, 0]) installed_tray_hardware();
} else if (part == "fit-assembly-right") {
    %color([0.12, 0.12, 0.12, 0.35]) reference_rail();
    color("#E7B64A") upper_fit_test();
    color("#4E6A78") lower_clamp();
    color("#D8D8D8") installed_latch_hardware();
    color("#8AA3B0") installed_hinge_hardware();
} else if (part == "upper-right") {
    orient_mount_side_on_bed() upper_mount();
} else if (part == "upper-left") {
    orient_mount_side_on_bed()
        mirror([0, 1, 0]) upper_mount();
} else if (part == "upper-right-assembly") {
    upper_mount();
} else if (part == "upper-left-assembly") {
    left_handed_upper();
} else if (part == "lower" || part == "lower-right") {
    orient_clamp_end_on_bed() lower_clamp();
} else if (part == "lower-left") {
    orient_clamp_end_on_bed()
        mirror([0, 1, 0]) lower_clamp();
} else if (part == "fit-upper-right") {
    orient_clamp_end_on_bed() upper_fit_test();
} else if (part == "fit-upper-left") {
    orient_clamp_end_on_bed()
        mirror([0, 1, 0]) upper_fit_test();
} else if (part == "lower-right-assembly") {
    lower_clamp();
} else if (part == "lower-left-assembly") {
    left_handed_lower();
} else if (part == "fit-upper-right-assembly") {
    upper_fit_test();
} else if (part == "fit-upper-left-assembly") {
    left_handed_fit_test();
} else if (part == "tray-pla") {
    pla_tray();
} else if (part == "hardware-fit-gauge") {
    hardware_fit_gauge();
} else {
    assert(false, str("Unknown part: ", part));
}
