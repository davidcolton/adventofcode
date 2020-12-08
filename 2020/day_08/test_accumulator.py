import pytest
from accumulator import Accumulator

input = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

input_dict = {
    idx: {"action": inst.split()[0], "value": int(inst.split()[1])}
    for idx, inst in enumerate(input.split("\n"), 1)
}

acc = Accumulator(input_dict)


@pytest.mark.parametrize(
    "acc, expected",
    [
        (acc, 5),
    ],
)
def test_process_instructions(acc, expected):
    assert acc.process_instructions() == expected


@pytest.mark.parametrize(
    "acc, expected",
    [
        (acc, 8),
    ],
)
def test_debug_instructions(acc, expected):
    assert acc.debug_instructions()[0] == expected