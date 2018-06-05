# -*- coding:utf-8 -*-
# 2017/7/11


def sel_sort_rec(seq):
    max_value = 0
    max_index = 0
    if len(seq) == 1:
        return seq
    for i, each in enumerate(seq):
        if each > max_value:
            max_value = each
            max_index = i
    pop_value = seq[-1]
    seq[max_index] = pop_value
    seq[-1] = max_value
    return sel_sort_rec(seq[:-1]) + [seq[-1], ]


def ins_sort(seq, i):
    if i == 0:
        return
    ins_sort(seq, i - 1)
    j = i
    while j > 0 and seq[j - 1] > seq[j]:
        seq[j - 1], seq[j] = seq[j], seq[j - 1]
        j -= 1


if __name__ == '__main__':
    test = [1, 2, 5, 7, 4, 6, 9, 0, 8]
    print ins_sort(test, len(test)-1)
    print test