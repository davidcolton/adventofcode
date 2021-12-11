import pytest
from match import find_parentheses, calculate_incomplete_score

input = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''

@pytest.mark.parametrize(
    "input, expected",
    [
        (input, 26397),
    ],
)
def test_find_parentheses(input, expected):
    assert find_parentheses(input) == expected

@pytest.mark.parametrize(
    "input, expected",
    [
        (input, 288957),
    ],
)
def test_calculate_incomplete_score(input, expected):
    assert calculate_incomplete_score(input) == expected
