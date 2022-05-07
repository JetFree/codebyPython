from multiprocessing import Process
import socket
import sys
from colorama import Fore


def scan_port(hostname, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((hostname, port))
        print(hostname, Fore.GREEN + f"Port: {port} is opened" + Fore.RESET)
    except socket.error:
        print(hostname, Fore.RED + f"Port: {port} is closed" + Fore.RESET)
        pass
    except socket.timeout:
        s.close()
        sys.exit(0)
    except KeyboardInterrupt:
        s.close()
        sys.exit(0)
    finally:
        s.close()


def run_scan(hostname):
    final_port = 65535
    t = 20
    port = 0
    while port <= final_port:
        t_list = []
        for port in range(port, port + t+1):
            mult = Process(target=scan_port, args=(hostname, port))
            mult.start()
            t_list.append(mult)
        try:
            t_list[-1].join()
        except KeyboardInterrupt:
            print("\nProgram process was interrupted by user. Exit.")
            sys.exit(0)
        port += 1


if __name__ == "__main__":
    url = input("Enter URL that need to be scanned: ")
    if url:
        ip = socket.gethostbyname(url)
        if ip is not None:
            run_scan(url)
        else:
            print("There is no such resource or resource is unavailable")
    else:
        print("Empty value was passed in program")
        sys.exit(0)