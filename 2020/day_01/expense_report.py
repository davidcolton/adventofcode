from itertools import combinations
import numpy as np


def fix_expenses(target, count, report):
    solution = [
        option for option in combinations(report, count) if sum(option) == target
    ]
    if solution:
        print(f"Solution Found: {solution}")
        print(f"The product of these two numbers is {np.prod(solution)}")
        return np.prod(solution)
    else:
        print("No solutions exist")
        return None


if __name__ == "__main__":

    # Read in the input ... always called `input`
    # Customize depending on the type of data structure required

    # Day 01: A simple list of numbers
    with open("input") as f:
        values = [int(line.strip()) for line in f]

    answer = fix_expenses(2020, 3, values)

