def decrypt(mes, l):
    result = ""
    for i in range(len(mes)):
        char = mes[i]
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + l - 65) % 26 + 65)
            else:
                result += chr((ord(char) + l - 97) % 26 + 97)
        else:
            result += char
    return result


if __name__ == '__main__':
    message = "=Lryqna Ljnbja="
    for index in range(26):
        print(f"Key +{index}: {decrypt(message, index)}")
