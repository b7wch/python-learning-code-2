#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/12/25

a = ['a', 'b', ' ', 'c', ' ', ' ', 'd', ' ', 'e', 'f', ' ']
print ''.join(a)


def sstrim(s):
    m, n = 0, 0
    while True and m < len(s)-1 and n < len(s)-1:
        if s[m] != " ":
            m += 1
            continue
        if s[n] == " " and n > m:
            n += 1
            continue
        if s[m] == " " and s[n] != " ":
            s[m], s[n] = s[n], s[m]
            m, n = n, m
    return s


print sstrim(a)
