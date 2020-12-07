import pytest
from baggage import input_to_graph, count_bags, count_predecessors

test_01 = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

DG = input_to_graph(test_01.split("\n"))


@pytest.mark.parametrize(
    "graph, start_node, expected",
    [
        (DG, "shiny_gold", 4),
    ],
)
def test_count_predecessors(graph, start_node, expected):
    assert count_predecessors(graph, start_node) == expected


@pytest.mark.parametrize(
    "graph, start_node, expected",
    [
        (DG, "shiny_gold", 32),
    ],
)
def test_count_bags(graph, start_node, expected):
    assert count_bags(graph, start_node) - 1 == expected