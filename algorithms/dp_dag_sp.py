#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/11/9
from functools import wraps

w = {
    'a': {'b': 2, 'f': 9},
    'b': {'c': 1, 'd': 2, 'f': 6},
    'c': {'d': 7},
    'd': {'e': 2, 'f': 3},
    'e': {'f': 4},
    'f': {},
}


def memo(f):
    _cache = {}

    @wraps(f)
    def ff(*args):
        if _cache.get(args):
            return _cache.get(args)
        else:
            _cache[args] = f(*args)
            return _cache[args]

    return ff


def rec_dag_sp(W, s, t):
    @memo
    def d(u):
        if u == t: return 0
        return min(W[u][v] + d(v) for v in W[u])

    return d(s)


print rec_dag_sp(w, 'a', 'f')
