import socket
from colorama import Fore

udp_port = 2323
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
broadcast_addr = ("", udp_port)
s.bind(broadcast_addr)
print("Жду подключения...")
saved_addr = ()
while True:
    try:
        msg, addr = s.recvfrom(1024)
        if msg.decode() == "exit":
            break
        elif msg:
            if addr != saved_addr:
                print(f"Соединение установлено: {addr}")
                saved_addr = addr
            print(Fore.RESET + f"UDP клиент: {msg.decode()}")
            s.sendto(input("Сервер UDP: " + Fore.GREEN).encode(), addr)
    except KeyboardInterrupt as e:
        print(Fore.RESET + "\nПрограмма прервана пользователем")
        break
s.close()
print(Fore.RESET + "\nСоединение закрыто.")
