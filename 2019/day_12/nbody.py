from dataclasses import dataclass


@dataclass
class Point:
    x: int = 0
    y: int = 0
    z: int = 0

    def __add__(self, point):
        self.x += point.x
        self.y += point.y
        self.z += point.z
        return self

    def __str__(self):
        return f"Point({self.x}, {self.y}, {self.z})"


class Body:
    def __init__(self, name, point):
        self.name = name
        self.position = point
        self.initial_position = Point(point.x, point.y, point.z)
        self.velocity = Point(0, 0, 0)
        self.next_move = Point(0, 0, 0)
        self.neighbors = []
        self.trajectory = [[Point(point.x, point.y, point.z), Point(0, 0, 0)]]
        self.count_of_moves = 0
        self.moves_to_repeat = [0, 0, 0]

    def _gravity(self, p1, p2):
        if p1 > p2:
            return -1
        if p2 > p1:
            return 1
        else:
            return 0

    def calculate_next_move(self):
        self.next_move = Point(0, 0, 0)
        for body in self.neighbors:
            self.next_move.x += self._gravity(self.position.x, body.position.x)
            self.next_move.y += self._gravity(self.position.y, body.position.y)
            self.next_move.z += self._gravity(self.position.z, body.position.z)
        return self

    def make_next_move(self):
        # Add next move
        self.position = self.position + self.next_move

        # Add current velocity
        self.position = self.position + self.velocity

        # Update velocity
        self.velocity = self.velocity + self.next_move

        # Add new position to trajectory
        self.trajectory.append(
            [
                Point(self.position.x, self.position.y, self.position.z),
                Point(self.velocity.x, self.velocity.y, self.velocity.z),
            ]
        )

        # Add count to number of moves
        self.count_of_moves += 1

        return self


class Moons:
    def __init__(self, moons, iterations):
        self.body_list = moons
        self.iterations = iterations

    def populate_neighbors(self):
        for body in self.body_list:
            body.neighbors = [moon for moon in self.body_list if body != moon]
        return self

    def move_moons(self):

        for i in range(1, self.iterations + 1):
            current_positions = []
            current_velocities = []
            for m in self.body_list:
                m.calculate_next_move()
            for m in self.body_list:
                m.make_next_move()
                current_positions.append(m)
                current_velocities.append(m.velocity)

            # Determine if planet positions all == original
            if all(
                [
                    p.position.x == p.initial_position.x and p.velocity.x == 0
                    for p in current_positions
                ]
            ):
                print(f"x dimensions repeat after {i} movements")
            if all(
                [
                    p.position.y == p.initial_position.y and p.velocity.y == 0
                    for p in current_positions
                ]
            ):
                print(f"y dimensions repeat after {i} movements")
            if all(
                [
                    p.position.z == p.initial_position.z and p.velocity.z == 0
                    for p in current_positions
                ]
            ):
                print(f"z dimensions repeat after {i} movements")

        return self

    def calculate_total_energy(self):
        body_energies = []
        for body in self.body_list:
            print(body.position, body.velocity)
            pos = abs(body.position.x) + abs(body.position.y) + abs(body.position.z)
            vel = abs(body.velocity.x) + abs(body.velocity.y) + abs(body.velocity.z)
            body_energies.append(pos * vel)
        return sum(body_energies)


Io = Body("Io", Point(8, 0, 8))
Europa = Body("Europa", Point(0, -5, -10))
Ganymede = Body("Ganymede", Point(16, 10, -5))
Callisto = Body("Callisto", Point(19, -10, -7))

jupiter_moons = Moons([Io, Europa, Ganymede, Callisto], 300000)
jupiter_moons.populate_neighbors()
jupiter_moons.move_moons()
print(jupiter_moons.calculate_total_energy())

