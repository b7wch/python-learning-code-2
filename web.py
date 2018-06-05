#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/5/30
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop


class HelloHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello world!")


application = Application([
    ('^/', HelloHandler)
], )

if __name__ == '__main__':
    application.listen(port=8881)
    IOLoop.current().start()
