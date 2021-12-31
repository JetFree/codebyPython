class Stuff:

    def __init__(self, name, prepayment, summa):
        self.name = name
        self.prepayment = prepayment
        self.summa = summa
        self.print_info()

    def print_info(self):
        print(f"{self.name} - аванс {self.summa} рублей")


class StuffPlus(Stuff):

    def __init__(self, name, prepayment, summa, salary, summa2):
        self.salary = salary
        self.summa2 = summa2
        super().__init__(name, prepayment, summa)

    def print_info(self):
        print(f"{self.name} - аванс {self.summa} рублей, зарплата - {self.summa2} рублей")


stuff_list = (
    ("Сергей Обухов", 3000, 3000),
    ("Иван Абрамов", 2400, 2400),
    ("Кирилл Навальный", 5000, 5000),
    ("Стас Костюшкин", 1000, 8000, 1000, 8000),
    ("Павел Старовойтов", 3000, 10000, 3000, 10000)
)

for stuff in stuff_list:
    if len(stuff) == 3:
        Stuff(*stuff)
    else:
        StuffPlus(*stuff)

