import pytest
from seat_number import get_seat_numbers, find_my_seat


@pytest.mark.parametrize(
    "input, expected",
    [
        (["FBFBBFFRLR"], 357),
    ],
)
def test_get_seat_numbers(input, expected):
    assert max(get_seat_numbers(input)) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        (["FFFFFBFLLR", "FFFFFBFLRL", "FFFFFBFRLL", "FFFFFBFRLR"], 19),
    ],
)
def test_find_my_seat(input, expected):
    assert find_my_seat(get_seat_numbers(input)) == expected
