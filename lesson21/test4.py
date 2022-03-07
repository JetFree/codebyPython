import multiprocessing


class CartridgesBox:

    def __init__(self, amount):
        self.amount = amount

    def get_cartridge(self):
        self.amount -= 1


def load_cage(number):
    with lock:
        print(f"Курсант {number} начал снаряжать магазин")
        for i in range(1, 31):
            general_box.get_cartridge()
            print(i, end=" ")
        print(f"\nКурсант {number} снарядил магазин\n")


if __name__ == "__main__":
    lock = multiprocessing.Lock()
    general_box = CartridgesBox(150)
    processes = [multiprocessing.Process(target=load_cage, args=(n,)) for n in range(1, 6)]
    for p in processes:
        p.start()
        p.join()
