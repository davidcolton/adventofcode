from dataclasses import dataclass, field
from collections import Counter

input = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""


@dataclass
class SimpleDigit:
    pattern: str
    output: str

    @property
    def count_unique_output(self):
        output_strs = self.output.split(" ")

        return sum([1 for o in output_strs if len(o) in [2, 3, 4, 7]])


@dataclass
class DecodedDigit:
    scrambled_patterns: str
    scrambled_outputs: str

    top: str = field(init=False)
    top_left: str = field(init=False)
    top_right: str = field(init=False)
    middle: str = field(init=False)
    bottom_left: str = field(init=False)
    bottom_right: str = field(init=False)
    bottom: str = field(init=False)

    zero: set = field(init=False)
    one: set = field(init=False)
    two: set = field(init=False)
    three: set = field(init=False)
    four: set = field(init=False)
    five: set = field(init=False)
    six: set = field(init=False)
    seven: set = field(init=False)
    eight: set = field(init=False)
    nine: set = field(init=False)

    numbers: list = field(init=False)

    def __post_init__(self):
        pattern_strs = self.scrambled_patterns.split(" ")

        # Get candidates for top_right and top_left
        for candidate in pattern_strs:
            if len(candidate) != 2:
                continue
            potential_tr, potential_br = [can for can in candidate]
            # print(f"Potential tr, br from 1: {potential_tr, potential_br}")

        # Now we can get top from 7
        for candidate in pattern_strs:
            if len(candidate) != 3:
                continue
            potential_top = [can for can in candidate]
            # print(f"Extract TOP from 7: {potential_top}")
            potential_top.remove(potential_tr)
            potential_top.remove(potential_br)
            self.top = potential_top[0]
            # print(f"TOP: {self.top}")

        # Now we get candidates for top_left and middle from 4
        for candidate in pattern_strs:
            if len(candidate) != 4:
                continue
            potentials = [can for can in candidate]
            # print(f"Extract tl and m from: {potentials}")
            potentials.remove(potential_tr)
            potentials.remove(potential_br)
            potential_tl, potential_m = [can for can in potentials]
            # print(f"Potential tl, m from 4: {potential_tl, potential_m}")

        # Now we get bottom from 9
        for candidate in pattern_strs:
            if len(candidate) == 6:
                potentials = [can for can in candidate]
                # print(f"Extract b from: {potentials}")
                try:
                    potentials.remove(potential_tr)
                    potentials.remove(potential_br)
                    potentials.remove(potential_tl)
                    potentials.remove(potential_m)
                    potentials.remove(self.top)
                    if len(potentials) == 1:
                        self.bottom = potentials[0]
                    # print(f"BOTTOM from 9: {self.bottom}")
                    break
                except ValueError:
                    continue

        # Now we get bottom_left from 8
        for candidate in pattern_strs:
            if len(candidate) != 7:
                continue
            potentials = [can for can in candidate]
            # print(f"Extract bl from: {potentials}")
            try:
                potentials.remove(potential_tr)
                potentials.remove(potential_br)
                potentials.remove(potential_tl)
                potentials.remove(potential_m)
                potentials.remove(self.top)
                potentials.remove(self.bottom)
                if len(potentials) == 1:
                    self.bottom_left = potentials[0]
                # print(f"BOTTOM LEFT from 8: {self.bottom_left}")
                break
            except ValueError:
                continue

        # Now we get bottom right from 6
        for candidate in pattern_strs:
            if len(candidate) == 6:
                potentials = [can for can in candidate]
                # print(f"Extract br from: {potentials}")
                try:
                    potentials.remove(potential_m)
                    potentials.remove(potential_tl)
                    potentials.remove(self.bottom_left)
                    potentials.remove(self.bottom)
                    potentials.remove(self.top)
                    if len(potentials) == 1:
                        self.bottom_right = potentials[0]
                    # print(f"BOTTOM RIGHT from 6: {self.bottom_right}")
                    break
                except ValueError:
                    continue

        # Now we have bottom_right we get top_right
        if potential_br == self.bottom_right:
            self.top_right = potential_tr
        else:
            self.top_right = potential_br
        # print(f"TOP RIGHT: {self.top_right}")

        # Now we also get middle from 2
        for candidate in pattern_strs:
            if len(candidate) != 5:
                continue
            potentials = [can for can in candidate]
            # print(f"Extract m from: {potentials}")
            try:
                potentials.remove(self.top)
                potentials.remove(self.top_right)
                potentials.remove(self.bottom_left)
                potentials.remove(self.bottom)
                if len(potentials) == 1:
                    self.middle = potentials[0]
                # print(f"MIDDLE from 2: {self.middle}")
                break
            except ValueError:
                continue

        # Now we have middle we get top_left
        if potential_m == self.middle:
            self.top_left = potential_tl
        else:
            self.top_left = potential_m
        # print(f"TOP LEFT: {self.top_left}")

        self.zero = set(
            self.top
            + self.top_left
            + self.top_right
            + self.bottom_left
            + self.bottom_right
            + self.bottom
        )

        self.one = set(self.top_right + self.bottom_right)

        self.two = set(
            self.top + self.top_right + self.middle + self.bottom_left + self.bottom
        )

        self.three = set(
            self.top + self.top_right + self.middle + self.bottom_right + self.bottom
        )

        self.four = set(
            self.top_left + self.top_right + self.middle + self.bottom_right
        )

        self.five = set(
            self.top + self.top_left + self.middle + self.bottom_right + self.bottom
        )

        self.six = set(
            self.top
            + self.top_left
            + self.middle
            + self.bottom_left
            + self.bottom_right
            + self.bottom
        )

        self.seven = set(self.top + self.top_right + self.bottom_right)

        self.eight = set(
            self.top
            + self.top_left
            + self.top_right
            + self.middle
            + self.bottom_left
            + self.bottom_right
            + self.bottom
        )

        self.nine = set(
            self.top
            + self.top_left
            + self.top_right
            + self.middle
            + self.bottom_right
            + self.bottom
        )

        self.numbers = {
            "0": self.zero,
            "1": self.one,
            "2": self.two,
            "3": self.three,
            "4": self.four,
            "5": self.five,
            "6": self.six,
            "7": self.seven,
            "8": self.eight,
            "9": self.nine,
        }

    def decode_output(self):
        number = ""
        digits = self.scrambled_outputs.split(" ")
        for digit in digits:
            digit = set(digit)
            for key, value in self.numbers.items():
                if digit == value:
                    number = number + key
        return int("".join(n for n in number))

    @property
    def count_unique_output(self):
        output_strs = self.output.split(" ")

        return sum([1 for o in output_strs if len(o) in [2, 3, 4, 7]])


def simple_digits(input):

    simple_observations = [
        SimpleDigit(x[0], x[1]) for x in (x.split(" | ") for x in input.split("\n"))
    ]

    return sum(obs.count_unique_output for obs in simple_observations)


def decode_digits(input):

    observations = [
        DecodedDigit(x[0], x[1]) for x in (x.split(" | ") for x in input.split("\n"))
    ]

    total = 0
    for obs in observations:
        total += obs.decode_output()

    return total


if __name__ == "__main__":

    # Read in the input ... always called `input`
    # Customize depending on the type of data structure required

    # Day 01: A simple list of numbers
    with open("input") as f:
        values = f.read()

    print(f"Part 01: {simple_digits(values)}")
    print(f"Part 02: {decode_digits(values)}")
