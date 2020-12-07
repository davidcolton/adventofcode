import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


def clean_contens_list(input):
    contents_list = []
    for bag in input:
        bag_elements = bag.strip().split()
        if bag_elements[0] == "no":
            bag_colour = None
            number_of_bags = 0
        else:
            bag_colour = "_".join(bag_elements[1:-1])
            number_of_bags = int(bag_elements[0])
        contents_list.append((bag_colour, number_of_bags))
    return contents_list


def input_to_graph(input):

    DG = nx.DiGraph()

    for rule in input:
        # Split on text 'bags contain'
        bag, contents = rule.split("bags contain")
        bag = bag.strip().replace(" ", "_")

        # If the is a comma in contents then there is more than
        #     1 bag type contain
        if "," in contents:
            contents_list = contents.split(",")
        else:
            contents_list = [contents]

        # Clean the contents of each bag and get in a format
        #     that will allow me to create the graph
        clean_contents = clean_contens_list(contents_list)

        # Now iterate over the contents and add an edge per bag
        for inner_bag in clean_contents:
            if inner_bag[0] is None:
                continue
            DG.add_edges_from([(bag, inner_bag[0])], weight=inner_bag[1])

    return DG


def count_predecessors(dg, start_node):
    stack = list(dg.predecessors(start_node))
    predecessors_set = set()
    predecessors_set.update(stack)

    while stack:
        node = stack.pop()
        predecessors = list(dg.predecessors(node))
        predecessors_set.update(predecessors)
        stack += predecessors

    return len(predecessors_set)


def count_bags(graph, node):
    return 1 + sum(
        v["weight"] * count_bags(graph, k)
        for k, v in graph[node].items()
        if graph[node]
    )


if __name__ == "__main__":

    # Read in the input ... always called `input`
    # Customize depending on the type of data structure required

    # Day 07: Just read text in split into list of lines,
    #         and pass on to next function
    with open("input") as f:
        input = f.read().splitlines()

    # Create a network graph from the input
    DG = input_to_graph(input)

    print(
        f"Part 1: Bag colours that can contain a shiny gold bag: {count_predecessors(DG, 'shiny_gold')}"
    )
    print(
        f"Part 2: Number of bags in a shiny gold bag: {count_bags(DG, 'shiny_gold') - 1}"
    )

    """nx.draw(
        sub_DG,
        with_labels=True,
        node_size=100,
        node_color="skyblue",
        node_shape="o",
        alpha=0.5,
        linewidths=1,
        font_size=8,
        font_color="grey",
        font_weight="bold",
        width=2,
        edge_color="grey",
    )
    plt.show()"""
