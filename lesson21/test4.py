import multiprocessing


class CartridgesBox:

    def __init__(self, amount):
        self.amount = amount

    def get_cartridges(self):
        with lock:
            print(self.amount)
            c_left = 30
            if self.amount >= 30:
                self.amount -= 30
            else:
                self.amount = 0
                c_left = self.amount
            return c_left


def load_cage(number):
    print(f"Курсант {number} начал снаряжать магазин")
    cartridges = general_box.get_cartridges()
    for i in range(1, cartridges + 1):
        print(i, end=" ")
    print(f"\nКурсант {number} снарядил магазин\n")


if __name__ == "__main__":
    lock = multiprocessing.Lock()
    general_box = CartridgesBox(140)
    processes = [multiprocessing.Process(target=load_cage, args=(n,)) for n in range(1, 6)]
    for p in processes:
        p.start()
        p.join()
