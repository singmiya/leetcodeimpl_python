#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 1

        a, b = 1, 2
        for _ in range(2, n):
            a, b = b, a + b

        return b

        # if n <= 0:
        #     return 0
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # a = 1
        # b = 2
        # all_ways = 0
        # while (n > 2):
        #     n -= 1
        #     all_ways = a + b
        #     a = b
        #     b = all_ways
        #
        # return all_ways

if __name__ == '__main__':
    s = Solution()
    print s.climbStairs(10)