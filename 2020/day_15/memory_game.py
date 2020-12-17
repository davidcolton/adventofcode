def memory_game(input, length):
    numbers = [int(n) for n in input.split(",")]
    spoken = {number: [idx] for idx, number in enumerate(numbers, 1)}
    most_recent = numbers[-1]
    for turn in range(len(spoken) + 1, length + 1):
        most_recent = (
            0
            if len(spoken[most_recent]) == 1
            else spoken[most_recent][-1] - spoken[most_recent][-2]
        )
        spoken[most_recent] = (
            (turn,)
            if len(spoken.get(most_recent, ())) == 0
            else (spoken[most_recent][-1], turn)
        )
    return most_recent


if __name__ == "__main__":

    input = "0,8,15,2,12,1,4"

    print(f"Part 1: {memory_game(input, 2020)}")
    print(f"Part 2: {memory_game(input, 30000000)}")
