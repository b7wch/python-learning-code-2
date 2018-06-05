# -*- coding:utf-8 -*-
# 2017/7/17

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    @staticmethod
    def average_of_levels(root):
        """
        :param root: Tree Node
        :return: List[float]
        """
        S, Q = list(), list()
        Q.append((0, root))
        while Q:
            level, u = Q[0]
            Q = Q[1:]
            S.append((level, u.val))
            if u.left:
                Q.append((level+1, u.left))
            if u.right:
                Q.append((level+1, u.right))
            # print level, u.val
        # print S
        from collections import defaultdict
        result = defaultdict(list)
        for each in S:
            level, val = each[0], each[1]
            result[level].append(val)
        # print result
        re = [0 for i in range(max(result.keys())+1)]
        for i, j in enumerate(re):
            re[i] = float(sum(result[i]))/len(result[i])
        return re


root = TreeNode(3)
root.left = TreeNode(9)
root.left.left = TreeNode(3)
root.left.right = TreeNode(6)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

Solution.average_of_levels(root)
