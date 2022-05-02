import itertools

import string

SYMBOL_AMOUNT = 62


def get_str_length():
    try:
        length_str = int(input("Количество символов в слове: "))
        if length_str <= 0:
            raise Exception()
        return length_str
    except Exception:
        print("Ошибка! Введите целое число больше нуля!")
        get_str_length()


def calculate_combinations(length):
    return SYMBOL_AMOUNT ** length


def generate_comb_list(length):
    symbol_list = string.digits + string.ascii_lowercase + string.ascii_uppercase
    return list(itertools.permutations(symbol_list, length))


def write_to_file(perm_list):
    with open("my_dict.txt", "w") as file:
        file.writelines(["".join(perm) + "\n" for perm in perm_list])


if __name__ == "__main__":
    str_length = get_str_length()
    comb_count = calculate_combinations(str_length)
    print(f"Количество комбинаций: {comb_count}")
    write_to_file(generate_comb_list(str_length))
    print("Done!")
