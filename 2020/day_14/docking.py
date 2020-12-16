from collections import defaultdict
from itertools import product
import re


class Docking:
    def __init__(self, input) -> None:

        self.instructions = input
        self.mask = ""
        self.memory = dict()
        self.rx = re.compile(r"mem\[(\d+)\]")

    def process_instructions(self, part):
        for ins in self.instructions:
            action, value = ins.split(" = ")
            if action == "mask":
                self.mask = [c for c in value]
                continue
            memory_loc = re.findall(self.rx, action)[0]
            if part == 1:
                self.update_memory_part01(memory_loc, value)
            else:
                self.update_memory_part02(memory_loc, value)
        return sum(self.memory.values())

    def update_memory_part01(self, memory_loc, value):
        value_bin_list = [int(x) for x in bin(int(value))[2:].zfill(36)]
        value_pairs = list(zip(self.mask, value_bin_list))
        masked_value = []
        for value_pair in value_pairs:
            if value_pair[0] == "X":
                masked_value.append(value_pair[1])
            else:
                masked_value.append(value_pair[0])
        self.memory[memory_loc] = int("".join(str(n) for n in masked_value), 2)

    def update_memory_part02(self, memory_loc, value):
        float_loc = [idx for idx, val in enumerate(self.mask) if val == "X"]
        float_num = len(float_loc)
        float_seq = ["".join(seq) for seq in product("01", repeat=float_num)]

        mem_bin_list = [int(x) for x in bin(int(memory_loc))[2:].zfill(36)]
        mem_pairs = list(zip(self.mask, mem_bin_list))

        # Base Memory address
        masked_mem = list()
        for mem_pair in mem_pairs:
            if mem_pair[0] == "0":
                masked_mem.append(str(mem_pair[1]))
            elif mem_pair[0] == "1":
                masked_mem.append("1")
            else:
                masked_mem.append("X")

        for bin_seq in float_seq:
            for digit_idx, digit in enumerate(bin_seq):
                masked_mem[float_loc[digit_idx]] = digit

            mem_loc = int("".join(str(n) for n in masked_mem), 2)
            self.memory[mem_loc] = int(value)


if __name__ == "__main__":

    # Read in the input ... always called `input`
    # Customize depending on the type of data structure required

    # Day 11: Just read text in
    with open("input") as f:
        input = f.read().splitlines()

    dock = Docking(input)
    print(f"Part 1: {dock.process_instructions(1)}")

    dock_02 = Docking(input)
    print(f"Part 2: {dock_02.process_instructions(2)}")