import pytest
import pandas as pd
from binary import get_power

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

df = pd.DataFrame(data)

@pytest.mark.parametrize(
    "input, expected",
    [
        (df, 198),
    ],
)
def test_get_power(input, expected):
    assert get_power(input) == expected