from tests.mocks import MockData
from praktikum.burger import Burger


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





