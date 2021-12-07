import pytest
import numpy as np
from whales import least_cost, weighted_least_cost

input = "16,1,2,0,4,2,7,1,2,14"

data = [int(n) for n in input.split(",")]


@pytest.mark.parametrize(
    "input, expected",
    [
        (data, 37),
    ],
)
def test_least_cost(input, expected):
    assert least_cost(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        (data, 168),
    ],
)
def test_weighted_least_cost(input, expected):
    assert weighted_least_cost(input) == expected
