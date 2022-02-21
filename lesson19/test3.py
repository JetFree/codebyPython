import re


def read_all_names():
    with open("surnames.txt", "r") as file:
        return file.read().split("\n")


def is_women_name(string):
    return re.match("^[А-яа-я-]+(ВА|НА|АЯ)$", string)


def write_to_file(file_name, line):
    with open(file_name, "a") as file:
        file.write(line + "\n")


def format_name(line):
    return line.lower().title()


if __name__ == "__main__":
    name_list = read_all_names()
    for name in name_list:
        if is_women_name(name):
            write_to_file("woman.txt", format_name(name))
        else:
            write_to_file("man.txt", format_name(name))
    print("Done!")
