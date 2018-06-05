# -*- coding:utf-8 -*-
# 2017/8/29print "Connecting..."
import socket
import os

if os.path.exists("/var/spool/postfix/dev/log"):
    client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    client.connect("/var/spool/postfix/dev/log")
    print "Ready."
    print "Ctrl-C to quit."
    print "Sending 'DONE' shuts down the server and quits."
    while True:
        try:
            x = raw_input("> ")
            if "" != x:
                print "SEND:", x
                client.send(x)
                if "DONE" == x:
                    print "Shutting down."
                    break
        except KeyboardInterrupt, k:
            print "Shutting down."
    client.close()
else:
    print "Couldn't Connect!"
print "Done"
