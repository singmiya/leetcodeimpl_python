#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
"""
import copy
import random


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        l1 = len(nums1)
        for i in range(l1 - m):
            nums1.pop(len(nums1) - 1)
        l2 = len(nums2)
        for i in range(l2 - n):
            nums2.pop(len(nums2) - 1)

        i, j = 0, 0
        while (i < m and j < n):
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                nums1.insert(i, nums2[j])
                i += 1
                j += 1
            m = len(nums1)

        while (j < n):
            nums1.append(nums2[j])
            j += 1

        # print nums1

if __name__ == "__main__":
    s = Solution()
    # length = random.randint(0, 40)
    # nums1 = []
    # for i in range(length):
    #     nums1.append(random.randint(0, 15))
    # length1 = random.randint(0, 40)
    # nums2 = []
    # for i in range(length1):
    #     nums2.append(random.randint(0, 13))
    # nums1 = sorted(nums1)
    # nums2 = sorted(nums2)
    # # length1 = 0
    # # length = 0
    # print nums1
    # print nums2
    # s.merge(nums1, length, nums2, length1)
    nums1, m, nums2, n = [1,2,3,0,0,0], 3, [2,5,6], 3
    s.merge(nums1, m, nums2, n)
    # nums1 = nums1[:0]
    print nums1
