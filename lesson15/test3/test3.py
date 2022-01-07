import click


@click.command()
@click.argument('value')
class LinesFinder:

    def __init__(self, value):
        self.value = value
        self.base_file = "phonebook_al.txt"
        content = self.get_file_content()
        result = self.find_lines(content)
        self.print_result(result)

    def get_file_content(self):
        with open(self.base_file, "r") as file:
            return file.readlines()

    def find_lines(self, lines):
        result_list = list()
        for line in lines:
            if self.value.lower() in line.lower():
                result_list.append(self.refactor_string(line))
        return result_list

    def refactor_string(self, string):
        return " ".join([line_part for line_part in string.split()
                         if "@" not in line_part]).title()

    def print_result(self, lines):
        print(f"Найдено {len(lines)} записей.")
        [print(line) for line in lines]


if __name__ == "__main__":
    LinesFinder()
