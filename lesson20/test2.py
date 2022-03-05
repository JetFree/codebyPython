import threading


def add_one():
    global x
    with lock:
        for _ in range(500000):
            x += 1


def minus_one():
    global x
    with lock:
        for _ in range(300000):
            x -= 1


if __name__ == "__main__":
    global x
    lock = threading.Lock()
    t1_list = [threading.Thread(target=add_one) for _ in range(10)]
    t2_list = [threading.Thread(target=minus_one) for _ in range(10)]
    print("Start of the process...")
    for index in range(10):
        x = 500000
        t1_list[index].start()
        t2_list[index].start()
        t1_list[index].join()
        t2_list[index].join()
        print(f"Iteration {index + 1}: x = {x}")
    print("Done!")
