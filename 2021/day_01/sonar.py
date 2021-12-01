def examine_sonar(input):
    increases = 0
    for position in range(len(input) - 1):
        if input[position + 1] > input[position]:
            increases += 1

    print(f"Solution Found: {increases}")
    return increases



if __name__ == "__main__":

    # Read in the input ... always called `input`
    # Customize depending on the type of data structure required

    # Day 01: A simple list of numbers
    with open("input") as f:
        values = [int(line.strip()) for line in f]

    answer = examine_sonar(values)

