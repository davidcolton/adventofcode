import numpy as np

test_data = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


def get_points(inp):
    points = []
    max_a = 0
    max_b = 0
    for l in inp.splitlines():
        a, b = l.split(",")
        points.append((int(a), int(b)))
        max_a = max(max_a, int(a))
        max_b = max(max_b, int(b))
    return points, (max_a, max_b)


def get_folds(inp):
    folds = []
    for l in inp.split("\n"):
        folds.append(l[11:].split("="))
    return folds


if __name__ == "__main__":

    with open("input") as f:
        data = f.read()

    input_01, input_02 = data.split("\n\n")

    points, sizes = get_points(input_01.strip())
    folds = get_folds(input_02.strip())

    arr = np.zeros([sizes[0] + 1, sizes[1] + 1])

    print(len(points))
    for p in points:
        arr[p[0], p[1]] += 1

    arr = arr.T
    print(f"PART 01: {(arr > 0).sum()}")

    fold_point = int(folds[0][1])

    arr_top = arr[:fold_point]
    arr_bot = arr[fold_point + 1 :]

    arr_bot = np.flipud(arr_bot)

    offset = arr_top.shape[0] - arr_bot.shape[0]

    arr_top[offset:] += arr_bot

    print(f"PART 01: {(arr_top > 0).sum()}")
