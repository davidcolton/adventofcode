import numpy as np
from dataclasses import dataclass, field


input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

small_input = """11111
19991
19191
19991
11111"""

data = [[int(num) for num in block] for block in (line for line in input.split("\n"))]


@dataclass
class OctopusGrid:
    arr: np.array

    MAX_A: int = field(init=False)
    MAX_B: int = field(init=False)

    cycles: int = 100

    MIN_A: int = 0
    MIN_B: int = 0

    def __post_init__(self):
        self.MAX_A = self.arr.shape[0]
        self.MAX_B = self.arr.shape[1]

    def run_cycles(self):
        flashes = 0
        for c in range(self.cycles):
            self.increase_energy()
            this_flash = self.flash()
            flashes += this_flash
        return flashes

    def increase_energy(self, increase=1):
        self.arr += 1

    def flash(self):

        while (self.arr > 9).sum():
            # The list of points that are greater that or equal to 9
            nines = list(np.transpose((self.arr > 9).nonzero()))

            # Create a zero array with the nine locations blocked out
            zero_arr = np.zeros([self.MAX_A, self.MAX_B])
            zero_arr[self.arr > 9] = np.nan

            # For each location that was a nine, increment neighbours
            for n in nines:
                a1, a2, b1, b2 = self.get_boundaries(n)
                zero_arr[a1:a2, b1:b2] += 1

            # Reset octopuses that flashed
            self.arr[self.arr > 9] = np.nan

            # Add the result of the flashed
            zero_arr[np.isnan(zero_arr)] = 0
            self.arr += zero_arr.astype(int)

        # Count the number of flashed octopus
        flashed = np.count_nonzero(np.isnan(self.arr))

        # Reset flashed octopus to zero
        self.arr[np.isnan(self.arr)] = 0

        return flashed

    def get_boundaries(self, n):
        a, b = n
        a1 = a - 1 if a - 1 > 0 else 0
        a2 = a + 2
        b1 = b - 1 if b - 1 > 0 else 0
        b2 = b + 2

        return a1, a2, b1, b2


if __name__ == "__main__":

    # Read in the input ... always called `input`
    # Customize depending on the type of data structure required

    with open("input") as f:
        f_input = f.read()

    f_data = [
        [int(num) for num in block] for block in (line for line in f_input.split("\n"))
    ]

    arr = np.array(f_data).astype(float)

    grid = OctopusGrid(arr, cycles=100)
    print(f"PART 01: {grid.run_cycles()}")

    grid = OctopusGrid(arr, cycles=250)
    print(grid.run_cycles())
