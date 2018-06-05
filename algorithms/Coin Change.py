#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/11/8
import collections


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        l = [float('inf')] * (amount + 1)
        l[0] = 0
        for e in range(1, amount+1):
            for c in coins:
                if e >= c:
                    l[e] = min(l[e], l[e-c]+1)
        if l[amount] == float('inf'):
            return -1
        return l[amount]
s = Solution()
print s.coinChange([1, 2, 5], 11)
