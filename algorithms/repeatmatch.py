#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/12/27
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        lenA = len(A)
        lenB = len(B)
        n = lenB//lenA
        for i in range(3):
            if B in A*(n+i):
                return n+i
        return -1
print(Solution().repeatedStringMatch("abababaaba", "aabaaba"))