from collections import deque
import numpy as np
from scipy.ndimage.interpolation import shift

'''input = """2199943210
3987894921
9856789892
8767896789
9899965678"""

data = [[int(num) for num in block] for block in (line for line in input.split("\n"))]'''


def risk_level(data):

    above = shift(arr, (1, 0), cval=10)
    below = shift(arr, (-1, 0), cval=10)
    left = shift(arr, (0, 1), cval=10)
    right = shift(arr, (0, -1), cval=10)

    comp_above = arr < above
    comp_below = arr < below
    comp_left = arr < left
    comp_right = arr < right

    result = comp_above & comp_below & comp_left & comp_right

    return result


if __name__ == "__main__":

    # Read in the input ... always called `input`
    # Customize depending on the type of data structure required

    with open("input") as f:
        input = f.read()
    data = [
        [int(num) for num in block] for block in (line for line in input.split("\n"))
    ]
    arr = np.array(data)

    part_01 = risk_level(data)
    print(f"Part 01: {(arr[part_01] + 1).sum()}")

    low_points = np.transpose((part_01 == True).nonzero())
    # nines = np.transpose((arr < 9).nonzero())
    # nines_list = [(ar[0], ar[1]) for ar in (n for n in nines)]

    MIN_A = MIN_B = 0
    MAX_A, MAX_B = arr.shape

    basin_sizes = []

    for low_point in low_points:
        # Initializing a search queue and add the point
        points_to_test = deque()
        points_to_test.append(low_point)

        # Initialise a zero array
        basins = np.zeros((MAX_A, MAX_B))

        seen = []

        while points_to_test:
            p = points_to_test.popleft()
            a, b = p

            # Add p to basins
            # Hack to account for 0 lowest points
            basins[a, b] = arr[a, b] + 1

            # Test up, avoid if 0
            if a > 0:
                # Add to queue
                if arr[a - 1, b] < 9 and f"{a - 1}{b}" not in seen:
                    points_to_test.append(np.array([a - 1, b]))
                    seen.append(f"{a - 1}{b}")

            # Test right, avoid if > MAX_B
            if b < MAX_B - 1:
                # Add to queue
                if arr[a, b + 1] < 9 and f"{a}{b + 1}" not in seen:
                    points_to_test.append(np.array([a, b + 1]))
                    seen.append(f"{a}{b + 1}")

            # Test down, avoid if > MAX_a
            if a < MAX_A - 1 and f"{a + 1}{b}" not in seen:
                # Add to queue
                if arr[a + 1, b] < 9:
                    points_to_test.append(np.array([a + 1, b]))
                    seen.append(f"{a + 1}{b}")

            # Test left, avoid if 0
            if b > 0:
                # Add to queue
                if arr[a, b - 1] < 9 and f"{a}{b - 1}" not in seen:
                    points_to_test.append(np.array([a, b - 1]))
                    seen.append(f"{a}{b - 1}")

        basin_sizes.append((basins > 0).sum())

    basin_sizes.sort()

    print(f"Part 02: {basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]}")
