#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) <= 0:
            return 0

        high = len(nums) - 1
        low = 0
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        if low > len(nums) - 1:
            nums.append(target)
            print "=====" + ''.join([str(i) for i in nums])
            return len(nums)

        if high < 0:
            nums.insert(0, target)
            print "=====" + ''.join([str(i) for i in nums])
            return 0

        if nums[low] > target:
            nums.insert(low, target)
            print "=====" + ''.join([str(i) for i in nums])
            return low
        else:
            nums.insert(high, target)
            print "=====" + ''.join([str(i) for i in nums])
            return high

if __name__ == '__main__':

    s = Solution()
    times = 30
    while times > 0:
        times -= 1
        length = random.randint(0, 15)
        nums = []
        for i in range(length):
            nums.append(random.randint(0, 7))

        nums = sorted(nums)
        val = random.randint(0, 7)
        print "=====" + ''.join([str(i) for i in nums])
        print "=====" + str(val)
        nums1 = []
        for i in nums:
            if i != val:
                nums1.append(i)
        print s.searchInsert(nums, val)
    # print s.searchInsert([1,4,5], 2)
