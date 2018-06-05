#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/11/7

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        for tt in range(l):
            for i in range(l - tt):
                if nums[i] == 0 and i + 1 <= l - tt - 1:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]

        return nums


class Solution2(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        for tt in range(l):
            for i in range(l - tt):
                if nums[i] == 0 and i + 1 <= l - tt - 1:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]

        return nums


s = Solution()
print s.moveZeroes([0, 1, 0, 3, 12])
