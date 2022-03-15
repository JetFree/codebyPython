import requests
from colorama import Fore


def is_vulnerable(url):
    url_s = url.split("=")[0]
    res = requests.get(f"{url_s}=\"")
    if res.content.decode().lower().find("error") == -1:
        return False
    else:
        return True


def format_result(url, is_v):
    if is_v:
        formatted_string = f"{Fore.GREEN}Vulnerable!{Fore.RESET}"
    else:
        formatted_string = f"{Fore.RED}Not Vulnerable!{Fore.RESET}"
    print(url, "===>", formatted_string)


if __name__ == "__main__":
    urls = [
        "http://leettime.net/sqlninja.com/tasks/basic_ch1.php?id=1",
        "https://www.genecards.org/cgi-bin/carddisp.pl?gene=ID1",
        "http://leettime.net/sqlninja.com/tasks/basic_ch2.php?id=1",
        "http://esjindex.org/search.php?id=1"
    ]
    for url in urls:
        format_result(url, is_vulnerable(url))
