from colorama import Fore


class Trapezoid:
    """Class Trapezoid contains data about Trapezoid and methods to calculate square"""

    def __init__(self, d1, d2, h):
        if h > d1 or h > d2:
            print(
                f"{Fore.RESET}{Fore.RED}Введите корректные параметры трапеции."
                f"{Fore.RESET}")
        else:
            self.print_square(self.count_square(d1, d2, h))

    def print_square(self, s):
        print(f"{Fore.RESET}Площадь трапеции: {s:.2f} кв.м")

    def count_square(self, d1, d2, h):
        return ((d2 ** 2 - h ** 2) ** 0.5 +
                (d1 ** 2 - h ** 2) ** 0.5) / 2 * h


if __name__ == "__main__":
    d1 = float(input(f"Введите диагональ трапеции 1: {Fore.GREEN}"))
    d2 = float(
        input(f"{Fore.RESET}Введите диагональ трапеции 2: {Fore.GREEN}"))
    h = float(
        input(f"{Fore.RESET}Введите высоту трапеции: {Fore.GREEN}"))
    Trapezoid(d1, d2, h)
