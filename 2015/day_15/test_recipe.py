import pytest
from recipe import best_recipe
from recipe import process_ingredients_defaultdict


ingredients = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""


@pytest.mark.parametrize("arg, expected", [(ingredients, 62842880)])
def test_best_recipe(arg, expected):
    ing = process_ingredients_defaultdict(ingredients.split("\n"))
    score = best_recipe(ing, 100)
    assert score == expected


@pytest.mark.parametrize("arg, expected", [(ingredients, 57600000)])
def test_best_recipe_calories(arg, expected):
    ing = process_ingredients_defaultdict(ingredients.split("\n"))
    score = best_recipe(ing, 100, 500)
    assert score == expected
