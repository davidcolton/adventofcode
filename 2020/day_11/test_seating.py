import pytest
from seating import Seating

test_01 = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

seats_01 = Seating(test_01)
seats_02 = Seating(test_01, recursive=True)


@pytest.mark.parametrize(
    "seats, expected",
    [
        (seats_01, 37),
        (seats_02, 26),
    ],
)
def test_find_optimal_seating(seats, expected):
    assert seats.find_optimal_seating() == expected