def print_all_words(*args):
    print(list(args))


word_list = []
while bool(word := input("Введите любое слово: ")):
    word_list.append(word)

print_all_words(*word_list)
