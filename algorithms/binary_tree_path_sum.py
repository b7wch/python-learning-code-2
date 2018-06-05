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
    path.append(root.val)
    if not root.left and not root.right:
        result.append(path[:])
        path.pop()
        return
    if root.left:
        walk(root.left, path, result)
    if root.right:
        walk(root.right, path, result)
    path.pop()


root = TreeNode(5)
node4 = TreeNode(4)
node8 = TreeNode(8)
root.left = node4
root.right = node8
node11 = TreeNode(11)
node7 = TreeNode(7)
node2 = TreeNode(2)
node13 = TreeNode(13)
node8_4 = TreeNode(4)
node1 = TreeNode(1)
node4.left = node11
node11.left = node7
node11.right = node2
node8.left = node13
node8.right = node8_4
node8_4.right = node1


root = TreeNode(1)
print Solution.binaryTreePaths(root)
print 22 in [sum(each) for each in Solution.binaryTreePaths(root)]
