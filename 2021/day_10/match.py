opening_braces = ['(', '[', '{', '<']
closing_braces = [')', ']', '}', '>']

error_values = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

"""input = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''"""

def find_parentheses(input):
    # The indexes of the open parentheses are stored in a stack, implemented
    # as a list

    errors = []

    o_stack = []
    c_stack = []

    for s in input.split('\n'):
        for i, c in enumerate(s.strip()):
            if c in opening_braces:
                o_stack.append(i)
                if c == '(': c_stack.append(')')
                if c == '[': c_stack.append(']')
                if c == '{': c_stack.append('}')
                if c == '<': c_stack.append('>')
            elif c in closing_braces:
                if c == c_stack[-1]:
                    c_stack = c_stack[:-1]
                else:
                    errors.append(c)
                    break
        
    return sum(error_values[k] for k in errors)



if __name__ == "__main__":

    # Read in the input ... always called `input`
    # Customize depending on the type of data structure required

    # Day 01: A simple list of numbers
    with open("input") as f:
        input = f.read()

    print(f'Part 01: {find_parentheses(input)}')



