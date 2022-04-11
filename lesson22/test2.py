import socket
import re
from ftplib import FTP


def format_hosts(hosts_list):
    return [re.search("[a-z]+\.[a-z]{2,}\.*[a-z]*", host).group() for host in hosts_list]


def get_host_addr(hosts_list):
    socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip_list = list()
    for host in hosts_list:
        ip_list.append(socket.gethostbyname(host) + "\n")
    return ip_list


def upload_file_ftp(username, password, file_name):
    ftp = FTP("localhost")
    ftp.login(username, password)
    ftp.cwd("files")
    with open(file_name, "r+b") as fp:
        ftp.storbinary(f"STOR {file_name}", fp)
    ftp.quit()


if __name__ == "__main__":
    hosts = ["https://www.hackthebox.eu/",
             "https://hack.me/",
             "http://www.gameofhacks.com/",
             "http://www.itsecgames.com/"
             ]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip_list = get_host_addr(format_hosts(hosts))
    with open("hosts_ip", "w") as file:
        file.writelines(ip_list)
    upload_file_ftp("ftpuser", "kali", "hosts_ip")

