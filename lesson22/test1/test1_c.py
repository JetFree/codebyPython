import socket


s = socket.socket()
try:
    s.connect(("127.0.0.1", 4444))
    print("Соединение установлено!")
    s.send("Мудрым пользуйся девизом - будь готов к любым сюрпризам".encode())
except Exception as e:
    print("Ошибка: ", e)
finally:
    s.close()