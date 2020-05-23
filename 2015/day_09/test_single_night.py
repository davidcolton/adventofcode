import pytest
from single_night import SingleNight


@pytest.fixture()
def test_distances():
    return """London to Dublin = 464
              London to Belfast = 518
              Dublin to Belfast = 141"""


def test_min_max_routes(test_distances):
    sn = SingleNight(test_distances)
    sn.populate_distances_dict()
    sn.calculate_shortest_route()
    assert sn.get_min_route_distance == 605
    assert sn.get_max_route_distance == 982
