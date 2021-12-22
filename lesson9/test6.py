import random
import time


def print_greetings():
    print("-" * 10, "Старт!", "-" * 10)


def print_row(value):
    for i in range(value):
        print("*", end="")
        time.sleep(0.5)
    print()


def print_rows(*args):
    print(args)
    rows_dict = dict(args[0])
    i = 1
    for row in rows_dict.values():
        print(str(i) + ")")
        print_row(row)
        i += 1


def print_winner(rows_dict):
    winner = sorted(rows_dict.items(), key=lambda item: item[1], reverse=True)[
        0]
    print("Дорожка", winner[0], "из", winner[1], "сим. победила!")


data_dict = {name: random.randint(10, 30) for name in "one two three".split()}
print_greetings()
print_rows(data_dict)
print_winner(data_dict)
