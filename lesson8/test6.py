def print_string_info(string):
    print("В предложении", len(string), "символов(л, а)")
    word_list = str(string).split()
    print("В предложении", len(word_list), "слов(а)")
    print("Сколько встречается каждый знак:")
    for s in sorted(set(string)):
        print(s, "-", string.count(s))


if __name__ == '__main__':
    print_string_info(input("Введите предложение: "))

