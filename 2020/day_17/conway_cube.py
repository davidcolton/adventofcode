import numpy as np


class ConwayCube:
    def __init__(self, input, iterations=6):

        self.iterations = iterations
        self.starting_grid = self.get_starting_grid(input)

        print(f"Sum {sum(self.starting_grid)}")

    def get_starting_grid(self, input):
        g = np.array(
            [
                [int(n) for n in l]
                for l in input.replace("#", "1").replace(".", "0").splitlines()
            ]
        )

        max_grid_size = max(g.shape) + (self.iterations * 2) + 1
        mid_point = max_grid_size // 2 + 1

        grid = np.zeros([max_grid_size, max_grid_size, max_grid_size])

        for idx, val in np.ndenumerate(g):
            grid[mid_point, idx[0] + self.iterations, idx[1] + self.iterations] = val

        return grid


if __name__ == "__main__":

    # Read in the input ... always called `input`
    # Customize depending on the type of data structure required

    # Day 11: Just read text in
    with open("input") as f:
        input = f.read()

    con = ConwayCube(input)