import numpy as np


class ChristmasLights:
    def __init__(self, grid_size, instructions):
        self.__grid = np.zeros([grid_size, grid_size], dtype=int)
        self.__instructions = [
            line.strip() for line in instructions.split("\n") if line != ""
        ]

    def __process_grid_coordinates(self, s1, s2):
        x1 = int(s1.split(",")[0])
        y1 = int(s1.split(",")[1])

        # x2 & y2 are + 1 because we are using matrix slices
        #    e.g. x1, x2 = 2, 4 only returns rows 2 up to but
        #         not including row 4 i.e. rows 2 & 3 only
        x2 = int(s2.split(",")[0]) + 1
        y2 = int(s2.split(",")[1]) + 1

        return x1, x2, y1, y2

    def turn_on(self, s1, s2):
        x1, x2, y1, y2 = self.__process_grid_coordinates(s1, s2)
        self.__grid[x1:x2, y1:y2] = 1
        return self

    def turn_off(self, s1, s2):
        x1, x2, y1, y2 = self.__process_grid_coordinates(s1, s2)
        self.__grid[x1:x2, y1:y2] = 0
        return self

    def toggle(self, s1, s2):
        x1, x2, y1, y2 = self.__process_grid_coordinates(s1, s2)
        self.__grid[x1:x2, y1:y2] += 1
        self.__grid[x1:x2, y1:y2] = self.__grid[x1:x2, y1:y2] % 2
        return self

    def follow_instructions(self):
        for ins in self.__instructions:
            if ins.startswith("toggle"):
                s1, _, s2 = ins[7:].split()
                self.toggle(s1, s2)
            elif ins.startswith("turn on"):
                s1, _, s2 = ins[8:].split()
                self.turn_on(s1, s2)
            else:
                s1, _, s2 = ins[9:].split()
                self.turn_off(s1, s2)
        return self

    @property
    def lights_on(self):
        return self.__grid.sum()


# Need to refactor to have a base ChristmasLights Class and
#    then a ChristmasLights1 & ChristmasLights2 subclasses
#    This will remove nearly all of the repetition
class ChristmasLights2:
    def __init__(self, grid_size, instructions):
        self.__grid = np.zeros([grid_size, grid_size], dtype=int)
        self.__instructions = [
            line.strip() for line in instructions.split("\n") if line != ""
        ]

    def __process_grid_coordinates(self, s1, s2):
        x1 = int(s1.split(",")[0])
        y1 = int(s1.split(",")[1])

        # x2 & y2 are + 1 because we are using matrix slices
        #    e.g. x1, x2 = 2, 4 only returns rows 2 up to but
        #         not including row 4 i.e. rows 2 & 3 only
        x2 = int(s2.split(",")[0]) + 1
        y2 = int(s2.split(",")[1]) + 1

        return x1, x2, y1, y2

    def turn_on(self, s1, s2):
        x1, x2, y1, y2 = self.__process_grid_coordinates(s1, s2)
        self.__grid[x1:x2, y1:y2] += 1
        return self

    def turn_off(self, s1, s2):
        x1, x2, y1, y2 = self.__process_grid_coordinates(s1, s2)
        self.__grid[x1:x2, y1:y2] -= 1
        self.__grid[self.__grid < 0] = 0
        return self

    def toggle(self, s1, s2):
        x1, x2, y1, y2 = self.__process_grid_coordinates(s1, s2)
        self.__grid[x1:x2, y1:y2] += 2
        return self

    def follow_instructions(self):
        for ins in self.__instructions:
            if ins.startswith("toggle"):
                s1, _, s2 = ins[7:].split()
                self.toggle(s1, s2)
            elif ins.startswith("turn on"):
                s1, _, s2 = ins[8:].split()
                self.turn_on(s1, s2)
            else:
                s1, _, s2 = ins[9:].split()
                self.turn_off(s1, s2)
        return self

    @property
    def lights_on(self):
        return self.__grid.sum()


if __name__ == "__main__":
    with open("./input.txt", "r") as f:
        instructions = f.read()

    lights = ChristmasLights(1000, instructions)
    lights.follow_instructions()
    print(f"Part 01:\nNumber of Lights on: {lights.lights_on}\n")

    lights2 = ChristmasLights2(1000, instructions)
    lights2.follow_instructions()
    print(f"Part 02:\nBrightness of Lights: {lights2.lights_on}\n")
