__author__ = 'yangbaoshan'
import socket

l = ['a', 'b', 'c', 'd']
if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for x in l:
        client.sendto(x, ('127.0.0.1', 8889))
        print client.recv(1024)
    client.close()
