# -*- coding:utf-8 -*- 
# 2017/5/4
import time
import random
import SocketServer
import SimpleHTTPServer


class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        # ips = ["10.14.53.113", "10.14.53.105"]
        # ip = random.choice(ips)
        # print '---'*10, ip
        self.send_response(200)
        self.end_headers()
        return


address = ("", 8008)

httpd = SocketServer.TCPServer(address, Handler)
httpd.serve_forever()
