from day12_input import day12_input
from collections.abc import Iterable


def common_iterable(obj):
    if isinstance(obj, dict):
        for key in obj:
            yield key
    else:
        for index, value in enumerate(obj):
            yield index


def find_numbers(inp, total_sum):
    # If iterable
    if isinstance(inp, Iterable) and not isinstance(inp, str):
        for obj in common_iterable(inp):
            # Calling a new iterable so reset it's private to 0
            total_sum += find_numbers(inp[obj], 0)
    else:
        if isinstance(inp, int):
            return inp
        else:
            return 0

    return total_sum


def find_numbers_nored(inp, total_sum):
    # If iterable
    if isinstance(inp, Iterable) and not isinstance(inp, str):
        for obj in common_iterable(inp):
            # Check if a Dict with a 'red' value
            if isinstance(inp[obj], dict) and "red" in inp[obj].values():
                next
            else:  # Calling a new iterable so reset it's private to 0
                total_sum += find_numbers_nored(inp[obj], 0)
    else:
        if isinstance(inp, int):
            return inp
        else:
            return 0

    return total_sum


print(f"Total owing: {find_numbers(day12_input, 0)}")
print(f"Total owing (no red): {find_numbers_nored(day12_input, 0)}")
