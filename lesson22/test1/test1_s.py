import socket


s = socket.socket()
print("Жду подключения...")
s.bind(("0.0.0.0", 4444))
s.listen(1)
conn, addr = s.accept()
try:
    print(f"Соединение установлено: {addr}")
    while True:
        client_msg = conn.recv(1024).decode()
        if not client_msg:
            break
        print(f"Клиент: {client_msg}")
except Exception as e:
    print("Ошибка:", e)
finally:
    conn.close()
    print("Соединение закрыто.")

