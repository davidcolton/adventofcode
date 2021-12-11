from dataclasses import dataclass
import pytest
import numpy as np
from octopus import OctopusGrid

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

data = [[int(num) for num in block] for block in (line for line in input.split("\n"))]
arr = np.array(data).astype(float)
grid_10 = OctopusGrid(arr, cycles=10)
grid_100 = OctopusGrid(arr, cycles=100)

small_input = """11111
19991
19191
19991
11111"""

small_data = [
    [int(num) for num in block] for block in (line for line in small_input.split("\n"))
]
small_arr = np.array(small_data).astype(float)
small_grid = OctopusGrid(small_arr, cycles=2)


@pytest.mark.parametrize(
    "input, expected",
    [
        (small_grid, 9),
        (grid_10, 204),
        (grid_100, 1656),
    ],
)
def test_risk_level(input, expected):
    assert input.run_cycles() == expected
