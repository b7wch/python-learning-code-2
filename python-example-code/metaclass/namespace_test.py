# -*- coding:utf-8 -*-
# 2017/6/30


class A(object):

    @staticmethod
    def print_self(name):
        print A.__name__, name

A.print_self('123')
