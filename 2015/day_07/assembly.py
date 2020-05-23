class Assembly:

    MAX_SIZE = 65535

    def __init__(self, instructions):
        self.instructions_raw = instructions
        self.instructions_list = [ins for ins in instructions.split("\n")]
        self.instructions_unresolved = dict()
        self.instructions_resolved = dict()
        self.instructions_in_progress = []

    def ingest_instructions(self):
        for ins in self.instructions_list:
            left_hand_side, right_hand_side = ins.split("->")
            if left_hand_side.strip().isnumeric():
                self.instructions_resolved[right_hand_side.strip()] = int(
                    left_hand_side.strip()
                )
            else:
                self.instructions_unresolved[
                    left_hand_side.strip()
                ] = right_hand_side.strip()
        return self

    def shift_left(self, value, amount):
        if value in self.instructions_resolved:
            return self.instructions_resolved[value] << amount
        else:
            return "Not Processed"

    def shift_right(self, value, amount):
        if value in self.instructions_resolved:
            return self.instructions_resolved[value] >> amount
        else:
            return "Not Processed"

    def logical_not(self, value):
        if value in self.instructions_resolved:
            return self.MAX_SIZE - self.instructions_resolved[value]
        else:
            return "Not Processed"

    def logical_and(self, value_01, value_02):
        if (
            value_01 in self.instructions_resolved
            and value_02 in self.instructions_resolved
        ):
            return (
                self.instructions_resolved[value_01]
                & self.instructions_resolved[value_02]
            )
        elif isinstance(value_01, int) and value_02 in self.instructions_resolved:
            return value_01 & self.instructions_resolved[value_02]
        else:
            return "Not Processed"

    def logical_or(self, value_01, value_02):
        if (
            value_01 in self.instructions_resolved
            and value_02 in self.instructions_resolved
        ):
            return (
                self.instructions_resolved[value_01]
                | self.instructions_resolved[value_02]
            )
        elif isinstance(value_01, int) and value_02 in self.instructions_resolved:
            return value_01 | self.instructions_resolved[value_02]
        else:
            return "Not Processed"

    def process_instructions(self):
        ins_dict = {
            "LSHIFT": self.shift_left,
            "RSHIFT": self.shift_right,
            "NOT": self.logical_not,
            "AND": self.logical_and,
            "OR": self.logical_or,
        }
        while len(self.instructions_unresolved) > 0:
            for ins, target in self.instructions_unresolved.items():
                if "NOT" in ins:
                    action, value_01 = ins.strip().split()
                    resolved = ins_dict[action](value_01)
                    if resolved != "Not Processed":
                        self.instructions_resolved[target] = int(resolved)
                        self.instructions_in_progress.append(ins)

                elif "LSHIFT" in ins or "RSHIFT" in ins:
                    value_01, action, amount = ins.strip().split()
                    resolved = ins_dict[action](value_01, int(amount))
                    if resolved != "Not Processed":
                        self.instructions_resolved[target] = int(resolved)
                        self.instructions_in_progress.append(ins)

                elif "AND" in ins or "OR" in ins:
                    value_01, action, value_02 = ins.strip().split()
                    if value_01.isnumeric():
                        value_01 = int(value_01)
                    resolved = ins_dict[action](value_01, value_02)
                    if resolved != "Not Processed":
                        self.instructions_resolved[target] = int(resolved)
                        self.instructions_in_progress.append(ins)

                else:
                    if ins.strip() in self.instructions_resolved:
                        self.instructions_resolved[target] = self.instructions_resolved[
                            ins
                        ]
                        self.instructions_in_progress.append(ins)

            for ins in self.instructions_in_progress:
                if ins in self.instructions_unresolved:
                    del self.instructions_unresolved[ins]

            self.instructions_in_progress = []

        return self

    @property
    def resolved(self):
        return self.instructions_resolved

    @property
    def unresolved(self):
        return self.instructions_unresolved

    def get_resolved_value(self, value):
        return self.instructions_resolved[value]

    def set_value(self, ins, value):
        self.instructions_resolved[ins] = value
        return self


if __name__ == "__main__":
    with open("./input.txt", "r") as f:
        instructions = f.read()

    assembly = Assembly(instructions)
    assembly.ingest_instructions()
    assembly.process_instructions()

    part_01_result = assembly.get_resolved_value("a")
    print(f'Part 01: The signal on wire "a" is: {part_01_result}')

    assembly_02 = Assembly(instructions)
    assembly_02.ingest_instructions()
    assembly_02.set_value("b", part_01_result)
    assembly_02.process_instructions()

    part_02_result = assembly_02.get_resolved_value("a")
    print(f'Part 02: The signal on wire "a" is: {part_02_result}')

