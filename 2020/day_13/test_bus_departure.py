import pytest
from bus_departure import next_bus, perfect_timing

test_01 = """939
7,13,x,x,59,x,31,19""".splitlines()


@pytest.mark.parametrize(
    "input, expected",
    [
        (test_01, 295),
    ],
)
def test_next_bus(input, expected):
    assert next_bus(input)[2] == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        (test_01, 1068781),
    ],
)
def test_perfect_timing(input, expected):
    assert perfect_timing(input) == expected