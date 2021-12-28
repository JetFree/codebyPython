class AmmunitionInfo:
    """Class helps to calculate time that left for shooting"""

    def __init__(self):
        self.ammunition_count = int(input("Введите количество патронов: "))
        if 250 > self.ammunition_count or self.ammunition_count > 1000:
            print("Введите число от 250 до 10000.")
        else:
            self.print_result(self.count_time_for_gun())

    def count_time_for_gun(self):
        shooting_speed_min=1200
        ammunition_in_section = 250
        time_change_section_sec = 20
        ammunition_in_second = float(60) / float(shooting_speed_min)
        result_time = self.ammunition_count * ammunition_in_second + (
                self.ammunition_count // ammunition_in_section) * \
                      time_change_section_sec
        if self.ammunition_count % ammunition_in_section == 0:
            return result_time - time_change_section_sec
        else:
            return result_time

    def print_result(self, result):
        print(f"Патроны закончаться через {result} сек")


if __name__ == "__main__":
    AmmunitionInfo()
