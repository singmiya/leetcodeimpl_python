#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def compareBinaryTree(p, q):
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            elif p.val == q.val:
                l = compareBinaryTree(p.left, q.left)
                r = compareBinaryTree(p.right, q.right)
                if l is True and r is True:
                    return True
                else:
                    return False
            else:
                return False

        return compareBinaryTree(p, q)


if __name__ == "__main__":
    t1 = TreeNode(0)
    t1.left = TreeNode(1)
    t1.left.left = TreeNode(1)
    t1.left.right = TreeNode(1)
    t1.right = TreeNode(1)
    t1.right.left = TreeNode(0)
    t1.right.right = TreeNode(1)
    t2 = TreeNode(0)
    t2.left = TreeNode(1)
    t2.left.left = TreeNode(1)
    t2.left.right = TreeNode(1)
    t2.right = TreeNode(1)
    t2.right.left = TreeNode(0)
    t2.right.right = TreeNode(1)

    print Solution().isSameTree(t1, t2)
