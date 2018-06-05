#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/11/27
import os
import time
import multiprocessing


def f(name):
    time.sleep(1)
    return name + 1


def fil(t):
    if t % 2:
        return True
    else:
        return False


def add(a, b):
    return a + b
def addL(a):
    a.append(0)

if __name__ == '__main__':
    # p = multiprocessing.Pool(5)
    # a = [1, 2, 3, 4, 5]
    # b = p.map(f, a)
    # print a, b
    # print len(filter(fil, [i for i in range(100)]))
    a = [i for i in range(10)]
    addL(a)
    print a