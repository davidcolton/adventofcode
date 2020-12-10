import pytest
from adapter import joltage_differences, count_combinations

input_01 = """16
10
15
5
1
11
7
19
6
12
4"""

input_02 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

test_01 = [int(n) for n in input_01.split("\n")]
test_02 = [int(n) for n in input_02.split("\n")]


@pytest.mark.parametrize(
    "input, expected",
    [
        (test_01, 35),
        (test_02, 220),
    ],
)
def test_joltage_difference(input, expected):
    assert joltage_differences(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        (test_01, 8),
        (test_02, 19208),
    ],
)
def test_count_combinations(input, expected):
    assert count_combinations(input) == expected