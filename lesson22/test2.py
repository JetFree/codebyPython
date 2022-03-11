import socket
import re
from ftplib import FTP

hosts = ["https://www.hackthebox.eu/",
         "https://hack.me/",
         "http://www.gameofhacks.com/",
         "http://www.itsecgames.com/"
         ]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_list = list()
hosts = [re.search("[a-z]+\.[a-z]{2,}\.*[a-z]*", host).group() for host in hosts]
for host in hosts:
    ip_list.append(socket.gethostbyname(host) + "\n")
with open("hosts_ip", "w") as file:
    file.writelines(ip_list)

ftp = FTP("localhost")
ftp.login("ftpuser", "kali")
ftp.cwd("files")
with open("hosts_ip", "r+b") as fp:
    ftp.storbinary("STOR hosts_ip", fp)
ftp.quit()

