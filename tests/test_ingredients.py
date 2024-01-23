import pytest
from praktikum.ingredient import Ingredient
import data


class TestIngredient:

    @pytest.mark.parametrize("ingredient_type, name, price", data.ingredient_test_data)
    def test_ingredients_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize("ingredient_type, name, price", data.ingredient_test_data)
    def test_ingredients_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type, name, price", data.ingredient_test_data)
    def test_ingredients_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
