import pytest
import numpy as np
from toboggan import count_tree_hit


@pytest.mark.parametrize(
    "across, down, array, expected",
    [
        (
            2,
            1,
            np.array(
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 1],
                    [0, 1, 0, 0, 1],
                    [0, 0, 1, 0, 1],
                ]
            ),
            3,
        ),
        (
            1,
            2,
            np.array(
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 1],
                    [0, 1, 0, 0, 1],
                    [0, 0, 1, 0, 1],
                ]
            ),
            1,
        ),
    ],
)
def test_count_tree_hit(across, down, array, expected):
    assert count_tree_hit(across, down, array) == expected
