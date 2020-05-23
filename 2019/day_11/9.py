from IntCodes import IntCodes

runner = IntCodes()
with open("input.txt") as lines:
    i = 0
    for line in lines:
        program = list(map(int, line.strip().split(",")))
        output = list(runner.run_program(program, [0]))
        print("case " + str(i), output)
        i += 1

