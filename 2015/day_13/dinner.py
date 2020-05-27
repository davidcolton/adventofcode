from collections import defaultdict
from itertools import permutations


class DinnerTable:
    def __init__(self, instructions) -> None:
        self.ins = instructions
        self.happiness_scores = {}
        self.guest_list = []

    def process_happiness_scores(self):
        lines = [line for line in self.ins.split("\n") if line != ""]
        for line in lines:
            elements = line.split()
            name = elements[0].strip()
            pos_neg = 0
            if elements[2].strip() == "gain":
                pos_neg = 1
            else:
                pos_neg = -1
            score = int(elements[3].strip())
            neighbour = elements[-1][:-1]
            if name not in self.happiness_scores.keys():
                self.happiness_scores[name] = {}
            self.happiness_scores[name].update({neighbour: score * pos_neg})

        self.guest_list = list(self.happiness_scores.keys())

    def add_host_to_happiness_scores(self):
        self.happiness_scores["Host"] = {}
        self.guest_list = list(self.happiness_scores.keys())
        for guest in self.guest_list:
            self.happiness_scores["Host"].update({guest: 0})
            self.happiness_scores[guest].update({"Host": 0})

    def seating_plan_naive(self):
        possible_plans = permutations(self.guest_list)
        possible_plans = [p + (p[0],) for p in possible_plans]

        best_plan = []
        best_plan_score = 0

        for plan in possible_plans:
            happiness = 0
            first = plan[0]
            for neighbour in plan[1:]:
                happiness += self.happiness_scores[first][neighbour]
                happiness += self.happiness_scores[neighbour][first]
                first = neighbour
            if happiness > best_plan_score:
                best_plan_score = happiness
                best_plan = plan
        print(
            f"The happiest plan {best_plan} with a happiness score of {best_plan_score}."
        )

        return best_plan_score


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        instructions = f.read()

    dt = DinnerTable(instructions)
    dt.process_happiness_scores()
    dt.add_host_to_happiness_scores()
    dt.seating_plan_naive()
