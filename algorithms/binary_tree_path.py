# -*- coding:utf-8 -*-
# 2017/7/18
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    @staticmethod
    def binary_tree_paths(root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        from collections import deque
        Q = deque()
        S = list()
        Q.append(root)
        while Q:
            u = Q.pop()
            S.append(u.val)
            if u.right:
                Q.append(u.right)
            if u.left:
                Q.append(u.left)
        return S

    @staticmethod
    def binaryTreePaths(root):
        result = list()
        if not root:
            return list()
        if not root.left and not root.right and root.val is None:
            return list()
        walk(root, result=result)
        return result


def walk(root, path=None, result=None):
    if path is None:
        path = list()
    path.append(str(root.val))
    if not root.left and not root.right:
        result.append('->'.join(path))
        path.pop()
        return
    if root.left:
        walk(root.left, path, result)
    if root.right:
        walk(root.right, path, result)
    path.pop()


node4 = TreeNode(4)
node5 = TreeNode(5)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1 = TreeNode(1)
node1.left = node2
node1.right = node3
node2.right = node5
# node2.left = node4
# node6 = TreeNode(6)
# node3.left = node6

print Solution.binaryTreePaths(node1)
result_walk = list()
walk(node1, result=result_walk)
print result_walk
