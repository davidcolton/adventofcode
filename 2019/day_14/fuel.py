from collections import namedtuple

Ingredient = namedtuple("Ingredient", "ingredient quantity ore_cost")

with open("./test_input_01.txt", "r") as f:
    raw_ingredients = f.readlines()

ingredients_dict = dict()

for line in raw_ingredients:
    inputs, output = line.strip().split("=>")

    # Get the name or the output and the quantity produced
    units_produced, output_name = output.strip().split()

    # List of ingredients
    list_of_ingredients = []

    # Get all of the input ingredients
    for ing in inputs.split(","):
        quantity_required, input_name = ing.strip().split()
        list_of_ingredients.append((input_name, int(quantity_required)))
        ore_cost = int(quantity_required) if input_name == "ORE" else 0

    ingredients_dict[output_name] = {
        "units_produced": int(units_produced),
        "ore_cost": ore_cost,
        "ingredients": list_of_ingredients,
    }

print(ingredients_dict)


def get_ore_cost(ingredient):
    if ingredients_dict[ingredient]["ore_cost"] != 0:
        return ingredients_dict[ingredient]["ore_cost"]


"""# while raw_ingredients_dict["FUEL"]["ore_cost"] == 0:
for item in ingredients_dict["FUEL"]["ingredients"]:
    if ingredients_dict[item[0]]["ore_cost"] == 0:
        # Need to break this down
        ore = get_ore_cost(item[0])
    else:
        ore = ingredients_dict[item][1]
    ingredients_dict["FUEL"]["ore_cost"] += ore"""

"""print(
    [
        (k, raw_ingredients_dict[k])
        for k, v in raw_ingredients_dict.items()
        if "ORE" in v
    ]
)"""
