import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard1():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_change_lang(keyboard1):
    keyboard1.change_lang()
    assert keyboard1.language == 'RU'
    keyboard1.change_lang()
    assert keyboard1.language == 'EN'


def test_set_language(keyboard1):
    with pytest.raises(AttributeError):
        keyboard1.language = 'CH'
        raise AttributeError




