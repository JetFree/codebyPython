def read_all_line_from_file(file):
    return file.read().splitlines()


def filter_cities(cities_list):
    return [city for city in cities_list if str(city).find("о") == -1]


def write_to_file(file, lines):
    for line in lines:
        file.write(line + "\n")


if __name__ == "__main__":
    with open("city.txt", "r") as file, open("city_2.txt", "w") as file1:
        content_lines = read_all_line_from_file(file)
        write_to_file(file1, filter_cities(content_lines))
