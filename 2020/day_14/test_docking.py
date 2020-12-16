import pytest
from docking import Docking

test_01 = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0""".splitlines()

test_02 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1""".splitlines()

dock_01 = Docking(test_01)
dock_02 = Docking(test_02)


@pytest.mark.parametrize(
    "dock_01, expected",
    [
        (dock_01, 165),
    ],
)
def test_process_instructions_part_01(dock_01, expected):
    assert dock_01.process_instructions(1) == expected


@pytest.mark.parametrize(
    "dock_02, expected",
    [
        (dock_02, 208),
    ],
)
def test_process_instructions_part_01(dock_02, expected):
    assert dock_02.process_instructions(2) == expected