def count_time_for_gun(ammunition):
    shooting_speed_min = 1200
    time_change_section_sec = 20
    sec_in_min = 60
    ammunition_in_section = 250
    ammunition_in_second = float(sec_in_min) / float(shooting_speed_min)
    result_time = ammunition * ammunition_in_second + \
           (ammunition // ammunition_in_section) * time_change_section_sec
    if ammunition % ammunition_in_section == 0:
        return result_time - time_change_section_sec
    else:
        return result_time


ammunition_count = int(input("Введите количество патронов: "))
if 250 > ammunition_count or ammunition_count > 1000:
    print("Введите число от 250 до 10000.")
else:
    result_sec = count_time_for_gun(ammunition_count)
    print("Патроны закончаться через", result_sec, "сек")
