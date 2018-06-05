# -*- coding:utf-8 -*- 
# 2017/5/9


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, j = 0, 0
        result = [0, 0, 1 if s else 0]
        while i < len(s):
            j = i + 1
            while j < len(s):
                if s[j] not in s[i:j]:
                    if len(s[i:j+1]) > result[2]:
                        result = [i, j, len(s[i:j+1])]
                    j += 1
                else:
                    break
            i += 1
        return result[2]


s = Solution()
print s.lengthOfLongestSubstring("abc")

