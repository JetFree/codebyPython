from colorama import Fore
from colorama import Back


class Color_util:

    def __init__(self):
        self.colors = ["Зелёный", "Красный", "Синий", "Пурпурный"]
        self.colorama_colors = {1: Back.GREEN, 2: Back.RED, 3: Back.BLUE,
                                4: Back.MAGENTA}
        self.print_colors()
        self.select_color()
        self.enter_string()
        self.print_colored_string()

    def print_colors(self):
        for index, value in enumerate(self.colors):
            print(f"{index+1}) {value}")

    def select_color(self):
        self.selected_color = int(input(f"Выберите цвет: {Fore.GREEN}"))

    def enter_string(self):
        self.string = input(f"{Fore.RESET}Введите строку: {Fore.GREEN}")

    def print_colored_string(self):
        print(f"{Fore.RESET}{self.colorama_colors.get(self.selected_color)}"
              f"{self.string}{Back.RESET}")


Color_util()

