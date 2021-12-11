opening_braces = ['(', '[', '{', '<']
closing_braces = [')', ']', '}', '>']

error_values = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

incomplete_values = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def find_parentheses(input, corrupt=True):
    # The indexes of the open parentheses are stored in a stack, implemented
    # as a list

    errors = []
    incomplete_stacks = []

    for s in input.split('\n'):

        o_stack = []
        c_stack = []

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
                    c_stack = []
                    break
        
        incomplete_stacks.append(c_stack)
        
    if corrupt:
        return sum(error_values[k] for k in errors)
    else:
        return incomplete_stacks

def calculate_incomplete_score(input):

    stacks = find_parentheses(input, corrupt=False)
    stacks = [s for s in stacks if len(s)]

    results = []

    for s in stacks:
        res = 0
        s = s[::-1]
        for b in s:
            res = res * 5
            res = res + incomplete_values[b]

        results.append(res)

    results.sort()

    middle = int((len(results) - 1) / 2)

    return results[middle]



if __name__ == "__main__":

    # Read in the input ... always called `input`
    # Customize depending on the type of data structure required

    # Day 01: A simple list of numbers
    with open("input") as f:
        input = f.read()

    print(f'Part 01: {find_parentheses(input)}')
    print(f'Part 01: {calculate_incomplete_score(input)}')

