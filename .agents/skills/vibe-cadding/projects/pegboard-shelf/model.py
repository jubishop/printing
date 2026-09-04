from __future__ import annotations

import cadquery as cq

from vibecad import cached_part, parameter


SHELF_COLOR = (0.95, 0.66, 0.10)
RIM_COLOR = (0.88, 0.45, 0.08)
BACKWALL_COLOR = (0.82, 0.24, 0.08)
PEG_COLOR = (0.12, 0.48, 0.82)
BOARD_COLOR = (0.66, 0.47, 0.27)


shelf_depth = parameter(100.0, 60.0, 160.0, 1.0, "Shelf depth (mm)")
lip_height = parameter(12.0, 5.0, 30.0, 1.0, "Retaining lip height (mm)")
side_overhang = parameter(5.0, 2.0, 20.0, 0.5, "Side overhang past pegs (mm)")
deck_thickness = parameter(8.0, 6.0, 12.0, 0.5, "Deck thickness (mm)")
lip_thickness = parameter(3.2, 2.0, 6.0, 0.2, "Front and side lip thickness (mm)")
front_corner_radius = parameter(12.0, 4.0, 25.0, 1.0, "Front corner radius (mm)")
lower_side_radius = parameter(3.0, 1.0, 4.0, 0.5, "Lower perimeter radius (mm)")
center_backwall_height = parameter(25.0, 12.0, 48.0, 1.0, "Center backwall height (mm)")


def build(
    shelf_depth: float,
    lip_height: float,
    side_overhang: float,
    deck_thickness: float,
    lip_thickness: float,
    front_corner_radius: float,
    lower_side_radius: float,
    center_backwall_height: float,
) -> None:
    peg_diameter = 32.0
    peg_length = 39.0
    peg_wall = 2.4
    peg_tip_chamfer = 1.0
    flange_diameter = 42.0
    flange_thickness = 8.0
    flange_edge_chamfer = 0.8
    peg_center_spacing = 178.5
    hole_bottom_to_board_edge = 17.0
    backwall_thickness = 8.0
    board_width = 280.0
    board_height = 110.0
    board_hole_clearance = 0.4

    shelf_width = peg_center_spacing + peg_diameter + 2 * side_overhang
    peg_center_height = -deck_thickness + hole_bottom_to_board_edge + peg_diameter / 2
    bridge_height = min(center_backwall_height, peg_center_height)

    deck(
        shelf_width,
        shelf_depth,
        deck_thickness,
        front_corner_radius,
        lower_side_radius,
    )
    retaining_rim(
        shelf_width,
        shelf_depth,
        deck_thickness,
        lip_height,
        lip_thickness,
        backwall_thickness,
        front_corner_radius,
        lower_side_radius,
    )
    raised_center_backwall(
        peg_center_spacing,
        bridge_height,
        backwall_thickness,
    )
    left_peg(
        -peg_center_spacing / 2,
        peg_center_height,
        peg_diameter,
        peg_length,
        peg_wall,
        peg_tip_chamfer,
        flange_diameter,
        flange_thickness,
        flange_edge_chamfer,
    )
    right_peg(
        peg_center_spacing / 2,
        peg_center_height,
        peg_diameter,
        peg_length,
        peg_wall,
        peg_tip_chamfer,
        flange_diameter,
        flange_thickness,
        flange_edge_chamfer,
    )
    reference_pegboard_not_printable(
        board_width,
        board_height,
        peg_length,
        deck_thickness,
        peg_center_spacing,
        peg_center_height,
        peg_diameter + board_hole_clearance,
    )


def _rounded_front_prism(
    width: float,
    depth: float,
    height: float,
    z_min: float,
    radius: float,
    y_offset: float = 0.0,
) -> cq.Workplane:
    rear = (
        cq.Workplane("XY")
        .box(width, depth - radius, height)
        .translate((0, y_offset + (depth - radius) / 2, z_min + height / 2))
    )
    front_center = (
        cq.Workplane("XY")
        .box(width - 2 * radius, radius, height)
        .translate((0, y_offset + depth - radius / 2, z_min + height / 2))
    )
    corners = (
        cq.Workplane("XY")
        .pushPoints(
            [
                (-width / 2 + radius, y_offset + depth - radius),
                (width / 2 - radius, y_offset + depth - radius),
            ]
        )
        .circle(radius)
        .extrude(height)
        .translate((0, 0, z_min))
    )
    return rear.union(front_center).union(corners)


@cached_part("rounded shelf deck", SHELF_COLOR)
def deck(
    width: float,
    depth: float,
    thickness: float,
    corner_radius: float,
    lower_edge_radius: float,
) -> cq.Workplane:
    deck_solid = _rounded_front_prism(
        width,
        depth,
        thickness,
        -thickness,
        corner_radius,
    )
    exposed_bottom_edges = deck_solid.edges("<Z").filter(
        lambda edge: edge.Center().y > 1e-6
    )
    return exposed_bottom_edges.fillet(lower_edge_radius)


@cached_part("rounded 12 mm retaining rim", RIM_COLOR)
def retaining_rim(
    width: float,
    depth: float,
    deck_thickness: float,
    height: float,
    side_thickness: float,
    rear_thickness: float,
    corner_radius: float,
    lower_edge_radius: float,
) -> cq.Workplane:
    outer = _rounded_front_prism(
        width,
        depth,
        height,
        0.0,
        corner_radius,
    )
    inner = _rounded_front_prism(
        width - 2 * side_thickness,
        depth - rear_thickness - side_thickness,
        height + 0.2,
        -0.1,
        corner_radius - side_thickness,
        rear_thickness,
    )
    rounded_rim = outer.cut(inner)
    lower_rear = (
        cq.Workplane("XY")
        .box(width, rear_thickness, deck_thickness)
        .translate((0, rear_thickness / 2, -deck_thickness / 2))
    )
    rounded_lower_rear = lower_rear.edges("|Y and <Z").fillet(
        lower_edge_radius
    )
    return rounded_rim.union(rounded_lower_rear)


@cached_part("raised center backwall", BACKWALL_COLOR)
def raised_center_backwall(
    width: float,
    height_above_deck: float,
    thickness: float,
) -> cq.Workplane:
    return (
        cq.Workplane("XY")
        .box(width, thickness, height_above_deck)
        .translate((0, thickness / 2, height_above_deck / 2))
    )


@cached_part("left fitted peg", PEG_COLOR)
def left_peg(
    x: float,
    z: float,
    diameter: float,
    length: float,
    wall: float,
    tip_chamfer: float,
    flange_diameter: float,
    flange_thickness: float,
    flange_edge_chamfer: float,
) -> cq.Workplane:
    return _fitted_peg(
        x,
        z,
        diameter,
        length,
        wall,
        tip_chamfer,
        flange_diameter,
        flange_thickness,
        flange_edge_chamfer,
    )


@cached_part("right fitted peg", PEG_COLOR)
def right_peg(
    x: float,
    z: float,
    diameter: float,
    length: float,
    wall: float,
    tip_chamfer: float,
    flange_diameter: float,
    flange_thickness: float,
    flange_edge_chamfer: float,
) -> cq.Workplane:
    return _fitted_peg(
        x,
        z,
        diameter,
        length,
        wall,
        tip_chamfer,
        flange_diameter,
        flange_thickness,
        flange_edge_chamfer,
    )


def _fitted_peg(
    x: float,
    z: float,
    diameter: float,
    length: float,
    wall: float,
    tip_chamfer: float,
    flange_diameter: float,
    flange_thickness: float,
    flange_edge_chamfer: float,
) -> cq.Workplane:
    negative_y = cq.Vector(0, -1, 0)
    positive_y = cq.Vector(0, 1, 0)
    center = cq.Vector(x, 0, z)
    outer_radius = diameter / 2
    inner_radius = outer_radius - wall
    tip_radius = outer_radius - tip_chamfer
    body_overlap = 0.1

    body = cq.Solid.makeCylinder(
        outer_radius,
        length - tip_chamfer + body_overlap,
        cq.Vector(x, body_overlap, z),
        negative_y,
    )
    tip = cq.Solid.makeCone(
        outer_radius,
        tip_radius,
        tip_chamfer,
        cq.Vector(x, -(length - tip_chamfer), z),
        negative_y,
    )
    inner = cq.Solid.makeCylinder(
        inner_radius,
        length + 0.01,
        center,
        negative_y,
    )
    tube = body.fuse(tip).cut(inner)

    flange_radius = flange_diameter / 2
    chamfered_radius = flange_radius - flange_edge_chamfer
    near_edge = cq.Solid.makeCone(
        chamfered_radius,
        flange_radius,
        flange_edge_chamfer,
        center,
        positive_y,
    )
    flange_middle = cq.Solid.makeCylinder(
        flange_radius,
        flange_thickness - 2 * flange_edge_chamfer,
        cq.Vector(x, flange_edge_chamfer, z),
        positive_y,
    )
    far_edge = cq.Solid.makeCone(
        flange_radius,
        chamfered_radius,
        flange_edge_chamfer,
        cq.Vector(x, flange_thickness - flange_edge_chamfer, z),
        positive_y,
    )
    flange = near_edge.fuse(flange_middle).fuse(far_edge)
    return cq.Workplane("XY").newObject([flange.fuse(tube)])


@cached_part("reference pegboard - not printable", BOARD_COLOR)
def reference_pegboard_not_printable(
    width: float,
    height: float,
    depth: float,
    shelf_bottom_z: float,
    peg_center_spacing: float,
    peg_center_z: float,
    hole_diameter: float,
) -> cq.Workplane:
    board = (
        cq.Workplane("XY")
        .box(width, depth, height)
        .translate((0, -depth / 2, -shelf_bottom_z + height / 2))
    )
    holes = (
        cq.Workplane("XZ", origin=(0, 0.1, 0))
        .pushPoints(
            [
                (-peg_center_spacing / 2, peg_center_z),
                (peg_center_spacing / 2, peg_center_z),
            ]
        )
        .circle(hole_diameter / 2)
        .extrude(depth + 0.2)
    )
    return board.cut(holes)
