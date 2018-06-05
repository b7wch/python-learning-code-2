# -*- coding:utf-8 -*-
# 2017/6/22
import time
import redis

c = redis.StrictRedis(host="10.8.15.110", port=6379, db=0, socket_keepalive=True)
pipline = c.pipeline()
time1 = time.time()
for each in xrange(10000):
    pipline.set("test_" + str(each), each)
pipline.execute()
time2 = time.time()
print time2-time1
