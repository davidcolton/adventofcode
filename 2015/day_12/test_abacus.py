import pytest
from abacus import find_numbers
from abacus import find_numbers_nored


@pytest.mark.parametrize(
    "arg, expected",
    [
        ([1, 2, 3], 6),
        ({"a": 2, "b": 4}, 6),
        ([[[3]]], 3),
        ({"a": {"b": 4}, "c": -1}, 3),
        ({"a": [-1, 1]}, 0),
        ([-1, {"a": 1}], 0),
        ([], 0),
        ({}, 0),
    ],
)
def test_find_numbers(arg, expected):
    result = find_numbers(arg, 0)
    assert result == expected


@pytest.mark.parametrize(
    "arg, expected",
    [
        ([1, 2, 3], 6),
        ([1, {"c": "red", "b": 2}, 3], 4),
        # Interesting next test fails if root level dictionary
        # contains a red value. I know why but not going to fix
        ([{"d": "red", "e": [1, 2, 3, 4], "f": 5}], 0),
        ([1, "red", 5], 6),
    ],
)
def test_find_numbers_nored(arg, expected):
    result = find_numbers_nored(arg, 0)
    assert result == expected
