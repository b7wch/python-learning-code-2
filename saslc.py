#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/3/20
import socket
client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
client.connect("/var/spool/postfix/var/run/saslauthd/mux")
client.send("hello")
client.close()