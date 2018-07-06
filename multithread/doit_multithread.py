__author__ = 'jasonyang'
from multiprocessing.dummy import Pool
import time

urls = [
    'http://www.python.org',
    'http://www.python.org/about/',
    'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
    'http://www.python.org/doc/',
    'http://www.python.org/download/',
    'http://www.python.org/getit/',
    'http://www.python.org/community/',
    'https://wiki.python.org/moin/',
    'http://planet.python.org/',
    'https://wiki.python.org/moin/LocalUserGroups',
    'http://www.python.org/psf/',
    'http://docs.python.org/devguide/',
    'http://www.python.org/community/awards/'
    # etc..
]


def printu(temp):
    print temp


if __name__ == '__main__':
    timestart = time.time()
    pool = Pool(2)
    pool.map(printu, urls)
    pool.close()
    pool.join()
    print "spend time", time.time()-timestart