import argparse


class Converter:
    access = {
        0: "---",
        1: "--x",
        2: '-w-',
        3: '-wx',
        4: 'r--',
        5: 'r-x',
        6: 'rw-',
        7: 'rwx'
    }

    def convert(self, string=""):
        return "".join([self.access[int(value)] for value in args.access])

    def __init__(self):
        print("Калькулятор прав доступа:")
        print(f"{args.access} this {self.convert()}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("access", type=str, help="code of access rights")
    args = parser.parse_args()
    Converter()
