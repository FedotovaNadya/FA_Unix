import socket

# Создаём IPv4 сокет потокового типа (TCP/IPv4)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Связываем сокет с адресом localhost и портом 65042
sock.bind(("localhost", 65042))
# Начинаем слушать
sock.listen(True)
# По мере поступления
while True:
    # При присоединении клиента создаём две переменные для управления соединения с клиентом и адрес этого клиента
    conn, addr = sock.accept()
    # Выводим адрес этого клиента
    print('Connected by', addr)
    # Читаем переданных клиентом данные, но не более 1024 байт
    data = conn.recv(1024)
    with open("/etc/passwd", "r") as f:
        data=f.read()
    conn.sendall(data.encode())