# -*- coding:utf-8 -*- 
# 2017/4/13


class A(object):
    def __new__(cls, *args, **kwargs):
        print 'A __new__ func'
        return super(A, cls).__new__(cls, *args, **kwargs)


class B(A):
    def __init__(self):
        print('B __init__ func')
        pass


if __name__ == '__main__':
    B()
