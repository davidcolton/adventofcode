from itertools import groupby


class ElvesSay:
    def __init__(self, input, repeat):
        self.input = str(input)
        self.repeat = repeat
        self.result = self.input

    def iterate(self):
        count = 0
        if (self.input == "") or (self.repeat == 0):
            pass
        else:
            while count < self.repeat:
                self.result = "".join(
                    str(len(list(g))) + str(k) for k, g in groupby(self.result)
                )
                count += 1
        return len(self.result)


if __name__ == "__main__":
    e = ElvesSay("1113222113", 50)
    print(f"Result (part 1): {e.iterate()}")
