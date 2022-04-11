import requests
import sys
import os
from colorama import Fore

DOMAIN = ""
DIRS = []


def greetings():
    """Функция отображает приветствие пользователя"""
    print(Fore.GREEN + '''
╔═══╗╔══╗╔═══╗     ╔═══╗╔╗─╔╗╔════╗╔════╗╔═══╗╔═══╗
╚╗╔╗║╚╣║╝║╔═╗║     ║╔══╝║║─║║╚══╗═║╚══╗═║║╔══╝║╔═╗║
─║║║║─║║─║╚═╝║     ║╚══╗║║─║║──╔╝╔╝──╔╝╔╝║╚══╗║╚═╝║
─║║║║─║║─║╔╗╔╝     ║╔══╝║║─║║─╔╝╔╝──╔╝╔╝─║╔══╝║╔╗╔╝
╔╝╚╝║╔╣║╗║║║╚╗     ║║───║╚═╝║╔╝═╚═╗╔╝═╚═╗║╚══╗║║║╚╗
╚═══╝╚══╝╚╝╚═╝     ╚╝───╚═══╝╚════╝╚════╝╚═══╝╚╝╚═╝
          ''' + Fore.RESET)


def check_wordlist_file(path_to_wordlist):
    """Функция проверяет наличие файла со словарём"""
    if not os.path.isfile(path_to_wordlist.replace("\'", "")):
        print(f"{path_to_wordlist}\nФайл со словарём не найден.")
        sys.exit(0)
    fill_dirs_from_file(path_to_wordlist)


def check_site_annotaion(hostname):
    """Функция проверяет есть ли коннект с хостом"""
    try:
        response = requests.get(hostname, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"},
                                timeout=1)
        response.raise_for_status()
        if response.status_code == 200:
            print('OK!')
    except (requests.exceptions.HTTPError, requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
        print('ERROR: %s' % e)

    set_url_format(hostname)


def set_url_format(hostname):
    """Функция проверяет форматирование url сайта"""
    global DOMAIN
    if hostname[-1] != "/":
        hostname += "/"
        DOMAIN = hostname
    else:
        DOMAIN = hostname


def check_args_qnt(args_qnt):
    """Функция проверяет количество аргументов"""
    if len(args_qnt) != 3:
        print('\033[94m' + 'To use the program, specify the domain and wordlist https://site.com '
                           '/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt')
        sys.exit(0)


def check_app_keys():
    """Функция проверяет правильность аргументов"""
    # Количество аргументов
    check_args_qnt(sys.argv)
    # Доступность файла словаря
    check_wordlist_file(sys.argv[2])
    # Доступность хоста
    check_site_annotaion(sys.argv[1])
    print(f"\nРаботаем с сайтом {sys.argv[1]}. Путь к словарю {sys.argv[2]}\n")


def fill_dirs_from_file(dirs_file):
    """Функция читает файл с адресами папок в список"""
    with open(dirs_file, "r") as reader:
        for line in reader.readlines():
            DIRS.append(line)
    print("\nЗагружено строк из словаря: " + str(len(DIRS)) + "\n")


def format_status_code(status_code):
    if status_code == 200:
        return f"{Fore.GREEN}{status_code}{Fore.RESET}"
    else:
        return f"{Fore.RED}{status_code}{Fore.RESET}"


def write_to_file(result_list):
    with open("fuzz.txt", "w") as file:
        file.writelines(result_list)


def get_site_dirs():
    """Функция проверки директорий"""
    counter = 0
    try:
        results = list()
        for target_dir in DIRS:
            target_url = DOMAIN + target_dir.strip() + "/"
            host_answer = requests.get(target_url)
            counter += 1
            if host_answer.status_code == 404:
                continue
            else:
                res_str = f"{'{:>08d}'.format(counter)} of {len(DIRS)}\t{format_status_code(host_answer.status_code)}\t{target_url}"
                print(res_str)
                results.append(res_str + "\n")
    except KeyboardInterrupt:
        print(Fore.RED + '  ERROR: manually stop Ctrl+C' + Fore.RESET)
    finally:
        if len(results) > 0:
            write_to_file(results)


if __name__ == "__main__":
    greetings()
    check_app_keys()
    get_site_dirs()
