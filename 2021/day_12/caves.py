from collections import defaultdict


def read_paths(input):

    paths = defaultdict(list)

    for p in input.splitlines():
        a, b = p.split("-")
        paths[a].append(b)
        paths[b].append(a)

    return paths


# twice_visited = True
# A node has been visited twice and we can't do it again
def path_count(paths, node, visited=set(), twice_visited=False):

    if node == "end":
        return 1
    count = 0
    new_visited = visited | {node} if node.islower() else visited

    for to in paths[node]:
        if to == "start":
            continue
        if to in visited:
            if twice_visited:
                continue
            count += path_count(paths, to, new_visited, True)
        else:
            count += path_count(paths, to, new_visited, twice_visited)
    return count


if __name__ == "__main__":

    # Read in the input ... always called `input`
    # Customize depending on the type of data structure required

    # Day 12: A string
    with open("input") as f:
        input = f.read()

    paths = read_paths(input)

    print(f'PART 01: {path_count(paths, "start", twice_visited=True)}')
    print(f'PART 02: {path_count(paths, "start")}')
