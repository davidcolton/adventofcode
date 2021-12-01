import pytest
from sonar import examine_sonar


@pytest.mark.parametrize(
    "input, expected",
    [
        ([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 7),
        ([199, 200, 208, 210, 240, 269], 5),
        ([199, 100], 0),
    ],
)
def test_examine_sonar(input, expected):
    assert examine_sonar(input) == expected
