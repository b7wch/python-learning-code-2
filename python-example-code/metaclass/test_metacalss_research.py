# -*- coding:utf-8 -*-
# 2017/6/29


class Meta(type):
    def __new__(mcs, *args, **kwargs):
        print "Meta new"
        return type.__new__(mcs, "meta_class", (), {})  # 1
        # return type('meta_class', (), {})  # 2

    def __init__(self, *args, **kwargs):
        print "meta class init"

    def __call__(cls, *args, **kwargs):
        return super(Meta, cls).__call__()
        # raise RuntimeError("initialize not allowed")


def base_class_with_meta(cls, *base):
    class metaclass(Meta):
        def __new__(mcs, *args, **kwargs):
            return Meta(mcs, base, kwargs)

    return type.__new__(metaclass, "temp_meta_class", base, {})


class A(base_class_with_meta(Meta)):
    def __new__(cls, *args, **kwargs):
        return super(A, cls).__new__(args, kwargs)

    def __init__(self, *args, **kwargs):
        super(A, self).__init__(args, kwargs)


a = A()
b = A()
