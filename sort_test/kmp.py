#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/12/20


def KnuthMorrisPratt(text, pattern):
    pattern = list(pattern)
    length = len(pattern)
    shifts = [1] * (length+1)
    shift = 1
    for pos, pat in enumerate(pattern):
        while shift <= pos and pat != pattern[pos-shift]:
            shift += shifts[pos-shift]
        shifts[pos+1] = shift
    startPos = 0
    matchLen = 0
    for c in text:
        while matchLen == length or matchLen >= 0 and pattern[matchLen] != c:
            startPos += shifts[matchLen]
            matchLen -= shifts[matchLen]
        matchLen += 1
        if matchLen == length:
            yield startPos


if __name__ == '__main__':
    for e in KnuthMorrisPratt('abcaabcbaabcaa', 'aabcaa'):
        print e
