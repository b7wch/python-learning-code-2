__author__ = 'jasonyang'
import socket
import threading
import time


def tcplink(sock, addr):
    print "accept new connection for %s" % str(addr)
    sock.send("hello")
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data:
            break
        print data
    sock.close()
    print "over!"


if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 8887))
    server.listen(6)
    while True:
        sock, addr = server.accept()
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()
