#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
最大数，给定一个非负整数列表，重新排列他们的顺序把他们组成一个最大的整数
例如，给定[3, 30, 34, 5, 9]，最大的组成数是9534330.
注意：结果可能非常大，所以您需要返回一个字符串，而不是整数
"""


def genMaxNumber(nums):
    a = [str(x) for x in nums]
    a.sort(reverse=True)
    print ''.join(a)


def bubbleSort(origin):
    pass


if __name__ == "__main__":
    genMaxNumber([3, 30, 34, 5, 9])
