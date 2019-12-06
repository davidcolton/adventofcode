from collections import defaultdict


test = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""

"""
com > b == 1

b > c == 2
b > g == 2

c > d == 3
g > h == 3

d > e == 4
d > i == 4

e > f == 5
e > j == 5

j > k == 6

k > l == 7"""


def count_orbits(orbit_map: str) -> list:
    def _path_to_com(i_orbit: dict, name: str) -> list:
        path_to_com = [name]
        planet = i_orbit[name]
        while planet != "COM":
            path_to_com.append(planet)
            planet = i_orbit[planet]
        path_to_com.append("COM")

        return path_to_com

    orbit_tuples = [(x[0], x[1]) for x in [y.split(")") for y in orbit_map.split()]]

    i_have_orbitors = defaultdict(list)
    i_orbit = dict()
    visited_planets = dict()

    for p, o in orbit_tuples:
        i_have_orbitors[p].append(o)

    for key, values in i_have_orbitors.items():
        for value in values:
            print(value, key)
            i_orbit[value] = key

    planets_to_visit = i_have_orbitors["COM"]
    visited_planets["COM"] = 0

    while len(planets_to_visit) != 0:
        print(f"Planets to visit: {planets_to_visit}")
        visiting = planets_to_visit.pop(0)
        print(f"Currently visiting: {visiting} and I orbit {i_orbit[visiting]}")
        if visiting in i_have_orbitors.keys():
            planets_to_visit.extend(i_have_orbitors[visiting])
        if i_orbit[visiting] in visited_planets.keys():
            visited_planets[visiting] = visited_planets[i_orbit[visiting]] + 1

    # Get full paths to COM
    you_path = _path_to_com(i_orbit, "YOU")
    san_path = _path_to_com(i_orbit, "SAN")

    # Reverse paths to com
    you_path = you_path[::-1]
    san_path = san_path[::-1]

    first_different = min(
        [index for index, elem in enumerate(you_path) if elem != san_path[index]]
    )

    print(you_path[first_different - 1], san_path[first_different - 1])
    print(you_path[first_different], san_path[first_different])

    you_steps_to_com = visited_planets["YOU"]
    san_steps_to_com = visited_planets["SAN"]
    common_steps_to_com = visited_planets[you_path[first_different - 1]]

    you_to_san = (you_steps_to_com - 1 + san_steps_to_com - 1) - (
        common_steps_to_com * 2
    )

    return sum(visited_planets.values()), you_to_san


with open("./input.txt") as f:
    test_orbits = f.read()

print(f"Total Length: {count_orbits(test_orbits)}")
