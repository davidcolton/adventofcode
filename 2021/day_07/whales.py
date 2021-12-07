import numpy as np


def least_cost(data):

    arr = np.array(data)

    min_val = min(data)
    max_val = max(data)

    results = [(np.absolute(arr - n)).sum() for n in range(min(data), max(data) + 1)]

    return min(results)


def weighted_least_cost(data):

    arr = np.array(data)

    min_val = min(data)
    max_val = max(data)

    results = []

    def f(x):
        return sum(range(1, x + 1))

    for n in range(min(data), max(data) + 1):
        tmp_arr = np.absolute(arr - n)
        tmp_arr = np.array([f(xi) for xi in tmp_arr])

        results.append(tmp_arr.sum())

    return min(results)


if __name__ == "__main__":

    # Read in the input ... always called `input`
    # Customize depending on the type of data structure required

    # Day 01: A simple list of numbers
    with open("input") as f:
        values = f.read()
        data = [int(n) for n in values.split(",")]

    print(f"Part 01: {least_cost(data)}")
    print(f"Part 02: {weighted_least_cost(data)}")
