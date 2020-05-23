import pytest
from new_password import NewPassword


@pytest.mark.parametrize(
    "arg, expected",
    [
        ("abcdefgh", False),
        ("abcdffaa", True),
        ("ghijklmn", False),
        ("ghjaabcc", True),
        ("abbcegjk", False),
    ],
)
def test_pairs_test(arg, expected):
    np = NewPassword(arg)
    result = np.pairs_test(arg)
    assert result == expected


@pytest.mark.parametrize(
    "arg, expected",
    [
        ("abcdefgh", True),
        ("abdeghkm", False),
        ("abcdffaa", True),
        ("ghjaabcc", True),
        ("abbcegjk", False),
    ],
)
def test_three_straight_test(arg, expected):
    np = NewPassword(arg)
    result = np.three_straight_test(arg)
    assert result == expected


@pytest.mark.parametrize(
    "arg, expected",
    [
        ("abcdefgh", True),
        ("abdeghkm", False),
        ("abcdffaa", True),
        ("ghjaabcc", True),
        ("abbcegjk", False),
    ],
)
def test_three_straight_test(arg, expected):
    np = NewPassword(arg)
    result = np.three_straight_test(arg)
    assert result == expected


@pytest.mark.parametrize(
    "arg, expected",
    [
        ("abcdffaa", "abcdffab"),
        ("ghjaabcc", "ghjaabcd"),
        ("zzzzzzzz", "aaaaaaaa"),
        ("aaaaaaaz", "aaaaaaba"),
        ("aaaaaaah", "aaaaaaaj"),
    ],
)
def test_add_letter(arg, expected):
    np = NewPassword(arg)
    result = np.add_letter(arg)
    assert result == expected
