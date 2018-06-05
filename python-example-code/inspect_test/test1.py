# -*- coding:utf-8 -*-
# 2017/8/11
import inspect


def f():
    import os
    print 123


print inspect.getsource(f)
exec('%s \n%s()' % (inspect.getsource(f), f.__name__), globals(), locals())
# import os
f()
print os.listdir('./')
