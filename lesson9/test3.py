rus_str = " йцукенгшщзхъфывапролджэёячсмитьбю"
eng_str = " qwertyuiop[]asdfghjkl;'\\zxcvbnm,."


def switch_lang_for_str():
    text = input("Введите текст: \n")
    rus_result = ""
    for s in text:
        index = eng_str.index(s)
        print(rus_str[index], end='')
    return rus_result


print(switch_lang_for_str())
