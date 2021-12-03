import pytest
import pandas as pd
from binary import get_power
from binary import get_life_support

data = [
    [0,0,1,0,0],
    [1,1,1,1,0],
    [1,0,1,1,0],
    [1,0,1,1,1],
    [1,0,1,0,1],
    [0,1,1,1,1],
    [0,0,1,1,1],
    [1,1,1,0,0],
    [1,0,0,0,0],
    [1,1,0,0,1],
    [0,0,0,1,0],
    [0,1,0,1,0],
]

df = pd.DataFrame(data, columns=[1,2,3,4,5])

@pytest.mark.parametrize(
    "input, expected",
    [
        (df, 198),
    ],
)
def test_get_power(input, expected):
    assert get_power(input) == expected

@pytest.mark.parametrize(
    "input, expected",
    [
        (df, 230),
    ],
)
def test_get_life_support(input, expected):
    assert get_life_support(input) == expected