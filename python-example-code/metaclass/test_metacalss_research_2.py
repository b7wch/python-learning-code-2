# -*- coding:utf-8 -*-
# 2017/6/29


class Meta(object):
    def __new__(cls, *args, **kwargs):
        print "Meta new"
        return super(Meta, cls).__new__(cls, args, kwargs)

    def __call__(self, *args, **kwargs):
        return super(Meta, self).__call__(args, kwargs)
        # raise RuntimeError("initialize not allowed")


def base_class_with_meta(cls, *base):
    class metaclass(Meta):
        def __new__(cls, *args, **kwargs):
            return Meta(cls, base, kwargs)

    return type.__new__(metaclass, "temp_meta_class", base, {})


class A(Meta):
    # def __new__(cls, *args, **kwargs):
    #     return super(A, cls).__new__(args, kwargs)

    def __init__(self, *args, **kwargs):
        super(A, self).__init__(args, kwargs)


a = A()
b = A()
