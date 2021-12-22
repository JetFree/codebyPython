def read_file():
    with open("symbol.txt", "r") as file:
        return file.read().replace("\n", '')


def print_symbols(string):
    n = 8
    text = [string[i:i+n] for i in range(0, len(string), n)]
    for part in text:
        print("{0:.<24}".format(f"{part:,>16}"))


if __name__ == "__main__":
    print_symbols(read_file())
