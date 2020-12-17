import pytest
from memory_game import memory_game


@pytest.mark.parametrize(
    "input, turns, expected",
    [
        ("0,3,6", 10, 0),
    ],
)
def test_memory_game(input, turns, expected):
    assert memory_game(input, turns) == expected
