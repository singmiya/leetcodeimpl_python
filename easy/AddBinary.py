#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ab = [int(i) for i in a]
        bb = [int(i) for i in b]
        suma = 0
        sumb = 0
        for i, j in enumerate(ab):
            suma += j * pow(2, len(ab) - i - 1)
        for i, j in enumerate(bb):
            sumb += j * pow(2, len(bb) - i - 1)

        return "{0:b}".format(suma + sumb)


if __name__ == "__main__":
    s = Solution()
    # s.addBinary("111", "110")
    print s.addBinary("111", "110")
