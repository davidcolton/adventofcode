from collections import namedtuple

PathCoords = namedtuple("PathCoords", "x y dist")


def _get_max_direction(wire: list) -> int:
    max = 0
    for dir in wire:
        dist = int(dir[1:])
        max = dist if dist > max else max
    return max


def _move_up(path: dict, coords: PathCoords, length: str):
    start_x = coords.x
    start_y = coords.y
    dist = int(length[1:])
    for n in range(1, dist + 1):
        new_coords = PathCoords(start_x, start_y + n, abs(start_x) + abs(start_y + n))
        path.add(new_coords)
    return path, new_coords


def _move_down(path: set, coords: PathCoords, length: str):
    start_x = coords.x
    start_y = coords.y
    dist = int(length[1:])
    for n in range(1, dist + 1):
        new_coords = PathCoords(start_x, start_y - n, abs(start_x) + abs(start_y - n))
        path.add(new_coords)
    return path, new_coords


def _move_right(path: set, coords: PathCoords, length: str):
    start_x = coords.x
    start_y = coords.y
    dist = int(length[1:])
    for n in range(1, dist + 1):
        new_coords = PathCoords(start_x + n, start_y, abs(start_x + n) + abs(start_y))
        path.add(new_coords)
    return path, new_coords


def _move_left(path: set, coords: PathCoords, length: str):
    start_x = coords.x
    start_y = coords.y
    dist = int(length[1:])
    for n in range(1, dist + 1):
        new_coords = PathCoords(start_x - n, start_y, abs(start_x - n) + abs(start_y))
        path.add(new_coords)
    return path, new_coords


def _follow_path(coords: set, root: PathCoords, wire: list) -> set:
    steps_taken = 0
    for instruction in wire:
        if instruction.startswith("U"):
            coords, root = _move_up(coords, root, instruction)
        elif instruction.startswith("D"):
            coords, root = _move_down(coords, root, instruction)
        elif instruction.startswith("L"):
            coords, root = _move_left(coords, root, instruction)
        else:
            coords, root = _move_right(coords, root, instruction)
    return coords


def crossed_wires(wire_01: list, wire_02: list) -> int:

    root = PathCoords(0, 0, 0)

    coords_wire_01 = set()
    coords_wire_02 = set()

    wire_01_coords = _follow_path(coords_wire_01, root, wire_01)
    wire_02_coords = _follow_path(coords_wire_02, root, wire_02)

    intersetion_points = wire_01_coords.intersection(wire_02_coords)

    closest = min(intersetion_points, key=lambda x: x.dist)

    return closest.dist


with open("input.txt", "r") as f:
    lines = f.read().split("\n")

wire_01 = lines[0].split(",")
wire_02 = lines[1].split(",")

print((crossed_wires(wire_01, wire_02)))
