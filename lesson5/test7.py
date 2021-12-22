target_dict = {'d': 3, 'o': 9, 'j': 8, 'c': 2, 'x': 6, 'g': 1, 'm': 4, 'z': 0,
               'k': 5, 'q': 7}
print("Сумма значений словаря: ", sum(target_dict.values()))
print("Отсортированный список значений словаря: ",
      sorted(list(target_dict.values()), reverse=True))
print("Сумма третьих значений словаря: ", sum(list(target_dict.values())[::3]))
