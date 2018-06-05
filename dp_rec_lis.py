#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/11/9
from functools import wraps


def meme(f):
    _cache = {}

    @wraps(f)
    def ff(*args):
        if args not in _cache:
            _cache[args] = f(*args)
        return _cache[args]

    return ff


def rec_lis(seq):
    @meme
    def L(cur):
        res = 1
        for pre in range(cur):
            if seq[pre] <= seq[cur]:
                res = max(res, 1 + L(pre))
        return res

    return max(L(i) for i in range(len(seq)))


def basic_lis(seq):
    L = [1] * len(seq)
    for cur, val in enumerate(seq):
        for pre in range(cur):
            if seq[pre] < val:
                L[cur] = max(L[cur], 1 + L[pre])
    print L
    return max(L)


from bisect import bisect


def lis(seq):
    end = []
    for val in seq:
        idx = bisect(end, val)
        print end, val, idx
        if idx == len(end):
            end.append(val)
        else:
            end[idx] = val
    print end
    return len(end)


print lis([3, 1, 0, 2, 4,5])
