import re


def get_data():
    try:
        return input("Введите пароль: ")
    except (KeyboardInterrupt, EOFError, UnboundLocalError):
        print("Выполнение программы было остановлено внешним фактором")
        return False


if __name__ == "__main__":
    password = get_data()
    if password:
        res = re.match(r"^[A-Z](?=.*[A-Za-z])(?=.*[\d])(?=.*_).{6,18}[A-Za-z\d]$", password)
        if res is not None:
            print("Пароль принят!")
        else:
            print("Пароль не соответствует требованиям!")