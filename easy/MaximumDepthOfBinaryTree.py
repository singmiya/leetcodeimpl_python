#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        # if not root.left and not root.right:
        #     return 1
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

if __name__ == "__main__":
    t1 = TreeNode(0)
    t1.left = TreeNode(1)
    # t1.left.left = TreeNode(1)
    t1.left.right = TreeNode(1)
    t1.right = TreeNode(1)
    # t1.right.left = TreeNode(0)
    t1.right.right = TreeNode(1)
    t2 = TreeNode(0)
    t1.right.right.left = t2
    t2.left = TreeNode(1)
    t2.left.left = TreeNode(1)
    t2.left.right = TreeNode(1)
    t2.right = TreeNode(1)
    t2.right.left = TreeNode(0)
    t2.right.right = TreeNode(1)
    print Solution().maxDepth(t1)
