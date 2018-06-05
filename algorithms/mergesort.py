# -*- coding:utf-8 -*-
# 2017/7/10


def mergesort(seq):
    mid = len(seq) // 2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1:
        lft = mergesort(lft)
    if len(rgt) > 1:
        rgt = mergesort(rgt)
    print("lft", ":", lft)
    print("rgt", ":", rgt)
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res


if __name__ == '__main__':
    test = [1, 2, 5, 7, 4, 6, 9, 0, 8]
    print mergesort(test)
