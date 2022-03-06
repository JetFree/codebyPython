from queue import LifoQueue
import time

if __name__ == "__main__":
    lq = LifoQueue()
    print("Собираем стопку монет...")
    for i in range(1, 11):
        lq.put(i)
        print(i, end=" ")
        time.sleep(1)
    print("\nРазбираем стопку монет...")
    while not lq.empty():
        i = lq.get()
        print(i, end=" ")
        time.sleep(1)