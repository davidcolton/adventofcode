import pytest
from reindeer import process_reindeer_stats
from reindeer import calculate_distance_travelled
from reindeer import calculate_bonus_points

from collections import namedtuple

Reindeer = namedtuple("Reindeer", "name flying_speed flying_duration rest_duration")
Distance = namedtuple("Distance", "name distance")

reindeers = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""


@pytest.mark.parametrize("arg, expected", [(reindeers, [1120, 1056])])
def test_calculate_distance_travelled(arg, expected):
    results = calculate_distance_travelled(
        process_reindeer_stats(reindeers.split("\n")), 1000
    )
    results = sorted(results, key=lambda x: -x.distance)
    for idx, res in enumerate(results):
        assert res.distance == expected[idx]


@pytest.mark.parametrize("arg, expected", [(reindeers, {"Dancer": 689, "Comet": 312})])
def test_calculate_bonus_points(arg, expected):
    results = calculate_bonus_points(
        process_reindeer_stats(reindeers.split("\n")), 1000
    )
    for key, val in results.items():
        assert val == expected[key]
