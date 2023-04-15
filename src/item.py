import csv
from os import path

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []


    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.__name = name #приватный атрибут имени
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"


    def __str__(self):
        return f"{self.__name}"
    @classmethod
    def instantiate_from_csv(cls):
        '''класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv'''
        cls.all.clear()
        with open(path.join('..','src','items.csv'), 'r', encoding='CP1251', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], row['price'], row['quantity'])

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
        price = self.price * self.pay_rate
        return price

#Item.instantiate_from_csv()
#print(len(Item.all))