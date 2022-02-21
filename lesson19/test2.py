import re

text = '''Примеры расширений файлов:
wald.jpeg
wow.mp4
book.txt
forest.png
fox.tiff 
wood.pdf
hub.gif
small.zip
sound.mp3'''


if __name__ == "__main__":
    matches_list = re.findall(r"(\w+\.(jpeg|png|tiff|gif))", text, re.MULTILINE)
    for t in matches_list:
        print(t[0])
