# -*- coding:utf-8 -*-
# 2017/6/29


class A(object):
    def __init__(self):
        print "A init invoked"


class B(object):
    def __init__(self):
        print "B init invoked"

    def initialize(self):
        print "initialize", self


class D(object):
    def __init__(self):
        print "D init invoked"


class C(D, B, A):
    def __init__(self):
        print "C init invoked", C.mro()
        super(D, self).initialize()


c = C()
