if set(string_1 := input("Введите первое слово:\n")) ==\
        set(string_2 := input("Введите второе слово:\n")):
    print("Слова", string_1, "и", string_2, "состоят из одних и тех же букв.\n")
else:
    print("Введённые слова содержат разный набор букв.\n")
