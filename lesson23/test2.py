import requests
from colorama import Fore


def format_response(status):
    if status == 404:
        return f"{Fore.RED}{status}{Fore.RESET} Not Found!"
    elif status == 301:
        return f"{Fore.LIGHTBLUE_EX}{status}{Fore.RESET} Success!"
    else:
        return f"{Fore.GREEN}{status}{Fore.RESET} Success!"


if __name__ == "__main__":
    urls = [
        "https://codeby.net/forums/",
        "https://geekprank.com/hacker/typer/",
        "https://bowandtie.ru/muzhskie-shlyapyi",
        "https://xakep.ru/",
        "https://sdelaicomp.ru/wi-fi/oshibka"
    ]
    for url in urls:
        resp = requests.get(url, allow_redirects=False)
        print(f"{url} {format_response(resp.status_code)}")
