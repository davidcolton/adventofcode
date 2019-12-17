from collections import Counter


class Floor:
    def __init__(self, input):
        self.__instructions = [i for i in input]
        self.__floors_counter = Counter(input)
        self.__floor = 0
        self.__moves = 0

    def final_floor(self):
        return f"Santa is on floor: {self.__floors_counter['('] - self.__floors_counter[')']}"

    def move_up_floor(self):
        self.__floor += 1
        return self

    def move_down_floor(self):
        self.__floor -= 1
        return self

    def first_basement_visit(self):
        while self.__instructions and self.__floor >= 0:
            self.__moves += 1
            inst = self.__instructions.pop(0)
            self.move_up_floor() if inst == "(" else self.move_down_floor()
        return f"Santa first went to the basement on move {self.__moves}"


with open("./input.txt", "r") as f:
    floors = f.read()

santa = Floor(floors)

print(santa.final_floor())
print(santa.first_basement_visit())
