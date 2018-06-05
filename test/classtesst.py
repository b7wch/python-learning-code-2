#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/11/6

class A(object):
    def __init__(self, a=1, b=2):
        self.a = a
        self.b = b


class B(A):
    def __init__(self, a, b, c):
        self.c = c
        A.__init__(self, a, b)

    def __str__(self):
        return str(self.__dict__)


b = B(1, 2, 3)
print b
