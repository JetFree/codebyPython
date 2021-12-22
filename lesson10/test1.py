import random


def get_data():
    try:
        number = int(input("Введите число: "))
    except ValueError:
        print("Необходимо ввести число!")
    except (KeyboardInterrupt, EOFError):
        print("Выполнение программы было остановлено внешним фактором")
    else:
        if number > 10 or number < 1:
            print("Введите число от 1 до 10")
        else:
            return number


def subseq_sum(a, b):
    sum_result = 0
    if a == b:
        sum_result = a + b
    else:
        for number in range(a, b + 1):
            sum_result += number
    return sum_result


if __name__ == "__main__":
    if num := get_data():
        r_int = random.randint(10, 100)
        print(subseq_sum(num, r_int))
