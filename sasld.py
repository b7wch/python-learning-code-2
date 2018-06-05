#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/3/19
import os
import socket

unix_file = "/var/spool/postfix/var/run/saslauthd/mux"
try:
    os.remove(unix_file)
except Exception, e:
    print(e)
oldmask = os.umask(000)
sk = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sk.bind(unix_file)
sk.listen(1)
os.umask(oldmask)
while True:
    buf = bytearray(128)
    conn, addr = sk.accept()
    result = conn.recv_into(buf, 128)
    print "---" * 9
    print result, buf
    for each in buf:
        print "%x" % each
    # print data, len(data), type(data)
    print "---" * 9
    # print " ".join([bin(ord(c)).replace('0b', '') for c in data])
