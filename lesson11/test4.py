def write_to_file(file_name, content):
    with open(file_name, "w") as file:
        file.write(content)


def print_content_file(file_name):
    with open(file_name, "r") as file:
        print(file.read())


if __name__ == "__main__":
    s = b'\xd0\x9f\xd1\x80\xd0\xb0\xd0\xb2\xd0\xb8\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xbe' \
    b'\xd0\xb9 \xd0\xb4\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb3\xd0\xbe\xd0\xb9 \xd0' \
    b'\xb8\xd0\xb4\xd1\x91\xd1\x82\xd0\xb5 \xd1\x82\xd0\xbe\xd0\xb2\xd0\xb0\xd1' \
    b'\x80\xd0\xb8\xd1\x89\xd0\xb8!\n'
    file_name = "decode.txt"
    write_to_file(file_name, s.decode())
    print_content_file(file_name)
