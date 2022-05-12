import string
import zipfile
import itertools
from colorama import Fore
from tqdm import tqdm


def start_bruteforce(zipfile, amount):
    psw_part = "o_main_got"
    iter = itertools.product(string.digits, repeat=digit_length)
    for digt_part in tqdm(iter, total=amount):
        password = psw_part + "".join(digt_part)
        try:
            zipfile.extractall(pwd=password.strip().encode())
        except:
            pass
        else:
            print("\nPassword found: " + Fore.GREEN + password + Fore.RESET)
            exit(0)


if __name__ == "__main__":
    digit_length = 5
    file_name = "secure.zip"
    zip_file = zipfile.ZipFile(file_name)
    comb_amount = len(string.digits) ** digit_length
    print("Start bruteforce...")
    print(f"Total passwords to test: {comb_amount}")
    start_bruteforce(zip_file, comb_amount)
