import socket
sock = socket.socket()
try:
  sock.bind(('', 80))
except OSError:
  print("5555")
  sock.bind(('', 8080))
except:
  print("5555-except")
  sock.bind(('', 5555)) 

sock.listen(1000)
conn, addr = sock.accept()
print("Connected", addr)
data = conn.recv(8192)
msg = data.decode()
print(msg) 

resp = """HTTP/1.1 200 OK 

Hello, webworld!"""
conn.send(resp.encode())

conn.close()
print("here")
