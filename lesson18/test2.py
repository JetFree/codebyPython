import re


def read_data():
    with open("proxy.txt", "r") as file:
        return file.readlines()

def print_all_ip_addresses(lines_list):
    for line in lines_list:
        print(re.match("([0-9]{1,3}[.]{0,1}){4}", line).group())


if __name__ == "__main__":
    lines_list = read_data()
    print_all_ip_addresses(lines_list)
