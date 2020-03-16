import socket

def tcp_echo():
    s = socket.socket()
    s.connect(('192.168.242.84',12345))
    s.sendall(b'Good Morning')
    echodata = s.recv(4096)
    print(echodata)

def udp_echo():
    s = socket.socket(type = socket.SOCK_DGRAM)
    s.sendto(b'hello world', ('192.168.242.84',12345))
    echodata,address = s.recvfrom(4096)
    print(echodata)

if __name__ == '__main__':
    tcp_echo()
