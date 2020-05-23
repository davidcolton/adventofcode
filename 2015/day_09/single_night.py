from collections import namedtuple
from itertools import permutations
from sys import maxsize

CityPair = namedtuple("CityPair", "origin destination")


class SingleNight:
    def __init__(self, distances):
        self.distances_raw = distances
        self.distances_list = [d.strip() for d in distances.split("\n")]
        self.distances_dict = dict()
        self.cities = set()
        self.min_route_distance = maxsize
        self.min_route = ""
        self.max_route_distance = 0
        self.max_route = ""

    def populate_distances_dict(self):
        for dist in self.distances_list:
            elements = dist.split(" ")
            city_01 = elements[0].strip()
            city_02 = elements[2].strip()
            distance = int(elements[4].strip())

            self.cities.add(city_01)
            self.cities.add(city_02)
            self.distances_dict[CityPair(city_01, city_02)] = distance
            self.distances_dict[CityPair(city_02, city_01)] = distance
        return self

    def calculate_shortest_route(self):

        route_permutations = permutations(self.cities)

        for route in route_permutations:
            distance = sum(
                [
                    self.distances_dict[CityPair(route[i], route[i + 1])]
                    for i in range(len(self.cities) - 1)
                ]
            )

            if distance < self.min_route_distance:
                self.min_route_distance = distance
                self.min_route = str(route)

            if distance > self.max_route_distance:
                self.max_route_distance = distance
                self.max_route = str(route)

        return self

    @property
    def get_min_route(self):
        return self.min_route

    @property
    def get_min_route_distance(self):
        return self.min_route_distance

    @property
    def get_max_route(self):
        return self.max_route

    @property
    def get_max_route_distance(self):
        return self.max_route_distance

    @property
    def get_distances_dict(self):
        return self.distances_dict

    @property
    def get_cities(self):
        return self.cities


if __name__ == "__main__":
    with open("./input.txt", "r") as data:
        inp = data.read()

    sn = SingleNight(inp)
    sn.populate_distances_dict()
    sn.calculate_shortest_route()

    print(f"Part 01: Shortest Route Distance is: {sn.get_min_route_distance}")
    print(sn.get_min_route)
    print()

    print(f"Part 02: Longest Route Distance is: {sn.get_max_route_distance}")
    print(sn.get_max_route)

