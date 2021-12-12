import pytest
from caves import read_paths, path_count

test_01 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

paths_01 = read_paths(test_01)

test_02 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

paths_02 = read_paths(test_02)


test_03 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

paths_03 = read_paths(test_03)


@pytest.mark.parametrize(
    "input, expected",
    [
        (paths_01, 10),
        (paths_02, 19),
        (paths_03, 226),
    ],
)
def test_path_count(input, expected):
    assert path_count(input, "start", twice_visited=True) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        (paths_01, 36),
        (paths_02, 103),
        (paths_03, 3509),
    ],
)
def test_path_count_02(input, expected):
    assert path_count(input, "start") == expected
