# -*- coding:utf-8 -*-
# 2017/8/29
import os
import yaml
import socket

if os.path.exists("./conf/conf.yml"):
    with open("./conf/conf.yml") as f:
        conf = yaml.safe_load(f)
unix_file = conf.get('log_file2')
try:
    os.unlink(unix_file)
except OSError, E:
    print E
    if os.path.exists(unix_file):
        raise IOError, "unix file exists"
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
sock.bind(unix_file)
while True:
    data = sock.recv(4096)
    print data

