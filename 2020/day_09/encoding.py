from itertools import permutations


class Encoding:
    def __init__(self, input, window=25):

        self.values = input
        self.window = window

        self.weakness_number = 0

    def find_weakness_number(self):

        insp_value = self.window

        # Simple sliding window. Sum of next number should be in the window
        while insp_value < len(self.values):
            if not any(
                num_1 + num_2 == self.values[insp_value]
                for num_1, num_2 in permutations(
                    self.values[insp_value - self.window : insp_value], 2
                )
            ):
                self.weakness_number = self.values[insp_value]
                return self.values[insp_value]
            insp_value += 1

    def find_encryption_weakness(self):

        if not self.weakness_number:
            self.find_encryption_weakness()

        first_idx = 0
        last_idx = 1

        while first_idx < len(self.values):
            if sum(self.values[first_idx:last_idx]) < self.weakness_number:
                last_idx += 1
            elif sum(self.values[first_idx:last_idx]) > self.weakness_number:
                first_idx += 1
                last_idx = first_idx + 1
            else:
                return min(self.values[first_idx:last_idx]) + max(
                    self.values[first_idx:last_idx]
                )


if __name__ == "__main__":

    # Read in the input ... always called `input`
    # Customize depending on the type of data structure required

    # Day 09: Just read text in split into list of lines,
    with open("input") as f:
        input = [int(n) for n in f.read().splitlines()]

    # Create Encoding Class
    enc = Encoding(input)
    part_01 = enc.find_weakness_number()
    print(f"Part 1: Weakness Number is {part_01}")
    part_02 = enc.find_encryption_weakness()
    print(f"Part 2: Encryption Weakness is {part_02}")
