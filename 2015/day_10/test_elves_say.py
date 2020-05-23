import pytest
from elves_say import ElvesSay

"""
1 becomes 11 (1 copy of digit 1).
11 becomes 21 (2 copies of digit 1).
21 becomes 1211 (one 2 followed by one 1).
1211 becomes 111221 (one 1, one 2, and two 1s).
111221 becomes 312211 (three 1s, two 2s, and one 1)."""


@pytest.mark.parametrize(
    "arg1, arg2, expected", [(1, 1, 2), (1, 2, 2), (1, 3, 4), (1, 4, 6), (1, 5, 6)]
)
def test_matchsticks_lengths(arg1, arg2, expected):
    es = ElvesSay(arg1, arg2)
    result = es.iterate()
    assert result == expected
