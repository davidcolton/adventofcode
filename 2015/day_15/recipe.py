from collections import namedtuple
from collections import defaultdict
from math import prod

Ingredient = namedtuple(
    "Ingredient", "name capacity durability flavor texture calories"
)


def sums(length, total_sum):
    # https://bit.ly/2XKUTYp
    if length == 1:
        yield (total_sum,)
    else:
        for value in range(total_sum + 1):
            for permutation in sums(length - 1, total_sum - value):
                yield (value,) + permutation


def process_ingredients_namedtuples(raw_ingredients):
    list_of_ingredients = []
    for ing in raw_ingredients:
        name, measures = ing.split(":")
        list_of_measures = []
        for measure in measures.split(","):
            list_of_measures.append(int(measure.split()[1]))
        list_of_ingredients.append(
            Ingredient(
                name,
                list_of_measures[0],
                list_of_measures[1],
                list_of_measures[2],
                list_of_measures[3],
                list_of_measures[4],
            )
        )
    return list_of_ingredients


def process_ingredients_defaultdict(raw_ingredients):
    list_of_ingredients = defaultdict(dict)
    for ing in raw_ingredients:
        name, measures = ing.split(":")
        list_of_measures = []
        for measure in measures.split(","):
            list_of_measures.append(int(measure.split()[1]))
        list_of_ingredients[name] = {
            "capacity": list_of_measures[0],
            "durability": list_of_measures[1],
            "flavor": list_of_measures[2],
            "texture": list_of_measures[3],
            "calories": list_of_measures[4],
        }
    return list_of_ingredients


def best_recipe(ingredients, total_weight, max_calories=None):
    best_score = 0
    ingredient_names = list(ingredients.keys())
    number_ingredients = len(ingredients)
    for mixture in sums(number_ingredients, total_weight):
        # Only process if all of the values are greater then 0
        if any([val == 0 for val in mixture]):
            next
        capacity = sum(
            [
                ingredients[ing]["capacity"] * mixture[idx]
                for idx, ing in enumerate(ingredient_names)
            ]
        )
        durability = sum(
            [
                ingredients[ing]["durability"] * mixture[idx]
                for idx, ing in enumerate(ingredient_names)
            ]
        )
        flavor = sum(
            [
                ingredients[ing]["flavor"] * mixture[idx]
                for idx, ing in enumerate(ingredient_names)
            ]
        )
        texture = sum(
            [
                ingredients[ing]["texture"] * mixture[idx]
                for idx, ing in enumerate(ingredient_names)
            ]
        )
        calories = sum(
            [
                ingredients[ing]["calories"] * mixture[idx]
                for idx, ing in enumerate(ingredient_names)
            ]
        )

        cookie = [capacity, durability, flavor, texture]
        if all([c > 0 for c in cookie]):
            if max_calories and calories != max_calories:
                continue
            else:
                best_score = max(best_score, prod(cookie))

    return best_score


if __name__ == "__main__":

    with open("./input.txt", "r") as f:
        raw_ingredients = f.read().strip().split("\n")

    ingredients = process_ingredients_defaultdict(raw_ingredients)

    print(f"Best Cookie Score is: {best_recipe(ingredients, 100, 500)}")
