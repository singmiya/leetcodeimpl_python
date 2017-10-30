#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from math import sqrt

"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = x
        while low <= high:
            mid = (low + high) / 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
        return high


if __name__ == "__main__":
    s = Solution()
    num = random.randint(1, 1000)
    print "num === " + str(num)
    print "math.sqrt root === " + str(int(sqrt(num)))
    print "mysqrt root === " + str(s.mySqrt(num))
