import animals
import random


def print_help():
    print("Help: ")
    for key, value in data_dict.items():
        print("   ", str(key) + ')', value[0])


def get_data():
    try:
        number = int(input("Введите номер рисунка: "))
    except ValueError:
        print("Необходимо ввести число!")
    except (KeyboardInterrupt, EOFError):
        print("Выполнение программы было остановлено внешним фактором")
    else:
        if number > 7 or number < 1:
            print("Введите число от 1 до 7")
        else:
            return number


def get_animal_image(num):
    if num == 7:
        return get_animal_image(random.randint(1, 6))
    else:
        return data_dict.get(num)[1]


if __name__ == "__main__":
    data_dict = {1: ("deer", animals.deer), 2: ("cat", animals.cat),
             3: ("cow", animals.cow), 4: ("frog", animals.frog),
             5: ("bat", animals.bat), 6: ("butterfly", animals.butterfly)
             }
    print_help()
    num = get_data()
    print(get_animal_image(num))
