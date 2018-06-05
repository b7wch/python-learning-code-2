#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/12/26

class Solution(object):
    def lengthOfLastWord(self, s):
        length = len(s)
        result = 0
        for x in range(length - 1, -1, -1):
            if s[x] != " ":
                result += 1
            elif s[x] == " " and result == 0:
                continue
            elif s[x] == " " and result != 0:
                break
        return result


print(Solution().lengthOfLastWord('a'))
