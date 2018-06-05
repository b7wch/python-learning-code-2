#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/12/27

def palindrome(s):
    length = len(s)
    mid = length // 2
    for i in range(mid):
        if s[i] == s[length - 1 - i]:
            continue
        else:
            return False
    else:
        return True

print(palindrome('aabbaa'))


def palindrome2(s, flag=0):
    length = len(s)
    mid = length // 2
    for i in range(mid):
        if s[i] == s[length - 1 - i]:
            continue
        else:
            if flag == 0:
                return palindrome2(s[1:], 1) or palindrome2(s[:-1], 1)
            else:
                return False
    else:
        return True

print(palindrome2('abda'))