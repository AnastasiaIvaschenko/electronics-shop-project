import csv
from os import path


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []


    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__()
        self.__name = name #приватный атрибут имени
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"


    def __str__(self):
        return f"{self.__name}"
    @classmethod
    def instantiate_from_csv(cls):
        '''класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv'''
        cls.all.clear()
        '''если файл `items.csv`, из которого по-умолчанию считываются данные, не найден → 
        выбрасывается исключение `FileNotFoundError` с сообщением “_Отсутствует файл items.csv_"'''
        try:
            with open(path.join('..', 'src', 'items.csv'), 'r', encoding='CP1251', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    '''если файл `item.csv` поврежден (например, отсутствует одна из колонок данных) → 
                    выбрасывается исключение `InstantiateCSVError` с сообщением “_Файл item.csv поврежден_”'''
                    try:
                        cls(row['name'], row['price'], row['quantity'])
                    except:
                        raise InstantiateCSVError
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл items.csv")

    @staticmethod
    def string_to_number(data):
        '''статический метод, возвращающий число из числа-строки'''
        data = float(data)
        return int(data)


    @property
    def name(self): #возвращает имя
        return self.__name

    @name.setter
    def name(self, name): #Вводит новое значение имени, если не более 10 символов
        if len(name) <= 10:
            self.__name = name
        else:
            raise ValueError

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return self.price


    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise AssertionError('Объект должен принадлежать к классу Item или Phone')


class InstantiateCSVError(ValueError, KeyError):
    def __init__(self):
        self.message = 'Файл items.csv поврежден'
    def __str__(self):
        return self.message

