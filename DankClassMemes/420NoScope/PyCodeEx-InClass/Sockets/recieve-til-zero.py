import socket

def tcp_echo():
    s = socket.socket()
    #s.connect(('192.168.242.84',12345))
    s.connect(('192.168.242.239',22222))
    s.sendall(b'I am an alpha gamer')
    #s.sendall(b'Whats your favorite scary movie?')
    #s.sendall(b'Bos i swear to gman, if you do not respond to me ill do something')

    recieved = bytearray()
    buf = s.recv(1)
    while buf:
        recieved.extend(buf)
        buf = s.recv(1)

    print(recieved)

def tcp_echo2():
    s = socket.socket()
    s.connect(('192.168.242.84',12345))
    s.sendall(b'hi')

    recieved = bytearray()
    buf = s.recv(1)
    while buf:
        recieved.extend(buf)
        buf = s.recv(1)

    print(recieved)

def tcp_echo3():
    s = socket.socket()
    s.connect(('104.9.242.101',12345))
    s.sendall(b'hi')

    recieved = bytearray()
    buf = s.recv(1)
    while buf:
        recieved.extend(buf)
        buf = s.recv(1)

    print(recieved)

if __name__ == '__main__':
    for x in range(0,420):
        #tcp_echo()
        #tcp_echo2()
        tcp_echo3()
