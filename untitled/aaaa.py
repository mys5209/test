#! /usr/bin/python
# -*-coding:utf-8 -*-
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#不需要建立连接
host=('192.168.1.10',45)
msg='你吃饭了'
s.sendto(msg.encode('utf-8'),host)
reg=s.recv(1024)
print(reg.decode('utf-8'))
s.close()

