def parenthetic_contents(string):
    """Generate parenthesized contents in string as pairs (level, contents)."""
    stack = []
    for i, c in enumerate(string):
        if c == "(":
            stack.append(i)
        elif c == ")" and stack:
            start = stack.pop()
            yield (len(stack), string[start + 1 : i])


def push(obj, l, depth):
    while depth:
        l = l[-1]
        depth -= 1

    l.append(obj)


def parse_parentheses(s):
    groups = []
    depth = 0

    try:
        for char in s:
            if char == "(":
                push([], groups, depth)
                depth += 1
            elif char == ")":
                depth -= 1
            else:
                push(char, groups, depth)
    except IndexError:
        raise ValueError("Parentheses mismatch")

    if depth > 0:
        raise ValueError("Parentheses mismatch")
    else:
        return groups


test_01 = "(((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2)"

print(list(parenthetic_contents(test_01)))
print(parse_parentheses(test_01))