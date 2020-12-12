import pandas as pd
import numpy as np


class Seating:
    def __init__(self, input, recursive=False) -> None:

        self.df = self.process_input(input)
        self.df_copy = self.df.copy()

        self.recursive = recursive
        self.max_neighbours = 5 if self.recursive else 4

        self.row = self.df.shape[0]
        self.column = self.df.shape[1]

        self.row_range = range(self.row)
        self.column_range = range(self.column)

        self.seat_changed = True
        self.seat_moves = 0

    def process_input(self, input):
        seats = [[s.strip() for s in line] for line in input.split("\n")]
        return pd.DataFrame(seats)

    def find_optimal_seating(self):
        # print(f"Entering find optimal seating ...")
        while self.seat_changed:
            self.seat_changed = False
            self.seat_moves += 1
            # print(f"  Iteration: {self.seat_moves}")
            self.seat_changed = any(
                [
                    self.process_seat(row, column)
                    for row in range(self.row)
                    for column in range(self.column)
                ]
            )
            del self.df
            self.df = self.df_copy.copy()

        # print(self.df_copy.apply(pd.value_counts)
        index, counts = np.unique(self.df_copy.values, return_counts=True)
        results = list(zip(index, counts))
        seated = [result[1] for result in results if result[0] == "#"]
        return seated[0]

    def check_valid_seat(self, row, column):
        if row in self.row_range and column in self.column_range:
            return True
        else:
            return False

    def check_seat(self, row, column, row_offset, col_offset):
        r = row + row_offset
        c = column + col_offset
        if self.recursive:
            while self.check_valid_seat(r, c):
                if self.df.iloc[r, c] == "#":
                    return 1
                elif self.df.iloc[r, c] == "L":
                    return 0
                else:
                    r = r + row_offset
                    c = c + col_offset
            return 0
        else:
            if self.check_valid_seat(r, c) and self.df.iloc[r, c] == "#":
                return 1
            else:
                return 0

    def get_neighbours(self, row, column):
        return sum(
            [
                self.check_seat(row, column, -1, -1),  # Above left
                self.check_seat(row, column, -1, 0),  # Above
                self.check_seat(row, column, -1, 1),  # Above right
                self.check_seat(row, column, 0, -1),  # Left
                self.check_seat(row, column, 0, 1),  # Right
                self.check_seat(row, column, 1, -1),  # Below left
                self.check_seat(row, column, 1, 0),  # Below
                self.check_seat(row, column, 1, 1),  # Below right
            ]
        )

    def process_seat(self, row, column):
        # Pandas iloc is rows first then columns
        # print(f"Processing seat ({row}, {column})")
        occupied_neighbours = self.get_neighbours(row, column)
        if self.df_copy.iloc[row, column] == ".":
            return False
        elif occupied_neighbours == 0 and self.df.iloc[row, column] == "L":
            self.df_copy.iloc[row, column] = "#"
            return True
        elif (
            occupied_neighbours >= self.max_neighbours
            and self.df.iloc[row, column] == "#"
        ):
            self.df_copy.iloc[row, column] = "L"
            return True
        return False


test = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

if __name__ == "__main__":

    # Read in the input ... always called `input`
    # Customize depending on the type of data structure required

    # Day 11: Just read text in
    with open("input") as f:
        input = f.read()

    seats = Seating(test, recursive=True)
    print(f"Number of occupied seat: {seats.find_optimal_seating()}")
