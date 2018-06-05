#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/12/22
from collections import defaultdict


def count_sort(A, key=lambda x: x):
    B, C = [], defaultdict(list)
    L = list()
    for each in A: # N
        L.extend(each)
    for x in L: #(M+N)
        C[key(x)].append(x)
    for k in range(min(C), max(C) + 1): #M+N
        B.extend(C[k])
    return B


import random
a = [
    [1, 2, 5, 7, 8, 9, 10],
    [2, 1, 6, 5, 3, 8, 9, 8, 10],
    [int(random.random()*100) for _ in range(int(random.random()*100))]
]
# count_sort(a)[m:(m + n)]
print(count_sort(a))
