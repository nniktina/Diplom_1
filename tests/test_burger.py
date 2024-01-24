from praktikum.ingredient import Ingredient
from tests.mocks import MockData
from praktikum.burger import Burger
from praktikum.database import Database


class TestBurger:

    def test_burger_set_buns(self):
        burger = Burger()
        mocked_bun = MockData.mock_bun()
        burger.set_buns(mocked_bun)
        assert burger.bun == mocked_bun

    def test_burger_add_ingredient(self):
        burger = Burger()
        mocked_ingredient = MockData.mock_ingredient()
        burger.add_ingredient(mocked_ingredient)
        assert mocked_ingredient in burger.ingredients

    def test_burger_remove_ingredient(self):
        burger = Burger()
        mocked_ingredient = MockData.mock_ingredient()
        burger.add_ingredient(mocked_ingredient)
        burger.remove_ingredient(0)
        assert mocked_ingredient not in burger.ingredients

    def test_burger_move_ingredient(self):
        burger = Burger()
        database = Database()
        burger.add_ingredient(database.ingredients[0])
        burger.add_ingredient(database.ingredients[3])
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1].name == database.ingredients[0].name
