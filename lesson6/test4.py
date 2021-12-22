string = input("Введите строку: ")
if (length := len(string)) > 100:
    print("Количество символов не должно быть больше 100!")
elif length % 10 == 1 and length != 11:
    print("В строке", length, "символ")
elif length % 10 in [2, 3, 4] and length not in [12, 13, 14]:
    print("В строке", length, "символа")
else:
    print("В строке", length, "символов")
