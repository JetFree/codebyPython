class Person:
    def __init__(self, cash, name, position):
        self.__cash = cash
        self.name = name
        self.position = position

    def money(self):
        return self.__cash


people = Person("2000", "Вася", "Дворник")
man = Person("15000", "Жора", "Гендиректор")
print(f'{people.position} {people.name} получил зарплату {people.money()} рублей')
print(f'{man.position} {man.name} получил зарплату {man.money()} рублей')
