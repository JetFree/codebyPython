class String_helper:

    def __init__(self):
        self.input_text = input("Введите предложение: ")

    def count_symbols(self):
        """Прорамма считает количество символов без учёта пробелов"""
        text = self.input_text.replace(' ', "")
        print("В предложении", len(text), "символов")
        print(self.count_symbols.__doc__)


if __name__ == "__main__":
    String_helper().count_symbols()
