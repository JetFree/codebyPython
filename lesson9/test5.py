from pyfiglet import Figlet

f = Figlet()
f.setFont(font="digital")
print(f.renderText("Pentester"))


def get_str_digital_style(text):
    length = len(text)
    s = "+-" * length + "+\n|"
    for sym in text:
        s += sym + "|"
    s += "\n" + "+-" * length + "+"
    return s


if __name__ == "__main__":
    print(get_str_digital_style(input("Введите текст: ")))
