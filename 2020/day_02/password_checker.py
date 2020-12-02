from collections import Counter


def process_password_definition(password_definition):
    # Process the line contain the password policy and the password
    letter_range, letter, password = password_definition.split()
    lower, upper = letter_range.split("-")
    letter = letter[0]
    return int(lower), int(upper), letter, password


def password_checker(password_list):
    valid_passowrds = 0

    for password_definition in password_list:
        lower, upper, letter, password = process_password_definition(
            password_definition
        )

        # Use a Counter to get a count of each letter in the password
        password_letters = Counter(password)

        # Is the letter the requisite times in the password
        if lower <= password_letters[letter] <= upper:
            valid_passowrds += 1

    return valid_passowrds


def positional_password_checker(password_list):
    valid_passwords = 0

    for password_definition in password_list:
        lower, upper, letter, password = process_password_definition(
            password_definition
        )

        # The positional locater and 1 indexed
        # Need to handle 0 indexed string
        if bool(password[lower - 1] == letter) ^ bool(password[upper - 1] == letter):
            valid_passwords += 1

    return valid_passwords


if __name__ == "__main__":

    # Read in the input ... always called `input`
    # Customize depending on the type of data structure required

    # Day 02: A simple list
    with open("input") as f:
        values = [line.strip() for line in f]

    print(f"Number of valid Sled passwords: {password_checker(values)}")
    print(f"Number of valid Toboggan passwords: {positional_password_checker(values)}")
