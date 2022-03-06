from queue import PriorityQueue

if __name__ == "__main__":
    q = PriorityQueue()
    q.put((4, "Оплатить счета ЖКУ"))
    q.put((5, "Полежать в ванной"))
    q.put((5, "Полежать в ванной"))
    q.put((1, "Сходить в магазин"))
    q.put((7, "Посмотреть кино"))
    q.put((3, "Отремонтировать дверную ручку"))
    q.put((2, "Выбросить хлам с антресолей"))
    q.put((6, "Составить список дел на завтра"))

    while not q.empty():
        priority, action = q.get()
        print(priority)
        print(action)