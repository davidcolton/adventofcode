import pytest
from matchsticks import MatchSticks


@pytest.mark.parametrize(
    "arg, expected",
    [
        (r'""', [2, 0, 6]),
        (r'"abc"', [5, 3, 9]),
        (r'"aaa\"aaa"', [10, 7, 16]),
        (r'"\x27"', [6, 1, 11]),
    ],
)
def test_matchsticks_lengths(arg, expected):
    ms = MatchSticks(arg)
    ms.calculate_string_lengths()
    assert ms.get_total_length_raw == expected[0]
    assert ms.get_total_length_decoded == expected[1]
    assert ms.get_total_length_escaped == expected[2]
