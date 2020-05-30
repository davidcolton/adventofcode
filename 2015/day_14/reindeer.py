from collections import namedtuple
from collections import defaultdict

Reindeer = namedtuple("Reindeer", "name flying_speed flying_duration rest_duration")
Distance = namedtuple("Distance", "name distance")


def process_reindeer_stats(stats):
    reindeers = []
    for deer in stats:
        words = [word for word in deer.split(" ")]
        reindeers.append(
            Reindeer(words[0], int(words[3]), int(words[6]), int(words[-2]))
        )
    return reindeers


def calculate_distance_travelled(reindeer, seconds):
    distances = []
    for deer in reindeer:
        full_cycles_distance = (
            deer.flying_speed
            * deer.flying_duration
            * (seconds // (deer.flying_duration + deer.rest_duration))
        )
        partial_cycle = seconds % (deer.flying_duration + deer.rest_duration)
        if partial_cycle >= deer.flying_duration:
            partial_distance = deer.flying_speed * deer.flying_duration
        else:
            partial_distance = deer.flying_speed * partial_cycle
        distances.append(Distance(deer.name, full_cycles_distance + partial_distance))

    return distances


def calculate_bonus_points(reindeer, seconds):
    distances_record = defaultdict(list)
    bonus_points = defaultdict(int)
    for seconds in range(1, seconds + 1):
        distances = calculate_distance_travelled(reindeer, seconds)
        _, max_dist = max(distances, key=lambda x: x.distance)
        for deer in distances:
            distances_record[deer.name].append(deer.distance)
            if deer.distance == max_dist:
                bonus_points[deer.name] += 1
    return bonus_points


if __name__ == "__main__":

    with open("./input.txt", "r") as f:
        stats = f.read().strip().split("\n")

    # Read the Reindeer information into a list of NamedTuples
    processed_stats = process_reindeer_stats(stats)

    # Get the total distances travelled
    distances_travelled = calculate_distance_travelled(processed_stats, 2503)

    # Calculate the bonus points
    # Call calculate distance for each second
    bonus_points = calculate_bonus_points(processed_stats, 2503)

    # Add the distances to the bonus points
    for deer in distances_travelled:
        print(
            f"{deer.name}, Bonus: {bonus_points[deer.name]}, Distance: {deer.distance}"
        )
