import socket
from colorama import Fore

udp_port = 2323
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
srv_addr = ("localhost", udp_port)
s.connect(srv_addr)
while True:
    try:
        msg = input("Клиент UDP: " + Fore.GREEN)
        s.sendto(msg.encode(), ("", udp_port))
        if msg == "exit":
            break
        msg, addr = s.recvfrom(1024)
        print(Fore.RESET + f"Сервер UDP: {msg.decode()}")
    except KeyboardInterrupt as e:
        print(Fore.RESET + "\nПрограмма прервана пользователем")
        break
s.close()
