#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/10/28

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        _head = head
        pre_node = head
        while True:
            node = head
            s_node = self.get_s_node(node, n - 1)
            if not node:
                return list()
            if s_node.next is None:
                if id(s_node) == id(node):
                    pre_node.next = None
                else:
                    pre_node.next = node.next
                break
            else:
                pre_node = head
                head = head.next
                if head is None:
                    break
                else:
                    continue
        # print node.val
        # print pre_node.val
        # print s_node.val
        # print "--" * 20
        if id(pre_node) == id(node) == id(_head) and pre_node.next is None:
            return None
        elif id(pre_node) == id(node) == id(_head) and pre_node.next is not None:
            return pre_node.next
        else:
            return _head

    @staticmethod
    def get_s_node(node, n):
        if n <= 0:
            return node
        for e in xrange(n):
            node = node.next
        return node


node_1 = ListNode(1)
node_2 = ListNode(2)
node_1.next = node_2
# node_3 = ListNode(3)
# node_2.next = node_3
# node_4 = ListNode(4)
# node_3.next = node_4
# node_5 = ListNode(5)
# node_4.next = node_5

result = Solution().removeNthFromEnd(node_1, 2)
print result
while result:
    print result.val
    result = result.next
