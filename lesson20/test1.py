import threading
import os


def show_image(image_name):
    os.system(f"feh {image_name}")


if __name__ == "__main__":
    print("Привет Бро! Я занял первое место в конкурсе!")
    t = threading.Timer(5, show_image, ["nb.png"])
    t.start()
