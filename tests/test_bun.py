import pytest
from praktikum_data.bun import Bun
import data


class TestBun:

    @pytest.mark.parametrize("bun_name, bun_price", data.bun_test_data)
    def test_bun_get_name(self, bun_name, bun_price):
        bun = Bun(bun_name, bun_price)
        result_name = bun.get_name()
        assert result_name == bun_name

    @pytest.mark.parametrize("bun_name, bun_price", data.bun_test_data)
    def test_bun_get_price(self, bun_name, bun_price):
        bun = Bun(bun_name, bun_price)
        result_price = bun.get_price()
        assert result_price == bun_price
