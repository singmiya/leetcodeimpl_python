#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = l1
        l2_ = l2
        quotient = 0
        while True:
            s = l1.val + l2.val + quotient
            quotient = s / 10
            l1.val = s % 10
            if l1.next is None or l2.next is None:
                break
            l1 = l1.next
            l2 = l2.next

        if l1.next is not None:
            l1 = l1.next
            while True:
                s = l1.val + quotient
                quotient = s / 10
                l1.val = s % 10
                if l1.next is None:
                    break
                l1 = l1.next

        if l2.next is not None:
            l2 = l2.next
            while True:
                s = l2.val + quotient
                quotient = s / 10
                if l2_ is not None:
                    l1.next = l2_
                    l1 = l1.next
                    l1.val = s % 10
                    l1.next = None
                    l2_ = l2_.next
                else:
                    l1.next = ListNode(s % 10)
                    l1 = l1.next
                if l2.next is None:
                    break
                l2 = l2.next

        if quotient > 0:
            if l2_ is not None:
                l1.next = l2_
                l2_.val = quotient
                l2_.next = None
            else:
                l1.next = ListNode(quotient)

        return sum

if __name__ == '__main__':
    l1 = ListNode(0)
    # l1_ = l1
    # l1_.next = ListNode(3)
    # l1_ = l1_.next
    # l1_.next = ListNode(6)
    # l1_ = l1_.next
    # l1_.next = ListNode(5)
    # l1_ = l1_.next
    # l1_.next = ListNode(5)
    # l1_ = l1_.next
    # l1_.next = ListNode(5)
    # l1_ = l1_.next
    # l1_.next = ListNode(5)
    # l1_ = l1_.next

    l2 = ListNode(2)
    l2_ = l2
    l2_.next = ListNode(7)
    l2_ = l2_.next
    l2_.next = ListNode(8)
    # l2_ = l2_.next
    # l2_.next = ListNode(8)
    # l2_ = l2_.next

    Solution().addTwoNumbers(l1, l2)
