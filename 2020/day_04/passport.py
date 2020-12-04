from voluptuous import Schema, Required, All, Range, Invalid, error
import string


def check_height(value):
    if "cm" in value or "in" in value:
        units = value[-2:]
        value = int(value[:-2])
        if (units == "cm" and 150 <= value <= 193) or (
            units == "in" and 59 <= value <= 76
        ):
            return value
    raise Invalid("Not a valid height")


def check_hair_colour(value):
    if value[0] == "#" and all(ch in string.hexdigits for ch in value[1:].lower()):
        return value
    else:
        raise Invalid("Not a valid hair colour")


def check_eye_colour(value):
    if value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return value
    else:
        raise Invalid("Not a valid eye colour")


def check_passport_id(value):
    if len(value) == 9 and all(ch in string.digits for ch in value):
        return value
    else:
        raise Invalid("Not a valid passport")


schema = Schema(
    {
        Required("byr"): All(int, Range(min=1920, max=2002)),
        Required("iyr"): All(int, Range(min=2010, max=2020)),
        Required("eyr"): All(int, Range(min=2020, max=2030)),
        Required("hgt"): check_height,
        Required("hcl"): check_hair_colour,
        Required("ecl"): check_eye_colour,
        Required("pid"): check_passport_id,
    },
    extra=True,
)


def passport_list_to_dict(input):
    # Takes a list of lists and returns a list of dictionaries
    passport_list = [l.replace("\n", " ").strip().split() for l in input.split("\n\n")]
    passports = [
        dict(key_value.split(":") for key_value in passport)
        for passport in passport_list
    ]

    year_types = ["byr", "iyr", "eyr"]

    # Fix year value type to be ints
    for passport in passports:
        for key_name in year_types:
            if key_name in passport.keys():
                passport[key_name] = int(passport[key_name])

    return passports


def simple_validation(input):
    passports = passport_list_to_dict(input)
    total_passports = len(passports)
    invalid_passports = sum(
        [1 for p in passports if len(p) < 7 or (len(p) == 7 and "cid" in p.keys())]
    )

    return total_passports - invalid_passports


def advanced_validation(input):
    passports = passport_list_to_dict(input)

    valid_passports = 0

    for passport in passports:
        try:
            schema(passport)
            valid_passports += 1
        except error.MultipleInvalid:
            pass

    return valid_passports


if __name__ == "__main__":

    # Read in the input ... always called `input`
    # Customize depending on the type of data structure required

    # Day 04: A simple list
    # Split on \n\n and then strip \n
    with open("input") as f:
        input = f.read()

    print(f"Simple Test Valid Passports: {simple_validation(input)}")
    print(f"Advanced Test Valid Passports: {advanced_validation(input)}")
