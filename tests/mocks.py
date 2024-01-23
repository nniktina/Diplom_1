from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class MockData:

    @staticmethod
    def mock_bun():
        mock_bun = Mock()
        mock_bun.configure_mock(name="black bun", price=1500)
        mocked = Bun(mock_bun.name, mock_bun.price)
        return mocked

    @staticmethod
    def mock_ingredient():
        mock_ingredient = Mock()
        mock_ingredient.configure_mock(ingredient_type='SAUCE', name='Spicy cоус', price=100)
        mocked = Ingredient(mock_ingredient.ingredient_type, mock_ingredient.name, mock_ingredient.price)
        return mocked
