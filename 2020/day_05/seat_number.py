# F = 0
# B = 1
# R = 1
# L = 0


def binary_decimal(n):
    return int(n, 2)


def get_seat_numbers(input):
    seat_numbers = []
    for seat_code in input:
        row = binary_decimal(seat_code[:7].replace("F", "0").replace("B", "1"))
        seat = binary_decimal(seat_code[7:].replace("R", "1").replace("L", "0"))
        seat_numbers.append(row * 8 + seat)
    return seat_numbers


def find_my_seat(input):
    first_seat = min(input)
    sorted_seats = sorted(input)
    for idx, seat in enumerate(sorted_seats, first_seat):
        if idx != seat:
            return idx


if __name__ == "__main__":

    # Read in the input ... always called `input`
    # Customize depending on the type of data structure required

    # Day 05: A simple list
    with open("input") as f:
        input = f.read().splitlines()

    seat_numbers = get_seat_numbers(input)
    print(f"The maximum seat number is {max(seat_numbers)}")

    sorted_seats = sorted(get_seat_numbers(input))
    print(f"Santa's seat number is {find_my_seat(seat_numbers)}")