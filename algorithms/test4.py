# -*- coding:utf-8 -*- 
# 2017/4/17

import gevent
import random


def task(pid):
    """
    Some non-deterministic task
    """
    gevent.sleep(random.randint(0, 2) * 1)
    print('Task %s done' % pid)


def synchronous():
    for i in range(1, 10):
        task(i)


def asynchronous():
    threads = [gevent.spawn(task, i) for i in xrange(10)]
    gevent.joinall(threads)


print('Synchronous:')
import time

t1 = time.time()
synchronous()
t2 = time.time()

print('Asynchronous:')
asynchronous()
t3 = time.time()

print t2 - t1, t3 - t2
