#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/12/20

def qsort(L):
    if len(L) <= 1:
        return L
    return qsort([x for x in L[1:] if x < L[0]]) + L[0:1] + qsort([x for x in L[1:] if x >= L[0]])


if __name__ == '__main__':
    print(qsort([1, 2, 0, 5, 3, 7, 9, 9, 9, 6, 4]))
