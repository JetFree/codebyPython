import urllib.parse
import base64


def get_file_content():
    with open("task.txt", "rb") as file:
        return file.read().decode('unicode-escape')


def url_decode(bin_v):
    return urllib.parse.unquote(bin_v)


def base64_decode(string):
    return base64.b64decode(string)


if __name__ == "__main__":
    content = get_file_content()
    url_decoded = url_decode(content.encode())
    b64_decoded = base64_decode(url_decoded)
    print(b64_decoded.decode('utf-8'))

