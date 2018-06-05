#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/12/29

class Node(object):
    left = None
    right = None

    def __init__(self, key, val):
        self.key = key
        self.val = val


def insert(node, key, val):
    if node is None:
        return Node(key, val)
    if node.key == key:
        node.val = val
    if node.key > key:
        node.left = insert(node.left, key, val)
    else:
        node.right = insert(node.right, key, val)
    return node


def search(node, key):
    if node is None:
        raise KeyError
    if node.key == key:
        return node.val
    if node.key > key:
        return search(node.left, key)
    else:
        return search(node.right, key)


class Tree(object):
    root = None

    def __setitem__(self, key, value):
        self.root = insert(self.root, key, value)

    def __getitem__(self, item):
        return search(self.root, item)

    def __contains__(self, item):
        try:
            search(self.root, item)
        except KeyError:
            return False
        return True
