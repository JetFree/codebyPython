from multiprocessing import Pool
import time


def print_time(x):
    time.sleep(1)
    print("\r" + str(x), end="")


if __name__ == "__main__":
    print("Cтарт!", end="")
    with Pool(1) as p:
        p.map(print_time, range(10, 0, -1))
    print("\rВремя вышло!")