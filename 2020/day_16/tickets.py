from itertools import chain


class Ticket:
    def __init__(self, input):

        ins, my_t, other_t = input.split("\n\n")

        self.fields = self.process_fields(ins)
        self.all_valid_field_values = self.all_valid_fields()

        self.my_ticket = [int(n) for n in my_t.split("\n")[1].split(",")]

        self.other_tickets = [
            [int(n) for n in t.split(",")] for t in other_t.strip().split("\n")[1:]
        ]
        self.all_other_tickets = [
            int(n) for t in other_t.strip().split("\n")[1:] for n in t.split(",")
        ]

    def process_fields(self, ins):
        return_dict = {}
        for line in ins.strip().splitlines():
            field, values = line.split(":")
            r1, r2 = values.strip().split(" or ")
            range_01 = int(r1.split("-")[0]), int(r1.split("-")[1].strip()) + 1
            range_02 = int(r2.split("-")[0]), int(r2.split("-")[1].strip()) + 1
            return_dict[field] = list(
                chain(range(range_01[0], range_01[1]), range(range_02[0], range_02[1]))
            )

        return return_dict

    def all_valid_fields(self):
        return set(n for v in self.fields.values() for n in v)

    def invalid_numbers_total(self):
        return sum(
            n for n in self.all_other_tickets if n not in self.all_valid_field_values
        )


if __name__ == "__main__":

    # Read in the input ... always called `input`
    # Customize depending on the type of data structure required

    # Day 11: Just read text in
    with open("input") as f:
        input = f.read()

    tic = Ticket(input)
    print(tic.other_tickets[0])
    print(tic.invalid_numbers_total())