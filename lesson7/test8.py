str = input("Введите строку: ")
print(' '.join([word[::-1] for word in str.split(" ")]))

