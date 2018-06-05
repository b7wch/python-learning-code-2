#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/1/2

def testfunc():
    for each in [1, 2]:
        try:
            a = 1
            if a in [1, 2]:
                print 'hello'
            return 'exit'
        except Exception, e:
            print e

testfunc()