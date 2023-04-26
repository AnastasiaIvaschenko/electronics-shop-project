"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone



@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def item_csv():
    return Item.instantiate_from_csv()


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


class Phone1:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

phone1 = Phone1("iPhone 14", 120000, 5)
@pytest.fixture
def phone1():
    return Phone1("iPhone 14", 120000, 5)


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



def test_self_repr(item):
    assert item.__repr__() == "Item('Смартфон', 10000, 20)"


def test_self_str(item):
    assert item.__str__() == 'Смартфон'


def test_add_quantity(item, phone):
    assert item.__add__(phone) == 25
    assert phone + item == 25


# class Phone1:
#     def __init__(self, name: str, price: float, quantity: int) -> None:
#         self.name = name
#         self.price = price
#         self.quantity = quantity

def test_add_quantity1(item, phone1):
    with pytest.raises(AssertionError):
        item + phone1
        raise AssertionError('Объект должен принадлежать к классу Item или Phone')




