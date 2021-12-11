from os.path import dirname, join
from itertools import product
import numpy as np


def parse(filename):
    with open(join(dirname(__file__), filename), "r") as f:
        return np.array(
            [[int(char) for char in line] for line in f.read().splitlines()]
        )


def solution(grid, star):
    total_flashes = 0
    i = 1
    while True:
        grid = grid + 1
        while True:
            flash_coords = list(zip(*np.where(grid > 9)))
            if len(flash_coords) == 0:
                break
            grid = np.where(grid > 9, 0, grid)
            for x, y in flash_coords:
                total_flashes += 1
                for dx, dy in product(*zip(*[(x + j, y + j) for j in [-1, 0, 1]])):
                    if (
                        (dx, dy) != (x, y)
                        and all(k in range(0, 10) for k in [dx, dy])
                        and grid[dx, dy] != 0
                    ):
                        grid[dx, dy] = grid[dx, dy] + 1
        if star == 1 and i == 100:
            return total_flashes
        if star == 2 and np.all((grid == 0)):
            return i
        i += 1


grid = parse("input")

print("Star 1:", solution(grid, 1))
print("Star 2:", solution(grid, 2))
