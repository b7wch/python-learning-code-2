# -*- coding:utf-8 -*- 
# 2017/4/12
import math
class Solution(object):
    def myAtoi(self, str_input):
        """
        :type str: str
        :rtype: int
        """
        try:
            x = int(str2int(str_input))
            if x > 2**31 - 1:
                return 2**31 - 1
            if x < -2**31:
                return -2**31
            return x
        except:
            return 0


def str2int(str_input):
    result = []
    i = 0
    for each in str_input:
        if each in ['-', '+'] and not i:
            result.append(each)
            i += 1
            continue
        if each == " " and not i:
            continue
        try:
            each = int(each)
        except:
            break
        if not each:
            if i != 1:
                result.append(str(each))
                i += 1
                continue
            else:
                continue
        if each in range(10):
            result.append(str(each))
            i += 2
            continue
        if each not in range(10):
            break
    if result == ['-'] or result == ["+"]:
        return 0
    return "".join(result)
print (Solution().myAtoi("       1056706k5060"))