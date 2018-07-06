__author__ = 'jasonyang'
import sys
import os
import ConfigParser
import logging


def check_user(username,password):
    cf = ConfigParser.ConfigParser()
    cf.read('user.ini')
    print str(cf.sections())
    try:
        i = cf.get(username, 'password')
        if i.__eq__(password):
            del cf
            return True
    except Exception, e:
        del cf
        return False
    del cf
    return False


if __name__ == '__main__':
    p = os.path.dirname(__file__)
    filename = p + '/user.ini'
    print filename
    f = ConfigParser.ConfigParser()
    f.read(filename)
    print f.sections()
