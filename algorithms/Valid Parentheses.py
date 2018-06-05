#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/11/8

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        if l%2 != 0:
            return False
        d = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        queue=list()
        for i in xrange(l):
            p = s[i]
            if p in d.values():
                queue.append(p)
            else:
                if len(queue)==0:
                    return False
                t = queue.pop()
                if d.get(p)!=t:
                    return False
        if len(queue)==0:
            return True
        else:
            return False

s = Solution()
print s.isValid('(([])){[()]}')