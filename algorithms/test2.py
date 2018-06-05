# -*- coding:utf-8 -*- 
# 2017/4/12

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = list()
        for each in range(numRows):
            result.append(list())
        flag = 0
        j = 0
        while s:
            if not flag:
                tmp = s[:numRows]
                s = s[numRows:]
                flag = 1
            else:
                tmp = ["" for i in range(numRows)]
                if numRows % 2 == 1:
                    tmp[(numRows - 1) / 2] = s[:1]
                else:
                    tmp[numRows / 2 - 1] = s[:1]
                s = s[1:]
                flag = 0
            for each in tmp:
                result[j].append(each)
            j += 1
            if j > numRows-1:
                j = 0
        res = list()
        for e in range(len(result[0])):
            for each in range(numRows):
                if e >= len(result[each]):
                    break
                res.append(result[each][e])
        return ''.join(res)


print Solution().convert("ABCDE", 2)
