def count_symbols(text):
    """Прорамма считает количество символов без учёта пробелов"""
    text = text.replace(' ', "")
    print("В предложении", len(text), "символов")
    print(count_symbols.__doc__)


input_text = input("Введите предложение: ")
count_symbols(input_text)
