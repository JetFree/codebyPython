class String_helper:
    """Прорамма считает количество символов без учёта пробелов"""

    def __init__(self):
        self.input_text = input("Введите предложение: ")

    def count_symbols(self):

        text = self.input_text.replace(' ', "")
        print("В предложении", len(text), "символов")
        print(self.count_symbols.__doc__)


if __name__ == "__main__":
    String_helper().count_symbols()
