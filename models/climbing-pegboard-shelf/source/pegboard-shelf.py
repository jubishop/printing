# /// script
# requires-python = ">=3.11,<3.15"
# dependencies = ["cadquery==2.8.0"]
# ///
"""CadQuery model of the climbing pegboard shelf.

A CadQuery counterpart of the shelf in pegboard-shelf.scad. Dimensions are in
millimetres. Installed coordinates use X across the pegboard, Y out from the
wall, and Z up, with the deck's top surface at Z = 0.

Run it from the repository root; uv installs CadQuery on first use:

    uv run models/climbing-pegboard-shelf/source/pegboard-shelf.py /tmp/pegboard-shelf.stl

Pass --help to list the adjustable dimensions.
"""

from __future__ import annotations

import argparse

import cadquery as cq

# Adjustable dimensions: name, default, and description. The defaults are the
# printed shelf's.
DIMENSIONS = {
    "shelf_depth": (100.0, "depth from the pegboard contact plane to the front face"),
    "lip_height": (12.0, "retaining lip height above the deck"),
    "side_overhang": (5.0, "side overhang past the outside of each peg"),
    "deck_thickness": (8.0, "deck thickness"),
    "lip_thickness": (3.2, "front and side lip thickness"),
    "front_corner_radius": (12.0, "front corner plan radius"),
    "lower_side_radius": (3.0, "exposed lower perimeter radius"),
    "center_backwall_height": (
        25.0,
        "raised center backwall height above the deck, capped at the peg axes",
    ),
}

# Fixed dimensions: the proven peg fit and spacing, the measured hole height,
# and the rear lip; see the model README.
PEG_DIAMETER = 32.0
PEG_LENGTH = 39.0
PEG_WALL = 2.4
PEG_TIP_CHAMFER = 1.0
FLANGE_DIAMETER = 42.0
FLANGE_THICKNESS = 8.0
FLANGE_EDGE_CHAMFER = 0.8
PEG_CENTER_SPACING = 178.5
HOLE_BOTTOM_TO_BOARD_EDGE = 17.0
BACKWALL_THICKNESS = 8.0

# Non-printing reference pegboard for the installed preview.
BOARD_WIDTH = 280.0
BOARD_HEIGHT = 110.0
BOARD_HOLE_CLEARANCE = 0.4


def build(
    shelf_depth: float,
    lip_height: float,
    side_overhang: float,
    deck_thickness: float,
    lip_thickness: float,
    front_corner_radius: float,
    lower_side_radius: float,
    center_backwall_height: float,
) -> tuple[cq.Workplane, cq.Workplane]:
    """Return the printable shelf and the reference pegboard."""
    shelf_width = PEG_CENTER_SPACING + PEG_DIAMETER + 2 * side_overhang
    peg_center_height = -deck_thickness + HOLE_BOTTOM_TO_BOARD_EDGE + PEG_DIAMETER / 2
    backwall_height = min(center_backwall_height, peg_center_height)

    shelf = (
        deck(
            shelf_width,
            shelf_depth,
            deck_thickness,
            front_corner_radius,
            lower_side_radius,
        )
        .union(
            retaining_rim(
                shelf_width,
                shelf_depth,
                deck_thickness,
                lip_height,
                lip_thickness,
                front_corner_radius,
                lower_side_radius,
            )
        )
        .union(raised_center_backwall(backwall_height))
    )
    for x in (-PEG_CENTER_SPACING / 2, PEG_CENTER_SPACING / 2):
        shelf = shelf.union(fitted_peg(x, peg_center_height))
    return shelf, reference_pegboard(deck_thickness, peg_center_height)


def rounded_front_prism(
    width: float,
    depth: float,
    height: float,
    z_min: float,
    radius: float,
    y_offset: float = 0.0,
) -> cq.Workplane:
    """A box whose two front vertical edges are rounded in plan."""
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


def deck(
    width: float,
    depth: float,
    thickness: float,
    corner_radius: float,
    lower_edge_radius: float,
) -> cq.Workplane:
    """The deck, with every exposed lower edge rounded and the rear left flat."""
    deck_solid = rounded_front_prism(width, depth, thickness, -thickness, corner_radius)
    exposed_bottom_edges = deck_solid.edges("<Z").filter(
        lambda edge: edge.Center().y > 1e-6
    )
    return exposed_bottom_edges.fillet(lower_edge_radius)


def retaining_rim(
    width: float,
    depth: float,
    deck_thickness: float,
    height: float,
    side_thickness: float,
    corner_radius: float,
    lower_edge_radius: float,
) -> cq.Workplane:
    """The front and side lips, and the rear lip down to the shelf bottom."""
    outer = rounded_front_prism(width, depth, height, 0.0, corner_radius)
    inner = rounded_front_prism(
        width - 2 * side_thickness,
        depth - BACKWALL_THICKNESS - side_thickness,
        height + 0.2,
        -0.1,
        corner_radius - side_thickness,
        BACKWALL_THICKNESS,
    )
    lower_rear = (
        cq.Workplane("XY")
        .box(width, BACKWALL_THICKNESS, deck_thickness)
        .translate((0, BACKWALL_THICKNESS / 2, -deck_thickness / 2))
        .edges("|Y and <Z")
        .fillet(lower_edge_radius)
    )
    return outer.cut(inner).union(lower_rear)


def raised_center_backwall(height_above_deck: float) -> cq.Workplane:
    """The raised wall between the peg axes."""
    return (
        cq.Workplane("XY")
        .box(PEG_CENTER_SPACING, BACKWALL_THICKNESS, height_above_deck)
        .translate((0, BACKWALL_THICKNESS / 2, height_above_deck / 2))
    )


def fitted_peg(x: float, z: float) -> cq.Workplane:
    """A hollow peg with a chamfered tip, on a chamfered flange at the wall."""
    negative_y = cq.Vector(0, -1, 0)
    positive_y = cq.Vector(0, 1, 0)
    center = cq.Vector(x, 0, z)
    outer_radius = PEG_DIAMETER / 2
    body_overlap = 0.1

    body = cq.Solid.makeCylinder(
        outer_radius,
        PEG_LENGTH - PEG_TIP_CHAMFER + body_overlap,
        cq.Vector(x, body_overlap, z),
        negative_y,
    )
    tip = cq.Solid.makeCone(
        outer_radius,
        outer_radius - PEG_TIP_CHAMFER,
        PEG_TIP_CHAMFER,
        cq.Vector(x, -(PEG_LENGTH - PEG_TIP_CHAMFER), z),
        negative_y,
    )
    bore = cq.Solid.makeCylinder(
        outer_radius - PEG_WALL,
        PEG_LENGTH + 0.01,
        center,
        negative_y,
    )
    tube = body.fuse(tip).cut(bore)

    flange_radius = FLANGE_DIAMETER / 2
    chamfered_radius = flange_radius - FLANGE_EDGE_CHAMFER
    near_edge = cq.Solid.makeCone(
        chamfered_radius,
        flange_radius,
        FLANGE_EDGE_CHAMFER,
        center,
        positive_y,
    )
    flange_middle = cq.Solid.makeCylinder(
        flange_radius,
        FLANGE_THICKNESS - 2 * FLANGE_EDGE_CHAMFER,
        cq.Vector(x, FLANGE_EDGE_CHAMFER, z),
        positive_y,
    )
    far_edge = cq.Solid.makeCone(
        flange_radius,
        chamfered_radius,
        FLANGE_EDGE_CHAMFER,
        cq.Vector(x, FLANGE_THICKNESS - FLANGE_EDGE_CHAMFER, z),
        positive_y,
    )
    flange = near_edge.fuse(flange_middle).fuse(far_edge)
    return cq.Workplane("XY").newObject([flange.fuse(tube)])


def reference_pegboard(deck_thickness: float, peg_center_height: float) -> cq.Workplane:
    """The pegboard behind the wall plane, bottom edge level with the shelf's."""
    board = (
        cq.Workplane("XY")
        .box(BOARD_WIDTH, PEG_LENGTH, BOARD_HEIGHT)
        .translate((0, -PEG_LENGTH / 2, -deck_thickness + BOARD_HEIGHT / 2))
    )
    holes = (
        cq.Workplane("XZ", origin=(0, 0.1, 0))
        .pushPoints(
            [
                (-PEG_CENTER_SPACING / 2, peg_center_height),
                (PEG_CENTER_SPACING / 2, peg_center_height),
            ]
        )
        .circle((PEG_DIAMETER + BOARD_HOLE_CLEARANCE) / 2)
        .extrude(PEG_LENGTH + 0.2)
    )
    return board.cut(holes)


def main() -> None:
    parser = argparse.ArgumentParser(description="Export the climbing pegboard shelf as an STL.")
    parser.add_argument("output", help="STL file to write")
    parser.add_argument(
        "--part",
        choices=("shelf", "installed-preview"),
        default="shelf",
        help="the printable shelf, or the shelf with a non-printing reference pegboard",
    )
    for name, (default, description) in DIMENSIONS.items():
        parser.add_argument(
            "--" + name.replace("_", "-"),
            type=float,
            default=default,
            help=f"{description} (default: {default:g} mm)",
        )
    args = parser.parse_args()

    shelf, board = build(**{name: getattr(args, name) for name in DIMENSIONS})
    solids = shelf.solids().vals()
    if len(solids) != 1 or not solids[0].isValid():
        raise SystemExit("The shelf did not build as one valid solid.")
    shape = solids[0]
    if args.part == "installed-preview":
        shape = cq.Compound.makeCompound([shape, board.val()])
    cq.exporters.export(shape, args.output, exportType="STL", tolerance=0.02, angularTolerance=0.05)
    bounds = shape.BoundingBox()
    print(f"Wrote {args.output}: {bounds.xlen:.1f} x {bounds.ylen:.1f} x {bounds.zlen:.1f} mm")


if __name__ == "__main__":
    main()
