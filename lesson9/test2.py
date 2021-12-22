import time


def measure_time_for_text():
    start_time = time.time()
    print("Время пошло!", end="\n\n")
    string = input()
    finish_time = time.time()
    return string, round(finish_time - start_time, 3)


def calc_typing_speed(text, passed_time):
    return int((len(text) / passed_time) * 60)


def print_time_results(text, time_result):
    print("Прошло", time_result, "сек")
    print("Ваша скорость набора", calc_typing_speed(text, time_result), "знаков в минуту")


if __name__ == '__main__':
    target_string, target_time = measure_time_for_text()
    print_time_results(target_string, target_time)
