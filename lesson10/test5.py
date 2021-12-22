def get_data():
    try:
        return input("Введите пароль: ")
    except (KeyboardInterrupt, EOFError, UnboundLocalError):
        print("Выполнение программы было остановлено внешним фактором")
        return False


def is_start_as_capital(string):
    return string[0].isupper()


def is_contains_latin(string):
    return True if any([str(i).isalpha() for i in string]) else False


def is_contains_digits(string):
    return True if any([str(i).isdigit() for i in string]) else False


def is_contains_underscore(string):
    return False if string.find("_") == -1 else True


def is_string_end_correct(string):
    return True if string[-1].isalpha() or string[-1].isdigit() else False


def is_string_length_correct(string):
    return True if 8 <= len(string) <= 20 else False


def is_password_meet_conditions(string):
    conditions = [is_start_as_capital(password),
                      is_contains_latin(password), is_contains_digits(password),
                      is_contains_underscore(password),
                      is_string_end_correct(password),
                      is_string_length_correct(password)]
    return True if all(conditions) else False


if __name__ == "__main__":
    password = get_data()
    if password:
        print("Пароль принят!") if is_password_meet_conditions(password) else \
            print("Пароль не соответствует требованиям!")

