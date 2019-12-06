import pytest
from uom import count_orbits


test_orbits = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""


def test_count_orbits():
    assert count_orbits(test_orbits) == 42
