#import
import socket
import time
import logging
#Запуск сервера

def log_print(st):
    logging.info(st)
    print(st)

logging.basicConfig(filename='server.log', encoding='utf-8', level=logging.INFO)

log_print('Starting server...')
PORT = 2000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', PORT))

try:
    while True:
        server.listen(1)
        #подключение клента
        client_socket, address = server.accept()
        log_print(f'User with ip {address} connected')
        
        client_socket.send('You are connected!'.encode('utf-8'))
        while True:
            try:
                data = client_socket.recv(2048).decode('utf-8')
            except OSError:
                data = None

            time.sleep(3)
            if data:
                #получение данных от клиента
                log_print('\nReceiving data from client:')
                log_print(data)
                if data.lower() == 'exit':
                    log_print('here')
                    break
            msg = input('\nEnter text to client:\n').encode('utf-8')
            #отправка сообщений клиенту
            client_socket.send(msg)
            if msg == 'exit'.encode('utf-8'):
                time.sleep(2)
                #отключение клиента
                log_print('exit command found')
                server.shutdown(socket.SHUT_WR)
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                server.bind(('127.0.0.1', 2000))
                break
#остановка сервера                
except KeyboardInterrupt:
    log_print('Server is shutting down')
    server.shutdown(socket.SHUT_WR)
except BrokenPipeError:
    log_print('Server doesnt have active users...\nShutting down!')
    server.shutdown(socket.SHUT_WR)