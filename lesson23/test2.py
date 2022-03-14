import requests
from colorama import Fore

urls = [
    "https://codeby.net/forums/",
    "https://geekprank.com/hacker/typer/",
    "https://bowandtie.ru/muzhskie-shlyapyi",
    "https://xakep.ru/",
    "https://sdelaicomp.ru/wi-fi/oshibka"
]


def format_response(status):
    result = ""
    if status == 404:
        result = Fore.RED + str(status) + Fore.RESET + " Not Found!"
    elif status == 301:
        result = Fore.LIGHTBLUE_EX + str(status) + Fore.RESET + " Success!"
    else:
        result = Fore.GREEN + str(status) + Fore.RESET + " Success!"
    return result


if __name__ == "__main__":
    for url in urls:
        resp = requests.get(url, allow_redirects=False)
        print(f"{url} {format_response(resp.status_code)}")
