from __future__ import annotations

# Example model for a newly initialized vibe-cadding project.
# Replace this file with the real project model once the initial viewer is running.

import math

import cadquery as cq

from vibecad import cached_part, parameter


PREVIEW_ONLY_PARAMS = {"theta"}

teeth = parameter(24, 12, 40, 1, "Teeth")
module = parameter(2.4, 1.2, 4.0, 0.1, "Gear module")
gear_thickness = parameter(7.0, 3.0, 14.0, 0.25, "Gear thickness")
plate_thickness = parameter(4.0, 2.0, 8.0, 0.25, "Plate thickness")
gear_clearance = parameter(0.45, 0.15, 1.2, 0.05, "Running clearance")
shaft_radius = parameter(4.0, 2.0, 7.0, 0.1, "Shaft radius")
cap_radius = parameter(6.4, 4.0, 10.0, 0.1, "Cap radius")
cap_thickness = parameter(2.6, 1.0, 5.0, 0.1, "Cap thickness")
theta = parameter(0.0, 0.0, 360.0, 5.0, "Theta")


def build(
    teeth: float,
    module: float,
    gear_thickness: float,
    plate_thickness: float,
    gear_clearance: float,
    shaft_radius: float,
    cap_radius: float,
    cap_thickness: float,
    theta: float,
) -> None:
    layout = _layout(teeth, module, plate_thickness, gear_clearance, gear_thickness)

    plate(layout["plate_length"], layout["plate_width"], plate_thickness, shaft_radius, layout["left_x"], layout["right_x"])
    shafts(plate_thickness, gear_thickness, gear_clearance, shaft_radius, layout["left_x"], layout["right_x"])
    involute_gear(
        "left",
        layout["tooth_count"],
        module,
        gear_thickness,
        shaft_radius + gear_clearance,
        layout["left_x"],
        layout["gear_z"],
        0.0,
    )
    involute_gear(
        "right",
        layout["tooth_count"],
        module,
        gear_thickness,
        shaft_radius + gear_clearance,
        layout["right_x"],
        layout["gear_z"],
        _mesh_phase_degrees(layout["tooth_count"]),
    )
    retaining_caps(cap_radius, cap_thickness, shaft_radius, layout["left_x"], layout["right_x"], layout["cap_z"])


def preview(
    teeth: float,
    module: float,
    gear_thickness: float,
    plate_thickness: float,
    gear_clearance: float,
    shaft_radius: float,
    cap_radius: float,
    cap_thickness: float,
    theta: float,
) -> dict[str, list[float]]:
    layout = _layout(teeth, module, plate_thickness, gear_clearance, gear_thickness)
    return {
        "left red gear": _rotate_z_matrix(theta, layout["left_x"], 0),
        "right blue gear": _rotate_z_matrix(-theta, layout["right_x"], 0),
    }


@cached_part("base plate", (0.18, 0.44, 0.54))
def plate(
    length: float,
    width: float,
    thickness: float,
    shaft_radius: float,
    left_x: float,
    right_x: float,
) -> cq.Workplane:
    corner_radius = min(5.0, width / 9)
    base = (
        cq.Workplane("XY")
        .rect(length - corner_radius * 2, width)
        .extrude(thickness)
        .translate((0, 0, -thickness / 2))
    )
    rounded_ends = (
        cq.Workplane("XY")
        .pushPoints([(-length / 2 + corner_radius, 0), (length / 2 - corner_radius, 0)])
        .circle(width / 2)
        .extrude(thickness)
        .translate((0, 0, -thickness / 2))
    )
    base = base.union(rounded_ends)
    screw_holes = [(-length * 0.4, -width * 0.34), (-length * 0.4, width * 0.34), (length * 0.4, -width * 0.34), (length * 0.4, width * 0.34)]
    base = base.faces(">Z").workplane().pushPoints(screw_holes).hole(3.2)
    return base.faces(">Z").workplane().pushPoints([(left_x, 0), (right_x, 0)]).circle(shaft_radius * 1.25).extrude(1.0)


@cached_part("fixed shafts", (0.42, 0.42, 0.40))
def shafts(
    plate_thickness: float,
    gear_thickness: float,
    gear_clearance: float,
    shaft_radius: float,
    left_x: float,
    right_x: float,
) -> cq.Workplane:
    height = plate_thickness + gear_thickness + gear_clearance * 2
    z = -plate_thickness / 2 + height / 2
    return (
        cq.Workplane("XY")
        .pushPoints([(left_x, 0), (right_x, 0)])
        .circle(shaft_radius)
        .extrude(height)
        .translate((0, 0, z - height / 2))
    )


@cached_part("left red gear", (0.84, 0.12, 0.13))
def _left_gear(
    teeth: int,
    module: float,
    thickness: float,
    bore_radius: float,
    x: float,
    z: float,
    rotation_deg: float,
) -> cq.Workplane:
    return _gear_body(teeth, module, thickness, bore_radius, x, z, rotation_deg)


@cached_part("right blue gear", (0.13, 0.30, 0.82))
def _right_gear(
    teeth: int,
    module: float,
    thickness: float,
    bore_radius: float,
    x: float,
    z: float,
    rotation_deg: float,
) -> cq.Workplane:
    return _gear_body(teeth, module, thickness, bore_radius, x, z, rotation_deg)


def involute_gear(
    side: str,
    teeth: int,
    module: float,
    thickness: float,
    bore_radius: float,
    x: float,
    z: float,
    rotation_deg: float,
) -> cq.Workplane:
    if side == "left":
        return _left_gear(teeth, module, thickness, bore_radius, x, z, rotation_deg)
    return _right_gear(teeth, module, thickness, bore_radius, x, z, rotation_deg)


@cached_part("retaining caps", (0.90, 0.70, 0.20))
def retaining_caps(
    cap_radius: float,
    cap_thickness: float,
    shaft_radius: float,
    left_x: float,
    right_x: float,
    z: float,
) -> cq.Workplane:
    cap = (
        cq.Workplane("XY")
        .pushPoints([(left_x, 0), (right_x, 0)])
        .circle(cap_radius)
        .extrude(cap_thickness)
        .translate((0, 0, z))
    )
    return cap.faces(">Z").workplane().pushPoints([(left_x, 0), (right_x, 0)]).hole(shaft_radius * 0.55, depth=cap_thickness * 0.7)


def _gear_body(
    teeth: int,
    module: float,
    thickness: float,
    bore_radius: float,
    x: float,
    z: float,
    rotation_deg: float,
) -> cq.Workplane:
    points = _involute_points(teeth, module)
    body = cq.Workplane("XY").polyline(points).close().extrude(thickness)
    body = body.faces(">Z").workplane().circle(bore_radius).cutThruAll()
    body = body.faces(">Z").workplane().circle(bore_radius * 1.55).cutBlind(-thickness * 0.18)
    body = body.faces("<Z").workplane().circle(bore_radius * 1.55).cutBlind(-thickness * 0.18)
    return body.rotate((0, 0, 0), (0, 0, 1), rotation_deg).translate((x, 0, z))


def _layout(
    teeth: float,
    module: float,
    plate_thickness: float,
    gear_clearance: float,
    gear_thickness: float,
) -> dict[str, float]:
    tooth_count = max(8, int(round(teeth)))
    pitch_radius = module * tooth_count / 2
    outer_radius = pitch_radius + module
    center_distance = pitch_radius * 2 + gear_clearance * 1.8
    return {
        "tooth_count": tooth_count,
        "left_x": -center_distance / 2,
        "right_x": center_distance / 2,
        "plate_length": center_distance + outer_radius * 2 + 20,
        "plate_width": outer_radius * 2 + 18,
        "gear_z": plate_thickness / 2 + gear_clearance,
        "cap_z": plate_thickness / 2 + gear_clearance + gear_thickness + gear_clearance,
    }


def _mesh_phase_degrees(tooth_count: int) -> float:
    tooth_pitch_degrees = 360.0 / tooth_count
    if tooth_count % 2 == 0:
        return tooth_pitch_degrees / 2
    return 0.0


def _rotate_z_matrix(angle_deg: float, origin_x: float, origin_y: float) -> list[float]:
    angle = math.radians(angle_deg)
    c = math.cos(angle)
    s = math.sin(angle)
    tx = origin_x - c * origin_x + s * origin_y
    ty = origin_y - s * origin_x - c * origin_y
    return [
        c,
        -s,
        0,
        tx,
        s,
        c,
        0,
        ty,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        1,
    ]


def _involute_points(teeth: int, module: float) -> list[tuple[float, float]]:
    pressure_angle = math.radians(20.0)
    pitch_radius = module * teeth / 2
    outer_radius = pitch_radius + module
    root_radius = max(pitch_radius - module * 1.25, module * 2.5)
    base_radius = pitch_radius * math.cos(pressure_angle)
    tooth_angle = 2 * math.pi / teeth
    half_tooth_at_pitch = tooth_angle / 4
    involute_at_pitch = math.tan(pressure_angle) - pressure_angle
    flank_steps = 8
    tip_steps = 3
    root_steps = 4

    def involute_angle(radius: float) -> float:
        t = math.sqrt(max((radius / base_radius) ** 2 - 1, 0))
        return t - math.atan(t)

    def left_flank_angle(center: float, radius: float) -> float:
        return center - half_tooth_at_pitch + (involute_angle(radius) - involute_at_pitch)

    def right_flank_angle(center: float, radius: float) -> float:
        return center + half_tooth_at_pitch - (involute_angle(radius) - involute_at_pitch)

    points: list[tuple[float, float]] = []
    for index in range(teeth):
        center = index * tooth_angle
        next_center = (index + 1) * tooth_angle
        left_base_angle = left_flank_angle(center, base_radius)
        right_base_angle = right_flank_angle(center, base_radius)
        left_outer_angle = left_flank_angle(center, outer_radius)
        right_outer_angle = right_flank_angle(center, outer_radius)
        next_left_base_angle = left_flank_angle(next_center, base_radius)

        points.append(_polar_point(root_radius, left_base_angle))
        points.append(_polar_point(base_radius, left_base_angle))

        for step in range(1, flank_steps + 1):
            radius = base_radius + (outer_radius - base_radius) * step / flank_steps
            points.append(_polar_point(radius, left_flank_angle(center, radius)))

        for step in range(1, tip_steps + 1):
            angle = left_outer_angle + (right_outer_angle - left_outer_angle) * step / tip_steps
            points.append(_polar_point(outer_radius, angle))

        for step in range(flank_steps - 1, -1, -1):
            radius = base_radius + (outer_radius - base_radius) * step / flank_steps
            points.append(_polar_point(radius, right_flank_angle(center, radius)))

        points.append(_polar_point(root_radius, right_base_angle))

        root_span = next_left_base_angle - right_base_angle
        for step in range(1, root_steps):
            angle = right_base_angle + root_span * step / root_steps
            points.append(_polar_point(root_radius, angle))
    return points


def _polar_point(radius: float, angle: float) -> tuple[float, float]:
    return (math.cos(angle) * radius, math.sin(angle) * radius)
