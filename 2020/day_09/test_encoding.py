import pytest
from encoding import Encoding

input = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

test_01 = [int(n) for n in input.split("\n")]

enc = Encoding(test_01, 5)


@pytest.mark.parametrize(
    "enc, expected",
    [
        (enc, 127),
    ],
)
def test_process_instructions(enc, expected):
    assert enc.find_weakness_number() == expected


@pytest.mark.parametrize(
    "enc, expected",
    [
        (enc, 62),
    ],
)
def test_debug_instructions(enc, expected):
    assert enc.find_encryption_weakness() == expected