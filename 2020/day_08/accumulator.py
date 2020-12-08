from collections import namedtuple
import sys


class Accumulator:
    def __init__(self, input):

        self.accumulator = 0
        self.executed_instructions = []

        self.next_instruction = 1

        self.instructions = input

        self.stopping_instruction = max(self.instructions.keys()) + 1
        self.stopping_instruction_reached = False

    def check_ins(self, ins):
        if ins == self.stopping_instruction:
            self.stopping_instruction_reached = True
            self.next_instruction = None
        elif ins in self.executed_instructions:
            self.next_instruction = None
        else:
            self.executed_instructions.append(ins)

    def acc(self):
        self.accumulator += self.instructions[self.next_instruction]["value"]
        self.next_instruction += 1

    def jmp(self):
        self.next_instruction += self.instructions[self.next_instruction]["value"]

    def nop(self):
        self.next_instruction += 1

    def process_instructions(self):

        funct = {"acc": self.acc, "jmp": self.jmp, "nop": self.nop}

        while self.next_instruction:
            funct[self.instructions[self.next_instruction]["action"]]()
            self.check_ins(self.next_instruction)

        return self.accumulator

    def debug_instructions(self):
        for ins in self.instructions.keys():
            reset_value = ""
            if self.instructions[ins]["action"] == "acc":
                continue
            elif self.instructions[ins]["action"] == "jmp":
                self.instructions[ins]["action"] = "nop"
                reset_value = "jmp"
            else:
                self.instructions[ins]["action"] = "jmp"
                reset_value = "nop"
            self.process_instructions()

            if self.stopping_instruction_reached:
                return self.accumulator, ins
            else:
                self.next_instruction = 1
                self.accumulator = 0
                self.instructions[ins]["action"] = reset_value
                self.executed_instructions = []


if __name__ == "__main__":

    # Read in the input ... always called `input`
    # Customize depending on the type of data structure required

    # Day 08: Just read text in split into list of lines,
    #         and pass on to Accumulator Class
    with open("input") as f:

        input_dict = {
            idx: {"action": inst.split()[0], "value": int(inst.split()[1])}
            for idx, inst in enumerate(f.read().splitlines(), 1)
        }

    acc = Accumulator(input_dict)
    print(f"Infinite Loop Detected. Accumulator Value: {acc.process_instructions()}")

    print(f"Debugging Instructions ... ")
    acc_val, debug_line = acc.debug_instructions()
    print(f"Debugged line: {debug_line}")
    print(f"Accumulator Value: {acc_val}")
