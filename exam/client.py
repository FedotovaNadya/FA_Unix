import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Присоединяемся к серверу
sock.connect(("localhost", 65042))
sock.sendall(b"Hello, world")
# Читаем данные от сервера, но не более 1024 байт
data = sock.recv(1024)
# Закрываем соединение
sock.close()
# Выводим полученные данные
print(data.decode("utf-8"))