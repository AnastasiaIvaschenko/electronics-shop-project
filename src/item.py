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

    @classmethod
    def instantiate_from_csv(cls):
        pass

    @staticmethod
    def string_to_number():
        pass
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
