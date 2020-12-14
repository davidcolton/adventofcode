import pytest
from navigate import Navigate
from waypoint import WayPoint

test_01 = """F10
N3
F7
R90
F11"""

nav = Navigate(test_01.splitlines())
way = WayPoint(test_01.splitlines())


@pytest.mark.parametrize(
    "nav, expected",
    [
        (nav, 25),
    ],
)
def test_find_optimal_seating(nav, expected):
    assert nav.process_instructions()[2] == expected


@pytest.mark.parametrize(
    "way, expected",
    [
        (way, 286),
    ],
)
def test_find_optimal_seating(way, expected):
    assert way.process_instructions()[1] == expected