import sys


def print_help():
    print("1 - encode text\n2 - decode text")


def encode_text(text):
    final = str()
    for symbol in text:
        for index_alpha, symbol_alpha in enumerate(c_alphabet_upper):
            if symbol == symbol_alpha:
                final += reversed_upper[index_alpha]
    print("Encrypted message: " + final)


def decode_text(text):
    final = str()
    for symbol in text:
        for index_alpha_rev, symbol_alpha_rev in enumerate(reversed_upper):
            if symbol == symbol_alpha_rev:
                final += c_alphabet_upper[index_alpha_rev]
    print("Decrypted message: " + final)


if __name__ == '__main__':
    c_alphabet_upper = [chr(x) for x in range(1040, 1072)]
    reversed_upper = list(c_alphabet_upper)
    reversed_upper.reverse()
    print_help()
    try:
        choice = int(input("Select action: "))
        text = input("Enter a message: ").upper()
    except ValueError:
        print("Incorrect value entered. Please select correct value")
        sys.exit(0)
    if choice == 1:
        encode_text(text)
    elif choice == 2:
        decode_text(text)
    else:
        print("Incorrect value entered. Please select correct value")
