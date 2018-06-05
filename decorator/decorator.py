#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/12/20

def wraper(func):
    def _wraper():
        print('in wraper')
        func()
        print('in wraper')

    return _wraper


def wraper1(level):
    print(level)

    def _wraper(func):
        def _wraper1(*args, **kwargs):
            print(1)
            print(level * 3)
            func(*args, **kwargs)
            print(2)

        return _wraper1

    return _wraper


@wraper
def f():
    print('123')


class Decorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print('123')
        return self.func

@Decorator
def ff():
    print('123')


@wraper1('hello')
def g(name):
    print('hello {0}'.format(name))


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


if __name__ == '__main__':
    # f()
    # g('abc')
    # f1, f2, f3 = count()
    # print(f1())
    # print(f2())
    # print(f3())
    ff()
