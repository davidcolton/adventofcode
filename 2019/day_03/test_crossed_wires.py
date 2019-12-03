import pytest
from crossed_wires import crossed_wires


@pytest.mark.parametrize(
    "arg, expected",
    [
        ([["R8", "U5", "L5", "D3"], ["U7", "R6", "D4", "L4"]], 6),
        (
            [
                ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
                ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"],
            ],
            159,
        ),
        (
            [
                [
                    "R98",
                    "U47",
                    "R26",
                    "D63",
                    "R33",
                    "U87",
                    "L62",
                    "D20",
                    "R33",
                    "U53",
                    "R51",
                ],
                ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"],
            ],
            135,
        ),
    ],
)
def test_crossed_wires(arg, expected):
    wire_01 = arg[0]
    wire_02 = arg[1]
    assert crossed_wires(wire_01, wire_02) == expected


"""Here are the best steps for the extra examples from above:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps
What is the fewest combined steps the wires must take to reach an intersection?"""

