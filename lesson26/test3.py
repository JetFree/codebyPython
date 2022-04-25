import requests
import sys
import os
from colorama import Fore
import click
import base64
import urllib.parse

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
        response = requests.get(hostname.replace("FUZZ", ""), headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/72.0.3626.119 Safari/537.36"}, timeout=1)
        response.raise_for_status()
        if response.status_code == 200:
            print('OK!')
    except (requests.exceptions.HTTPError, requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
        print('ERROR: %s' % e)
        sys.exit(0)

    set_url_format(hostname)


def set_url_format(hostname):
    """Функция проверяет форматирование url сайта"""
    global DOMAIN
    if hostname[-1] != "/":
        hostname += "/"
        DOMAIN = hostname
    else:
        DOMAIN = hostname


def print_help():
    with click.get_current_context() as ctx:
        click.echo(ctx.get_help())
    sys.exit(0)


def check_args_qnt(*args):
    """Функция проверяет количество аргументов"""
    if any(x is None for x in args):
        print('\033[94m' + 'To use the program, specify the domain and wordlist https://site.com '
                           '/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt')
        sys.exit(0)


def check_app_keys(U, W):
    """Dir Fuzzer"""
    # Количество аргументов
    check_args_qnt(U, W)
    # Доступность файла словаря
    check_wordlist_file(W)
    # Доступность хоста
    check_site_annotaion(U)
    print(f"\nРаботаем с сайтом {U.replace('FUZZ', '')}. Путь к словарю {W}\n")


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


def parse_heads(head_string):
    head_dict = dict()
    head_string = head_string.strip()
    if head_string.find(',') > -1:
        for head in head_string.split(","):
            name, value = head.strip().split(':')
            head_dict[name.strip()] = value.strip()
    else:
        name, value = head_string.strip().split(':')
        head_dict[name] = value.strip()
    return head_dict


def get_site_dirs(encoding, heads):
    """Функция проверки директорий"""
    counter = 0
    try:
        results = list()
        for target_dir in DIRS:
            if encoding == "base64":
                target_url = DOMAIN.replace("FUZZ", str(base64.b64encode(target_dir.strip().encode("UTF-8")), "utf-8"))
            elif encoding == "urlencode":
                target_url = DOMAIN.replace("FUZZ", urllib.parse.quote(target_dir.strip()))
            else:
                target_url = DOMAIN.replace("FUZZ", target_dir.strip())
            host_answer = requests.get(target_url, headers=parse_heads(heads))
            counter += 1
            res_str = f"{'{:>08d}'.format(counter)} of {len(DIRS)}\t{format_status_code(host_answer.status_code)}\t{target_url}"
            if host_answer.status_code == 404:
                print(f"{res_str: <80}" + "\r", end="")
            else:
                print(f"{res_str: <80}")
                results.append(res_str + "\n")
    except KeyboardInterrupt:
        print(Fore.RED + '  ERROR: manually stop Ctrl+C' + Fore.RESET)
    finally:
        if len(results) > 0:
            write_to_file(results)


@click.command()
@click.option("-u", "U", help="Enter domain https://site.com")
@click.option("-w", "W", help="name and path of the wordlist")
@click.option("-b64", "base", is_flag=True, help="преобразует нагрузку в формат base64")
@click.option("-uenc", "url_enc", is_flag=True, help="преобразует нагрузку в формат urlencode")
@click.option("-head", type=click.STRING, default="",
              help="отправляет вместе с нагрузкой заголовки HTTP, заголовки заключать можно в одинарные"
                   " или двойные кавычки.")
def run_main(U, W, base, url_enc, head):
    """Dir Fuzzer"""
    greetings()
    if U is None and W is None:
        print_help()
    check_app_keys(U, W)
    encoding = None
    if base:
        encoding = "base64"
    elif url_enc:
        encoding = "urlencode"
    get_site_dirs(encoding, head)


if __name__ == "__main__":
    run_main()
