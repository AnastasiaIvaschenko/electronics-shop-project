import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120000, 5, 2)


def test_self_repr(phone):
    assert phone.__repr__() == "Phone('iPhone 14', 120000, 5, 2)"


def test_pos_num_sim(phone):
    phone.number_of_sim = 2
    assert phone.new_number_of_sim == 2



def test_zero_num_sim(phone):
    with pytest.raises(ValueError):
        phone.new_number_of_sim = 0
        raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')


def test_float_num_sim(phone):
    with pytest.raises(ValueError):
        phone.new_number_of_sim = 2.5
        raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')


def test_neg_num_sim(phone):
    with pytest.raises(ValueError):
        phone.new_number_of_sim = -2
        raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')
