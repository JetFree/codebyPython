import socket


def name():
    print("1. Host IP\n")


def get_address():
    host = input("Enter the host: ")
    if host:
        if "://" in host:
            host = host.split("://")[1]
        host = host.replace("/", "")
        try:
            remote_ip = socket.gethostbyname(host)
            print(f"IP Address of {host} is {remote_ip}")
            return remote_ip
        except socket.gaierror as e:
            print(e.strerror)
    else:
        print("User have to enter correct host")


def run():
    name()
    get_address()
