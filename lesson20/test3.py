import threading
from colorama import Fore
import time


def start_race(car_name, start_time):
    print(f"\nКоличество активных авто: {threading.active_count() - 1}")
    print(f"Автомобиль {Fore.GREEN + car_name + Fore.RESET} финишировал {find_place()}")
    print(Fore.LIGHTMAGENTA_EX + f"Доехал до финиша за: {time.time() - start_time:.3f} сек." + Fore.RESET)


def find_place():
    number = 3
    if threading.active_count() == 4:
        number = 1
    elif threading.active_count() == 3:
        number = 2
    return number


if __name__ == "__main__":
    race_dict = {"MAZDA": 15, "HONDA": 18, "TOYOTA": 19}
    for car_name, sec in race_dict.items():
        print(f"Автомобиль {car_name} стартовал!")
        threading.Timer(sec, start_race, [car_name, time.time()]).start()
