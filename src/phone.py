from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim
        if number_of_sim <= 0:
            raise ValueError("Number of SIM cards must be greater than zero.")


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):  # получает количество сим-карт для этой модели телефона
        return self.new_number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number_of_sim):  # устанавливает новое количество симок, если это число целое, положительное, не равное нулю
        if type(new_number_of_sim) == int and new_number_of_sim >= 1:
            self.new_number_of_sim = new_number_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')




# phone1 = Phone("iPhone 14", 120_000, 5, 2)
# print(phone1.number_of_sim)
# phone1.number_of_sim = 7.5
# print(phone1.number_of_sim)