def decorate(func):

    def print_decorated(*args):
        text = args[0]
        length = len(text)
        s = "+-" * length + "+\n|"
        for sym in text:
            s += sym + "|"
        s += "\n" + "+-" * length + "+"
        func(s)
        return func

    return print_decorated

@decorate
class Text:

    def __init__(self, text):
        print(text)


Text(input("Введите текст: "))
