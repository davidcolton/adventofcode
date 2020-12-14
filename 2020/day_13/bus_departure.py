from math import prod


def chinese_remainder(n, a):
    p = prod(n)
    total = sum(y * pow(p // x, -1, x) * (p // x) for x, y in zip(n, a))
    return total % p


def perfect_timing(input):
    _, schedule = input
    n = []
    a = []
    for idx, num in enumerate(schedule.split(",")):
        if num == "x":
            continue
        n.append(int(num))
        a.append(int(num) - idx)

    return chinese_remainder(n, a)


def next_bus(input):

    current_time, schedule = input

    current_time = int(current_time)

    next_bus = []

    for sch in schedule.split(","):
        if sch == "x":
            continue
        sch = int(sch)
        last_bus_left = current_time % sch
        next_bus.append(((sch - last_bus_left), sch, sch * (sch - last_bus_left)))

    return min(next_bus)


if __name__ == "__main__":

    # Read in the input ... always called `input`
    # Customize depending on the type of data structure required

    # Day 13: Just read text in
    with open("input") as f:
        input = f.read().splitlines()

    next_bus = next_bus(input)
    print(f"Bus {next_bus[1]} will leave in {next_bus[0]} minutes.")
    print(f"The answer is {next_bus[2]}")

    print(f"The perfect time stamp is: {perfect_timing(input)}")
