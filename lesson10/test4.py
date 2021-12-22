import random


def get_data():
    try:
        number = int(input("Введите число от 1 до 10: "))
    except ValueError:
        print("Необходимо ввести число!")
    except (KeyboardInterrupt, EOFError):
        print("Выполнение программы было остановлено внешним фактором")
    else:
        if number > 10 or number < 1:
            print("Ошибка! Введите число от 1 до 10")
        return number


def get_help_msg(actual_num, expected_num, try_counter):
    if not actual_num:
        return
    if actual_num == expected_num:
        return "Ты победил!"
    elif try_counter < 3:
        return "Ваше число больше" if actual_num > expected_num \
            else "Ваше число меньше"
    else:
        return "Удача не на твоей стороне, попробуй ещё!"


if __name__ == "__main__":
    exp_v = random.randint(1, 10)
    for i in range(1, 4):
        result = get_help_msg(get_data(), exp_v, i)
        if result:
            print(result)
            if result == "Ты победил!":
                break
        else:
            break
