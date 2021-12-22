my_dict = {1: ("ладошка", "лошадка"), 2: ("сушилка", "подмена"),
           3: ("вязанка", "навязка"), 4: ("каторга", "рогатка"),
           5: ("плесень", "полдник")}

print(*my_dict[1], set(my_dict[1][0]) == set(my_dict[1][1]))
print(*my_dict[2], set(my_dict[2][0]) == set(my_dict[2][1]))
print(*my_dict[3], set(my_dict[3][0]) == set(my_dict[3][1]))
print(*my_dict[4], set(my_dict[4][0]) == set(my_dict[4][1]))
print(*my_dict[5], set(my_dict[5][0]) == set(my_dict[5][1]))
