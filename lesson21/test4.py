import multiprocessing


amount = multiprocessing.Value("i", 150)


def get_cartridges():
    global amount
    c_left = 30
    if amount.value >= 30:
        amount.value -= 30
    else:
        c_left = amount.value
        amount.value = 0
    return c_left


def load_cage(number):
    print(f"Курсант {number} начал снаряжать магазин.")
    cartridges = get_cartridges()
    for i in range(1, cartridges + 1):
        print(i, end=" ")
    print(f"\nКурсант {number} снарядил магазин\n")


if __name__ == "__main__":
    lock = multiprocessing.Lock()
    processes = [multiprocessing.Process(target=load_cage, args=(n,)) for n in range(1, 6)]
    for p in processes:
        p.start()
        p.join()
