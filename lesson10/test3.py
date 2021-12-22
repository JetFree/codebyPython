import time


def get_data():
    try:
        number = int(input("Введите число: "))
    except ValueError:
        print("Необходимо ввести число!")
    except (KeyboardInterrupt, EOFError):
        print("Выполнение программы было остановлено внешним фактором")
    else:
        if number < 10 or number > 30:
            print("Ошибка! Введите число от 10 до 30")
        else:
            return number


def print_time(num):
    if num:
        for i in sorted(range(0, num + 1), reverse=True):
            if i < 10:
                print(" ", end='')
            print(i, end='')
            time.sleep(1.0)
            print("\r", end="")


if __name__ == "__main__":
    try:
        print_time(get_data())
    except KeyboardInterrupt:
        print("Выполнение программы было остановлено внешним фактором")
