import pytest
from src.item import Item, InstantiateCSVError


def test_instantiatecsverror():
    assert str(InstantiateCSVError()) == 'Файл items.csv поврежден'
    '''проверяем что новый класс ошибки InstantiateCSVError возвращает ожидаемое строковое сообщение'''

def test_instantiate_from_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()
        raise FileNotFoundError("Отсутствует файл items.csv")
    '''ожидается, что метод `instantiate_from_csv()` выбросит исключение `FileNotFoundError`,
     если файл `items.csv` не существует'''

def test_instantiate_from_csv_broken_file():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()
        raise InstantiateCSVError
    '''Ожидается, что метод `instantiate_from_csv()` выбросит исключение `InstantiateCSVError`,
    если файл `items.csv` поврежден'''



