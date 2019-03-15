#!/usr/bin/python

import socket

HOST = '104.248.158.18'

PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.blind((HOST,PORT))
s.listen(1)

conn, addr = s.accept()

print 'Connected by', addr

while 1:
    data = conn.recv(1024)
    if not data: break
    conn.send(data)

conn.close()

