import pytest
import numpy as np
from lava import risk_level

input = """2199943210
3987894921
9856789892
8767896789
9899965678"""

data = [[int(num) for num in block] for block in (line for line in input.split("\n"))]


@pytest.mark.parametrize(
    "input, expected",
    [
        (data, 15),
    ],
)
def test_risk_level(input, expected):
    assert risk_level(input) == expected
