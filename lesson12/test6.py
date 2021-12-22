import calendar
from colorama import Fore

year_calendar = calendar.LocaleTextCalendar(locale="ru_RU.UTF-8")

with open("calendar.txt", "w") as file:
    file.write(year_calendar.formatyear(2020, 0, 0, 6, 3))
with open("calendar.txt", "r") as file:
    file_lines = file.readlines()

for line in file_lines:
    if line.find("2020") > 0 or line.find("а") > 0:
        print(Fore.GREEN + line + Fore.RESET, end="")
    elif line.find("сб") > 0:
        print(line.replace("сб вс", f"{Fore.RED}{'сб вс'}{Fore.RESET}"), end="")
    else:
        print(line, end="")

