# -*- coding:utf-8 -*-
# 2017/9/27
file_name = 'name_data.csv'
count_total = 0
if __name__ == '__main__':
    result = dict()
    for each in open(file_name, 'r').readlines():
        each = each.strip().replace('"', '')
        if not each:
            continue
        if not result.get(each):
            result[each] = 1
        else:
            result[each] += 1
        count_total += 1
    print count_total
    tpl = '{0},{1},{2}'
    for i, j in result.iteritems():
        print tpl.format(i,j,(j / float(count_total)))