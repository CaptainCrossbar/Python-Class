import socket

def tcp_qotd():
    s = socket.socket()
    s.connect(('djxmmx.net',17))
    received = bytearray()
    buf = s.recv(64)
    while buf:
        received.extend(buf)
        buf = s.recv(64)
    print(received)

if __name__ = '__main__':
    tcp_qotd()
