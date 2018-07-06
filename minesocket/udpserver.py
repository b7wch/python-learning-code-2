__author__ = 'yangbaoshan'
import socket

if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(('0.0.0.0', 8889))
    while True:
        data, addr = server.recvfrom(1024)
        print "receive %s from %s" % (data, addr)
        server.sendto('server got it', addr)
