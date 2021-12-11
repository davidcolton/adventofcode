import pytest
import numpy as np
from octopus import risk_level

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


@pytest.mark.parametrize(
    "input, expected",
    [
        (data, 15),
    ],
)
def test_risk_level(input, expected):
    assert risk_level(input) == expected
