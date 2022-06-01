from . import ip_address
import requests
from sys import exit


def run_ip_reversed_lookup():
    print("9. Reverse IP lookup")
    ip = ip_address.get_address()
    res = requests.get(f"https://api.hackertarget.com/reverseiplookup/?q={ip}")
    if res.status_code == 200:
        print(res.text)
        return res.text
    else:
        print("Error during executing response")
        exit(0)




