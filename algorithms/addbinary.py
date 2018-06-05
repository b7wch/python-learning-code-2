#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/3/27

def addBinary(a, b):
    index = 0
    max_l = min(len(a), len(b)) + 1
    result = [0 for _ in range(max_l)]
    a = a[::-1]
    b = b[::-1]
    print a, '---', b
    print result
    while index < min(len(a), len(b)):
        x = a[index:index + 1]
        y = b[index:index + 1]
        r = (0 if x == "0" else 1) + (0 if y == "0" else 1) + result[index]
        c = r // 2
        if c == 1:
            result[index + 1] = 1
        result[index] = c % 2
        index += 1
    print result
    if result[-1] == 0:
        result.pop(-1)
    if len(a) > len(b):
        left = a[index:]
    else:
        left = b[index:]
    print result
    for each in left:
        if not each:
            continue
        result.append(0 if each == "0" else 1)
    reversed(result)
    return "".join(map(str, result))


if __name__ == '__main__':
    print addBinary("11", '10')
