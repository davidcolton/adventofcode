import pytest
from dinner import DinnerTable

scores = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol."""


@pytest.mark.parametrize("arg, expected", [(scores, 330)])
def test_seating_plan(arg, expected):
    dt = DinnerTable(arg)
    dt.process_happiness_scores()
    result = dt.seating_plan_naive()
    assert result == expected


@pytest.mark.parametrize("arg, expected", [(scores, 286)])
def test_seating_plan_withhost(arg, expected):
    dt = DinnerTable(arg)
    dt.process_happiness_scores()
    dt.add_host_to_happiness_scores()
    result = dt.seating_plan_naive()
    assert result == expected
