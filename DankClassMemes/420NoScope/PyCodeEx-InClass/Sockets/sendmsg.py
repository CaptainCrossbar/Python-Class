import socket

s = socket.socket()
s.connect((address,port))
s.sendall(b'pete')
msg = bytearray()
data = s.recv(1)
while data:
    msg.extend(data)
    data = s.recv(1)
return msg 
