def calculate_position(values):

    position = depth = 0

    for ins in values:
        if ins[0] == 'forward':
            position += int(ins[1])
        elif ins[0] == 'down':
            depth += int(ins[1])
        elif ins[0] == 'up':
            depth -= int(ins[1])

    return position * depth



if __name__ == "__main__":

    # Read in the input ... always called `input`
    # Customize depending on the type of data structure required

    # Day 01: A simple list of numbers
    with open("input") as f:
        values = [(line.strip().split()) for line in f]

    print(f'Position is: {calculate_position(values)}')
