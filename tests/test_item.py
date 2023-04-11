"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)
def test_calc_total_price(item):
    assert item.calculate_total_price() == 200000

def test_apply_disc(item):
    Item.pay_rate = 0.8
    assert item.apply_discount() == 8000.0

