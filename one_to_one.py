#! /usr/bin/python3
'''File Name: one_to_one.py
   Author: Longxin Li
   Purpose: This program will accept two arguments,
            one is the string which called host,
            second one is the integer which called port.
            Program will check the host, if the host equal
            "server", program will create a server with port.
            Otherwise it will create a client which connect to
            the server.
            It allows send message once by time between client
            and server, start with client. If client sends nothing
            to the server, the client will disconnect from server.
            It will also disconnect if the server stop running.
   CS346'''
import sys
from socket import *
from sys import argv


def main(host, port):
    if host == 'server':
        server(port)
    else:
        addr = (host, port)
        client(addr)


def client(addr):
    sock = socket()
    sock.connect(addr)
    msg = input()
    while msg != '':
        sock.sendall(msg.encode())
        data = sock.recv(1024).decode()
        if data == '':
            sock.close()
            sys.exit()
        print(data)
        msg = input()
    sock.close()
    sys.exit()


def server(port):
    sock = socket()
    addr = ("0.0.0.0", port)
    sock.bind(addr)
    sock.listen()
    while True:
        (conn, conn_addr) = sock.accept()
        data = conn.recv(1024).decode()
        while data != "":
            print(data)
            msg = input()
            if msg == '':
                conn.close()
                sys.exit()
            conn.sendall(msg.encode())
            data = conn.recv(1024).decode()


if __name__ == "__main__":
    host = str(argv[1])
    port = int(argv[2])
    main(host, port)
