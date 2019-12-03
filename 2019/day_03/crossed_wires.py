from collections import namedtuple

PathCoords = namedtuple("PathCoords", "x y dist")


class WirePath:
    def __init__(self, path: list):
        self.root = PathCoords(0, 0, 0)
        self.current = PathCoords(0, 0, 0)
        self.path = path
        self.steps = 0

        self.wire_path_coords = set()
        self.steps_taken = dict()

    def move_up(self, length: str):
        x = self.current.x
        y = self.current.y
        moves = int(length[1:])
        for n in range(1, moves + 1):
            dist = abs(x) + abs(y + n)
            new_coords = PathCoords(x, y + n, dist)
            self.wire_path_coords.add(new_coords)
        self.current = new_coords

    def move_down(self, length: str):
        x = self.current.x
        y = self.current.y
        moves = int(length[1:])
        for n in range(1, moves + 1):
            dist = abs(x) + abs(y - n)
            new_coords = PathCoords(x, y - n, dist)
            self.wire_path_coords.add(new_coords)
        self.current = new_coords

    def move_right(self, length: str):
        x = self.current.x
        y = self.current.y
        moves = int(length[1:])
        for n in range(1, moves + 1):
            dist = abs(x + n) + abs(y)
            new_coords = PathCoords(x + n, y, dist)
            self.wire_path_coords.add(new_coords)
        self.current = new_coords

    def move_left(self, length: str):
        x = self.current.x
        y = self.current.y
        moves = int(length[1:])
        for n in range(1, moves + 1):
            dist = abs(x - n) + abs(y)
            new_coords = PathCoords(x - n, y, dist)
            self.wire_path_coords.add(new_coords)
        self.current = new_coords

    def follow_path(self) -> set:
        for instruction in self.path:
            if instruction.startswith("U"):
                self.move_up(instruction)
            elif instruction.startswith("D"):
                self.move_down(instruction)
            elif instruction.startswith("L"):
                self.move_left(instruction)
            else:
                self.move_right(instruction)
        return self.wire_path_coords


def crossed_wires(wire_01: list, wire_02: list) -> int:

    coords_wire_01 = WirePath(wire_01)
    coords_wire_02 = WirePath(wire_02)

    wire_01_coords = coords_wire_01.follow_path()
    wire_02_coords = coords_wire_02.follow_path()

    intersetion_points = wire_01_coords.intersection(wire_02_coords)

    closest = min(intersetion_points, key=lambda x: x.dist)

    return closest.dist


with open("input.txt", "r") as f:
    lines = f.read().split("\n")

wire_01 = lines[0].split(",")
wire_02 = lines[1].split(",")

print((crossed_wires(["R8", "U5", "L5", "D3"], ["U7", "R6", "D4", "L4"])))
