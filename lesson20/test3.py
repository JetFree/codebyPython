import threading
from colorama import Fore
import time


def start_race(car_name, race_time):
    start_time = time.time()
    print(f"Автомобиль {car_name} стартовал!")
    time.sleep(race_time)
    print(f"\nКоличество активных авто: {threading.active_count() - 1}")
    print(f"Автомобиль {Fore.GREEN + car_name + Fore.RESET} финишировал {find_place()}")
    print(Fore.LIGHTMAGENTA_EX + f"Доехал до финиша за: {time.time() - start_time:.3f} сек." + Fore.RESET)


def find_place():
    with lock:
        number = 3
        if threading.active_count() == 4:
            number = 1
        elif threading.active_count() == 3:
            number = 2
    return number


if __name__ == "__main__":
    lock = threading.Lock()
    cars = [threading.Thread(target=start_race, args=["MAZDA", 15]),
            threading.Thread(target=start_race, args=["HONDA", 18]),
            threading.Thread(target=start_race, args=["TOYOTA", 19])
            ]
    for t in cars:
        t.start()
