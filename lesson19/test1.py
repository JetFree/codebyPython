import re

text = 'Сначала был адрес http://yandex.ru, потом стал https://yandex.ru. \
Гугл https://google.com имеет шире охват чем https://yandex.ru.'

if __name__ == "__main__":
    res = set(re.findall(r'\w{4,5}:\/\/\w+\.\w+', text))
    for val in res:
        print(val)

