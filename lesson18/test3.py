import re


def read_data():
    with open("job.txt", "r") as file:
        return file.read().split("\n")


def print_filtered_jobs(lines_list):
    for line in lines_list:
        if (res := re.search("(^[КЛМНПРС].{5}[к]$)", line)) is not None:
            print(res.group())


if __name__ == "__main__":
    lines_list = read_data()
    print_filtered_jobs(lines_list)
