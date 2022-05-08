from multiprocessing import Pool
import socket
import sys

import netaddr.core
from colorama import Fore
from netaddr import *


def scan_port(hostname):
    for port in port_list:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((str(hostname), port))
            print(hostname, Fore.GREEN + f"Port: {port} is opened" + Fore.RESET)
        except socket.error:
            # print(hostname, Fore.RED + f"Port: {port} is closed" + Fore.RESET)
            pass
        except socket.timeout:
            sys.exit(0)
        except KeyboardInterrupt:
            sys.exit(0)
        finally:
            s.close()


def run_scan_multithread(ip_range):
    with Pool(10) as p:
        p.map(scan_port, ip_range)


if __name__ == "__main__":
    port_list = [43, 80, 109, 110, 115, 118, 119, 143, 194, 220, 443, 540, 585, 591, 1112, 1433, 1443, 3128, 3197, 3306,
                 3899, 4224, 4444, 5000, 5432, 6379, 8000, 8080, 10000]
    try:
        ipStart, ipEnd = input("Enter IP-IP: ").split("-")
        iprange = IPRange(ipStart, ipEnd)
        run_scan_multithread(iprange)
    except ValueError:
        print("Incorrect format of entered data.")
    except netaddr.core.AddrFormatError:
        print("Failed to detect a valid IP or format of IP is incorrect")