from abc import ABC

class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    def consumption(self):
        return f'Сумма затраченной ткани равна: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}'


class Coat(Clothes):
    def consumption(self):
        return f'Для пошива пальто нужно: {self.param / 6.5 + 0.5 :} '


class Costume(Clothes):
    def consumption(self):
        return f'Для пошива костюма нужно: {2 * self.param + 0.3 }'



coat = Coat(400)
costume = Costume(55)
print(coat.consumption)
print(costume.consumption())
