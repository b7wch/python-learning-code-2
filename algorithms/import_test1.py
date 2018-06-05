#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/11/2
a = [x for x in range(10)]


class temp(object):
    def __init__(self):
        self.x = 1


def append(t):
    t.append(1)

def set(t):
    t.x = 2
print a
append(a)
print a
b = temp()
print b.x
set(b)
print b.x
