"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item



@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)
@pytest.fixture
def item_csv():
    return Item.instantiate_from_csv()



def test_calc_total_price(item):
    assert item.calculate_total_price() == 200000


def test_apply_disc(item):
    Item.pay_rate = 0.8
    assert item.apply_discount() == 8000.0


def test_instantiate_from_csv(item_csv):
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('123') == 123
    assert Item.string_to_number('-2754') == -2754

def test_name(item):
    assert item.name == "Смартфон"


def test_name_setter(item):
    item.name = 'gena'
    assert item.name == 'gena'
    with pytest.raises(ValueError):
        item.name = 'hghjghjggdgfdgfsfdsgj'




