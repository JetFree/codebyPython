def encrypt(mes):
    result = ""
    l = 19968
    for i in range(len(mes)):
        char = mes[i]
        if char.isalpha() or char.isspace():
            if ord(char) >= 19968:
                result += chr(ord(char) - l)
            else:
                result += chr(ord(char) + l)
        else:
            result += char
    return result


if __name__ == '__main__':
    msg = input("Enter a message: ")
    print(f"Encrypted/decrypted message: {encrypt(msg)}")
