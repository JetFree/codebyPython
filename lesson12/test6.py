import calendar
from colorama import Fore

year_calendar = calendar.LocaleTextCalendar(locale="ru_RU.UTF-8")

with open("calendar.txt", "w") as file:
    file.write(year_calendar.formatyear(2020, 0, 0, 6, 3))
with open("calendar.txt", "r") as file:
    for line in file.readlines():
        if "2020" in line or "а" in line:
            print(f"{Fore.GREEN}{line}{Fore.RESET}", end="")
        elif "сб" in line:
            print(line.replace("сб вс", f"{Fore.RED}{'сб вс'}{Fore.RESET}"), end="")
        else:
            print(line, end="")

