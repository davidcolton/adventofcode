import numpy as np

from skimage.util.shape import view_as_windows as vw


def strided_indexing_roll(a, r):
    # See https://stackoverflow.com/questions/51200369/shift-rows-of-a-numpy-array-independently
    # Concatenate with sliced to cover all rolls
    p = np.full((a.shape[0], a.shape[1] - 1), np.nan)
    a_ext = np.concatenate((p, a, p), axis=1)

    # Get sliding windows; use advanced-indexing to select appropriate ones
    n = a.shape[1]
    return vw(a_ext, (1, n))[np.arange(len(r)), -r + (n - 1), 0]


def count_tree_hit(across, down, single_array):

    # The shape of the single array
    no_rows, num_cols = single_array.shape

    # Number of times to multiple the single array across
    # Could divide by the number of down step to reduce for performance
    array_multiplier = ((no_rows * across) // num_cols) + 1

    # Multiple the single array
    full_array = np.tile(single_array, (1, array_multiplier))

    # Need to handle the scenario where down is greater than 1
    # We handle this by only considering every nth row
    if down > 1:
        full_array = full_array[::down]

    # Refresh the number of rows and columns
    no_rows, num_cols = full_array.shape

    # The plan is to shift each row left by the negative across value
    # Use range to create this list of shift values
    shift_array = np.array(list(range(0, -(no_rows * across), -across)))

    # Now shift each row
    shifted_array = strided_indexing_roll(full_array, shift_array)

    # Sum each column and return the value for the first
    return np.sum(shifted_array, axis=0)[0]


if __name__ == "__main__":

    # Read in the input ... always called `input`
    # Customize depending on the type of data structure required

    # Day 03: A simple list
    with open("input") as f:
        lines = f.read().replace(".", "0").replace("#", "1").split()
        data = [[int(n) for n in line] for line in lines]
        single_array = np.array(data)

    print(f"Number of trees hit: {count_tree_hit(1, 1, single_array)}")
    print(f"Number of trees hit: {count_tree_hit(3, 1, single_array)}")
    print(f"Number of trees hit: {count_tree_hit(5, 1, single_array)}")
    print(f"Number of trees hit: {count_tree_hit(7, 1, single_array)}")
    print(f"Number of trees hit: {count_tree_hit(1, 2, single_array)}")
