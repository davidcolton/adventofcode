class Navigate:
    def __init__(self, input) -> None:

        self.instructions = input

        self.x = 0
        self.y = 0

        self.direction = "E"
        self.direction_pointer = 0

        self.functions = {
            "N": self.north,
            "S": self.south,
            "E": self.east,
            "W": self.west,
            "L": self.left,
            "R": self.right,
            "F": self.forward,
        }

        self.orientations = ["E", "S", "W", "N"]

    def north(self, val):
        self.y += val

    def south(self, val):
        self.y -= val

    def east(self, val):
        self.x += val

    def west(self, val):
        self.x -= val

    def left(self, val):
        self.direction_pointer = self.direction_pointer - int(val / 90)
        self.direction = self.orientations[
            self.direction_pointer % len(self.orientations)
        ]

    def right(self, val):
        self.direction_pointer = self.direction_pointer + int(val / 90)
        self.direction = self.orientations[
            self.direction_pointer % len(self.orientations)
        ]

    def forward(self, val):
        self.functions[self.direction](val)

    def process_instructions(self):

        for ins in self.instructions:
            funct = ins[0]
            val = int(ins[1:])
            self.functions[funct](val)

        return (self.x, self.y, abs(self.x) + abs(self.y))


if __name__ == "__main__":

    # Read in the input ... always called `input`
    # Customize depending on the type of data structure required

    # Day 11: Just read text in
    with open("input") as f:
        input = f.read().splitlines()

    nav = Navigate(input)
    print(nav.process_instructions())