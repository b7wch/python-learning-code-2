__author__ = 'yangbaoshan'

import os
from package_test import sayhi


class Temp:
    def __init__(self):
        print("create!")

    def __del__(self):
        print('delete!')


if __name__ == '__main__':
    sayhi.sayhi()
    print "package_test"
    print '/////////////////////////'
    print __file__
    print(os.path.dirname(__file__))
    print (os.path.dirname(os.path.dirname(__file__)))
    print '#################'
    print(os.path.abspath(__file__))
    path = os.path.abspath(__file__)
    for i in range(5):
        print(str(i) + ">>>>>>>" + path)
        path = os.path.dirname(path)
    tem = Temp()
    del tem
