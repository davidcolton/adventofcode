import numpy as np
from scipy.ndimage.interpolation import shift

'''input = """2199943210
3987894921
9856789892
8767896789
9899965678"""

data = [[int(num) for num in block] for block in (line for line in input.split("\n"))]
'''


def risk_level(data):

    arr = np.array(data)

    above = shift(arr, (1, 0), cval=10)
    below = shift(arr, (-1, 0), cval=10)
    left = shift(arr, (0, 1), cval=10)
    right = shift(arr, (0, -1), cval=10)

    comp_above = arr < above
    comp_below = arr < below
    comp_left = arr < left
    comp_right = arr < right

    result = comp_above & comp_below & comp_left & comp_right

    return (arr[result] + 1).sum()


if __name__ == "__main__":

    # Read in the input ... always called `input`
    # Customize depending on the type of data structure required

    with open("input") as f:
        input = f.read()
        data = [
            [int(num) for num in block]
            for block in (line for line in input.split("\n"))
        ]

    print(f"Part 01: {risk_level(data)}")
