from data import input
import copy


def int_code(input):
    offset = 0
    opcode = input[offset]
    while opcode != 99:
        val_01 = input[input[offset + 1]]
        val_02 = input[input[offset + 2]]
        dest = input[offset + 3]
        input[dest] = val_01 + val_02 if opcode == 1 else val_01 * val_02
        offset += 4
        opcode = input[offset]

    return input


expected_output = 19690720

for noun in range(0, 100):
    for verb in range(0, 100):
        tmp_input = copy.deepcopy(input)
        tmp_input[1] = noun
        tmp_input[2] = verb
        if int_code(tmp_input)[0] == expected_output:
            print(tmp_input[1:3])
            break
