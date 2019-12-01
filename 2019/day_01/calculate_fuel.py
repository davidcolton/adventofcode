from data import masses


def calculate_fuel(mass):
    return (mass // 3) - 2


def calculate_fuel_complex(mass):
    fuel = calculate_fuel(mass)

    # Base case: Fuel == 0
    if fuel <= 0:
        return 0

    # Recursive case:
    else:
        return fuel + calculate_fuel_complex(fuel)


def simple_fuel(list_of_masses):
    return sum(calculate_fuel(m) for m in list_of_masses)


def complex_fuel(list_of_masses):
    return sum(calculate_fuel_complex(m) for m in list_of_masses)


simple_total = simple_fuel(masses)
complex_total = complex_fuel(masses)

print(f"Fuel calculated using simple method:  {simple_total}")
print(f"Fuel calculated using complex method: {complex_total}")

