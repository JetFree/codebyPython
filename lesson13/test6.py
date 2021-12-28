import random


class Competition:

    def __init__(self):
        self.player_dict = {name: random.sample([0, 5, 6, 7, 8, 9, 10], 3)
                            for name in ["Артур", "Семён", "Даниил"]}
        self.print_results()
        self.print_final_results()

    def print_results(self):
        for name, result in self.player_dict.items():
            print(f"Стреляет {name}:")
            for index, value in enumerate(result):
                index += 1
                if value < 5:
                    print(f"Попытка {index}: {0:>02d} оч. Мазила!")
                elif value in range(5, 8):
                    print(f"Попытка {index}: {value:>02d} оч. Так себе")
                elif value in range(8, 10):
                    print(f"Попытка {index}: {value:>02d} оч. Неплохо")
                else:
                    print(f"Попытка {index}: {value:>02d} оч. Меткий выстрел")

    def print_final_results(self):
        sorted_dict = sorted(self.player_dict.items(), key=lambda x: sum(x[1]),
                             reverse=True)
        print(sorted_dict)
        print("\n", "-" * 50, "\n")
        for index, value in enumerate(sorted_dict):
            index += 1
            print(f"{index} место в стрельбе из лука: {value[0]} -"
                  f" {sum(value[1])} оч.")


Competition()
