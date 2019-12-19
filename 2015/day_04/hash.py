import hashlib


def calculate_matching_hash(starts_with, zeros):
    zeros_to_find = range(1, zeros + 1)
    n = 0
    for z in zeros_to_find:
        while True:
            text_to_hash = f"{starts_with}{n}"
            h = hashlib.md5(text_to_hash.encode("utf-8")).hexdigest()
            if h.startswith("0" * z):
                print(f"The hash that starts with {z} zeros is: {h}")
                print(f"The input value to produce this hash is {text_to_hash}")
                print(f"The suffix added to {starts_with} is {n}\n")
                break
            n += 1


if __name__ == "__main__":

    calculate_matching_hash("bgvyzdsv", 6)

