from queue import PriorityQueue

if __name__ == "__main__":
    d = {4: "Оплатить счета ЖКУ",
         5: "Полежать в ванной",
         1: "Сходить в магазин",
         7: "Посмотреть кино",
         3: "Отремонтировать дверную ручку",
         2: "Выбросить хлам с антресолей",
         6: "Составить список дел на завтра"}
    q = PriorityQueue()
    for priority, action in d.items():
        q.put((priority, action))

    while not q.empty():
        priority, action = q.get()
        print(priority)
        print(action)
