import socket

def tcp_echo():
    s = socket.socket() #AF_INET and SOCK_STREAM by default
    s.bind(('0.0.0.0',12345))
    s.listen()
    while True:
        conn,address = s.accept()
        print('connection accepted from {}'.format(address))
        conn.sendall(conn.recv(4096))
        conn.close()

def udp_echo():
    s = socket.socket(type = socket.SOCK_DGRAM)
    s.bind(('0.0.0.0',12345))
    while True:
        data,address = s.recvfrom(4096)
        print(data, 'recieved from {}'.format(address))
        s.sendto(data, address)

if __name__ = '__main__':
    udp_echo()
