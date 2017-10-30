#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits_str = [str(x) for x in digits]
        sum = int(''.join(digits_str)) + 1
        return [int(i) for i in str(sum)]


if __name__ == "__main__":
    s = Solution()

    print s.plusOne([1, 2, 3, 4, 5])