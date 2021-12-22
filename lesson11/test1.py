def write_number_in_file():
    with open("numbers.txt", "w") as file:
        file.writelines(str(i) + "\n" for i in range(1, 10001))


if __name__ == "__main__":
    write_number_in_file()
