class WayPoint:
    def __init__(self, input) -> None:

        self.instructions = input

        self.disp = [0, 0]
        self.wp = [10, 1]

        self.functions = {
            "N": self.north,
            "S": self.south,
            "E": self.east,
            "W": self.west,
            "L": self.rotate,
            "R": self.rotate,
            "F": self.forward,
        }

    def north(self, val):
        self.wp[1] += val

    def south(self, val):
        self.wp[1] -= val

    def east(self, val):
        self.wp[0] += val

    def west(self, val):
        self.wp[0] -= val

    def rotate(self, direction, degrees):
        lr = {"L": -1, "R": 1}
        x = self.wp[0]
        y = self.wp[1]

        degrees = (lr[direction] * degrees) % 360
        if degrees == 0:
            self.wp = [x, y]
        elif degrees == 90:
            self.wp = [y, -x]
        elif degrees == 180:
            self.wp = [-x, -y]
        else:
            self.wp = [-y, x]

    def forward(self, val):
        self.disp[0] += self.wp[0] * val
        self.disp[1] += self.wp[1] * val

    def process_instructions(self):

        for ins in self.instructions:
            funct = ins[0]
            val = int(ins[1:])
            if funct in ["L", "R"]:
                self.functions[funct](funct, val)
            else:
                self.functions[funct](val)

        return (self.disp, abs(self.disp[0]) + abs(self.disp[1]))


if __name__ == "__main__":

    # Read in the input ... always called `input`
    # Customize depending on the type of data structure required

    # Day 11: Just read text in
    with open("input") as f:
        input = f.read().splitlines()

    wp = WayPoint(input)
    print(wp.process_instructions())
