import click


@click.command()
@click.argument('value')
class LinesFinder:

    def __init__(self, value):
        self.value = value
        self.base_file = "phonebook_al.txt"
        content = self.get_file_content()
        content = self.find_lines(content)
        self.print_result(content)

    def get_file_content(self):
        with open(self.base_file, "r") as file:
            return file.readlines()

    def find_lines(self, lines):
        result_list = list()
        for line in lines:
            if self.value.upper() in line or self.value.lower() in line:
                result_list.append(self.refactor_string(line))
        return result_list

    def refactor_string(self, string):
        line_list = string.split()
        if line_list[0].isupper():
            line_list[0] = line_list[0].capitalize()
        new_str = " ".join([line_part for line_part in line_list
                            if "@" not in line_part])
        return new_str

    def print_result(self, lines):
        print(f"Найдено {len(lines)} записей.")
        [print(line) for line in lines]


if __name__ == "__main__":
    LinesFinder()
