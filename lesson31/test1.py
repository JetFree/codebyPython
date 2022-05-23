import sys


def print_help():
    print("1 - encode text\n2 - decode text")


def get_data():
    try:
        choice = int(input("Select action: "))
        text = input("Enter a message: ").upper()
    except ValueError:
        print("Incorrect value entered. Please select correct value")
        sys.exit(0)
    if choice == 1:
        return text, True
    elif choice == 2:
        return text, False
    else:
        print("Incorrect value entered. Please select correct value")


def encode_text(text, is_encode):
    final = str()
    alpha = reversed_upper
    revers_alpha = c_alphabet_upper
    if is_encode:
        alpha = c_alphabet_upper
        revers_alpha = reversed_upper
    for symbol in text:
        for index_alpha, symbol_alpha in enumerate(alpha):
            if symbol == symbol_alpha:
                final += revers_alpha[index_alpha]
    print("Encrypted message: " + final)


if __name__ == '__main__':
    c_alphabet_upper = [chr(x) for x in range(1040, 1072)]
    reversed_upper = list(c_alphabet_upper)
    reversed_upper.reverse()
    print_help()
    text, choice = get_data()
    encode_text(text, choice)
