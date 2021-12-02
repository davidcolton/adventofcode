import pytest
from position import calculate_position


@pytest.mark.parametrize(
    "input, expected",
    [
        ([['forward', 5],
        ['down', 5],
        ['forward', 8],
        ['up', 3],
        ['down', 8],
        ['forward', 2]], 150),
    ],
)
def test_calculate_position(input, expected):
    assert calculate_position(input) == expected
