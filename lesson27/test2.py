import itertools
import re
import string


def print_help():
    help_str = "Keyword generator\n\nB - большие буквы\nL - маленькие буквы\nS - спецсимволы\nN - числа\n\n"
    print(help_str)


def get_str_length():
    try:
        length_str = int(input("Количество символов в слове: \n"))
        if length_str <= 0:
            raise ValueError()
        return length_str
    except ValueError:
        print("Ошибка! Введите целое число больше нуля!")
        return get_str_length()


def build_dict_with_args():
    dict_v = {'b': string.ascii_uppercase, 'l': string.ascii_lowercase, 's': string.punctuation, 'n': string.digits}
    final_dict = list()
    for letter in set(input("Выберите аргументы: \n")):
        if letter in dict_v.keys():
            final_dict.append(dict_v[letter])
    return "".join(final_dict)


def calculate_combinations(sym_dict, length):
    return len(sym_dict) ** length


def generate_comb_list(symbol_dict, length):
    return itertools.product(symbol_dict, repeat=length)


def write_to_file(perm_iter):
    with open("gen_dict.txt", "w") as file:
        for permutation in perm_iter:
            file.write("".join(permutation) + "\n")


if __name__ == "__main__":
    print_help()
    symbols = build_dict_with_args()
    str_length = get_str_length()
    comb_count = calculate_combinations(symbols, str_length)
    print(f"Количество комбинаций: {comb_count}")
    write_to_file(generate_comb_list(symbols, str_length))
    print("Done!")
