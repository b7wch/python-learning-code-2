# -*- coding:utf-8 -*- 
# 2017/5/23


def f():
    n = yield 1
    print n
    return
a = f()
a.send(None)