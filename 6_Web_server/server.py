import socket
import logging
import os


wd = "6_Web_server\\6_wd\\"

def log_print(st):
    logging.info(st)
    print(st)

def genResp(dat):
  d=dat.split()
  print( d)
  fn =d[1]
  if len(fn)>1:
    fn=fn[1:]
    print ("if")
  else:
    return "index.html"
  if fn in os.listdir(wd):
    print("qwer")
    return fn
  else:
    print("jasdj")
    return "404.html"

  




sock = socket.socket()
try:
  sock.bind(('', 80))
except OSError:
  sock.bind(('', 8080))


sock.listen(1000)
conn, addr = sock.accept()
log_print("Connected"+str(addr))

while True:
  try:
    data = conn.recv(8192).decode('utf-8')
  except OSError:
    data = None

  if data:
      #получение данных от клиента
      log_print('\nReceiving data from client:')
      log_print(data)
      if data.lower() == 'exit':
          log_print('here')
          break
      #отправка сообщений клиенту
      print("----")
      file=genResp(data)
      with open(wd+file, "r") as f:
        resp = "HTTP/1.1 200 OK \n\n"+f.read()
      print("he134re")
      
      conn.send(resp.encode())

conn.close()
print("here")
