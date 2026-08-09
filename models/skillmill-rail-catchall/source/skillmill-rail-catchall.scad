// Skillmill rail catch-all tray
// Original parametric design. Dimensions are millimetres.

// Select one export at a time:
// "assembly-right", "assembly-left", "upper-right", "upper-left",
// "lower-right", "lower-left", "fit-upper-right", "fit-upper-left",
// "clamp-screw", or "hinge-pin"
part = "assembly-right";

// Choose either input mode. Circumference is easiest with a fabric tape;
// diameter is useful for a known nominal tube size or when using calipers.
rail_measurement_mode = "diameter"; // [circumference, diameter]
rail_circumference = 125.0;
rail_diameter = 40.0;

effective_rail_diameter = rail_measurement_mode == "circumference"
    ? rail_circumference / 3.141592653589793
    : rail_diameter;

assert(
    rail_measurement_mode == "circumference"
        || rail_measurement_mode == "diameter",
    "rail_measurement_mode must be circumference or diameter."
);

// Space for a soft, non-marking liner between the printed clamp and rail.
liner_thickness = 0.8;
radial_fit_clearance = 0.25;

clamp_width = 32;
clamp_wall = 6;
split_gap = 1.6; // closing travel available at the threaded latch

tray_length = 155;
tray_depth = 85;
tray_height = 28;
tray_floor = 3.2;
tray_wall = 2.8;
tray_corner_radius = 9;

hinge_pin_shaft_diameter = 5.0;
hinge_hole_diameter = 5.5;
hinge_pin_head_diameter = 9.0;
hinge_pin_head_height = 2.4;
hinge_pin_barb_diameter = 6.1;
hinge_pin_barb_length = 3.2;
hinge_pin_split_width = 1.2;

latch_thread_major_diameter = 12.0;
latch_thread_pitch = 3.0;
latch_thread_depth = 1.2;
latch_thread_radial_clearance = 0.40;
latch_screw_diameter_scale = 0.94;
latch_upper_height = 10;
latch_lower_height = 13;
latch_lug_width = 24;
latch_lug_length = 28;
latch_screw_knob_diameter = 24;
latch_screw_knob_height = 8;
latch_screw_thread_length = 28;
latch_screw_tip_length = 2;

female_thread_start_z = -split_gap / 2 + 1;
screw_thread_start_z = split_gap / 2 + latch_upper_height;
thread_phase_turns =
    (screw_thread_start_z - female_thread_start_z) / latch_thread_pitch;
latch_screw_assembly_rotation =
    360 * (1 - (thread_phase_turns - floor(thread_phase_turns)));

$fn = 96;

clamp_inner_radius =
    effective_rail_diameter / 2 + liner_thickness + radial_fit_clearance;
clamp_outer_radius = clamp_inner_radius + clamp_wall;

hinge_barrel_radius = 5.5;
hinge_y = clamp_outer_radius + hinge_barrel_radius + 1.5;
hinge_center_knuckle = 12;
hinge_knuckle_gap = 0.7;
hinge_outer_knuckle =
    (clamp_width - hinge_center_knuckle - 2 * hinge_knuckle_gap) / 2;

latch_screw_y = -clamp_outer_radius - 14;

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

module coarse_external_thread(
    major_diameter,
    pitch,
    length,
    thread_depth,
    flank_fraction = 0.32
) {
    core_radius = major_diameter / 2 - thread_depth;
    slices_per_turn = 32;

    union() {
        cylinder(h = length, r = core_radius);

        linear_extrude(
            height = length,
            twist = -360 * length / pitch,
            slices = ceil(length / pitch * slices_per_turn),
            convexity = 16
        )
            translate([core_radius - 0.02, 0])
                polygon(points = [
                    [0, -pitch * flank_fraction],
                    [thread_depth + 0.04, 0],
                    [0, pitch * flank_fraction]
                ]);
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

        translate([0, latch_screw_y, split_gap / 2 - 1])
            cylinder(
                h = latch_upper_height + 2,
                d = latch_thread_major_diameter + 1.0
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

        // Female thread follows the installed, downward-facing screw.
        translate([
            0,
            latch_screw_y,
            -split_gap / 2 + 1
        ])
            rotate([180, 0, 0])
                coarse_external_thread(
                    latch_thread_major_diameter
                        + 2 * latch_thread_radial_clearance,
                    latch_thread_pitch,
                    latch_lower_height + 2,
                    latch_thread_depth,
                    0.36
                );

        // Lead-in chamfer helps the printed screw find the first thread.
        translate([
            0,
            latch_screw_y,
            -split_gap / 2 - 1.4
        ])
            cylinder(
                h = 1.5,
                d1 = latch_thread_major_diameter
                    - 2 * latch_thread_depth
                    + 2 * latch_thread_radial_clearance,
                d2 = latch_thread_major_diameter + 1.4
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

module clamp_to_tray_bridge() {
    // Broad saddle plus two ribs resist the tray's twisting load.
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
            tray_bottom_z
        ])
            cube([clamp_width, 18, tray_floor]);
    }

    for (x = [-clamp_width / 2, clamp_width / 2 - 4]) {
        hull() {
            translate([x, 4, clamp_outer_radius - 1])
                cube([4, 6, 4]);
            translate([x, tray_near_y + 28, tray_bottom_z])
                cube([4, 6, tray_floor]);
        }
    }
}

module upper_catchall() {
    union() {
        upper_saddle();
        upper_hinge();
        upper_latch();
        clamp_to_tray_bridge();
        tray_shell();
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

module left_handed_upper() {
    mirror([0, 1, 0]) upper_catchall();
}

module left_handed_lower() {
    mirror([0, 1, 0]) lower_clamp();
}

module left_handed_fit_test() {
    mirror([0, 1, 0]) upper_fit_test();
}

module clamp_screw() {
    screw_major_diameter =
        latch_thread_major_diameter * latch_screw_diameter_scale;
    core_diameter = screw_major_diameter - 2 * latch_thread_depth;

    union() {
        cylinder(
            h = latch_screw_knob_height,
            d = latch_screw_knob_diameter,
            $fn = 12
        );

        translate([0, 0, latch_screw_knob_height - 0.6])
            cylinder(h = 1.2, d = latch_thread_major_diameter + 4);

        translate([0, 0, latch_screw_knob_height])
            coarse_external_thread(
                screw_major_diameter,
                latch_thread_pitch,
                latch_screw_thread_length,
                latch_thread_depth
            );

        translate([
            0,
            0,
            latch_screw_knob_height + latch_screw_thread_length
        ])
            cylinder(
                h = latch_screw_tip_length,
                d1 = core_diameter,
                d2 = core_diameter * 0.65
            );
    }
}

module hinge_pin() {
    shaft_length = clamp_width + 1.0;

    difference() {
        union() {
            cylinder(
                h = hinge_pin_head_height,
                d = hinge_pin_head_diameter
            );

            translate([0, 0, hinge_pin_head_height - 0.1])
                cylinder(
                    h = shaft_length + 0.2,
                    d = hinge_pin_shaft_diameter
                );

            translate([0, 0, hinge_pin_head_height + shaft_length])
                cylinder(
                    h = hinge_pin_barb_length,
                    d1 = hinge_pin_barb_diameter,
                    d2 = hinge_pin_shaft_diameter * 0.75
                );
        }

        translate([
            -hinge_pin_split_width / 2,
            -hinge_pin_barb_diameter,
            hinge_pin_head_height + shaft_length - 5
        ])
            cube([
                hinge_pin_split_width,
                2 * hinge_pin_barb_diameter,
                hinge_pin_barb_length + 6
            ]);
    }
}

module installed_screw() {
    translate([
        0,
        latch_screw_y,
        split_gap / 2 + latch_upper_height + latch_screw_knob_height
    ])
        rotate([180, 0, 0])
            rotate([0, 0, latch_screw_assembly_rotation]) clamp_screw();
}

module installed_hinge_pin() {
    translate([
        -clamp_width / 2 - hinge_pin_head_height - 0.2,
        hinge_y,
        0
    ])
        rotate([0, 90, 0]) hinge_pin();
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
    color("#E7B64A") upper_catchall();
    color("#4E6A78") lower_clamp();
    color("#D8D8D8") installed_screw();
    color("#8AA3B0") installed_hinge_pin();
} else if (part == "assembly-left") {
    %color([0.12, 0.12, 0.12, 0.55]) reference_rail();
    color("#E7B64A") left_handed_upper();
    color("#4E6A78") left_handed_lower();
    color("#D8D8D8") mirror([0, 1, 0]) installed_screw();
    color("#8AA3B0") mirror([0, 1, 0]) installed_hinge_pin();
} else if (part == "upper-right") {
    upper_catchall();
} else if (part == "upper-left") {
    left_handed_upper();
} else if (part == "lower" || part == "lower-right") {
    lower_clamp();
} else if (part == "lower-left") {
    left_handed_lower();
} else if (part == "fit-upper-right") {
    upper_fit_test();
} else if (part == "fit-upper-left") {
    left_handed_fit_test();
} else if (part == "clamp-screw") {
    clamp_screw();
} else if (part == "hinge-pin") {
    hinge_pin();
} else if (part == "diagnostic-screw-lower") {
    intersection() {
        lower_clamp();
        installed_screw();
    }
} else if (part == "diagnostic-pin-clamp") {
    intersection() {
        union() {
            upper_catchall();
            lower_clamp();
        }
        installed_hinge_pin();
    }
} else {
    assert(false, str("Unknown part: ", part));
}
