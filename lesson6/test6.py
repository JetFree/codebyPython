months_dict = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май",
               6: "Июнь", 7: "Июль", 8: "Август", 9: "Сентябрь", 10: "Октябрь",
               11: "Ноябрь", 12: "Декабрь"}
if (month_number := int(input("Введите число от 1 до 12: "))) > 12 or\
        month_number <= 0:
    print("Введите число от 1 до 12")
elif month_number == 12 or 0 < month_number <= 2:
    print("Зима,", months_dict.get(month_number))
elif 3 <= month_number <= 5:
    print("Весна,", months_dict.get(month_number))
elif 6 <= month_number <= 8:
    print("Лето,", months_dict.get(month_number))
elif 9 <= month_number <= 11:
    print("Осень,", months_dict.get(month_number))
