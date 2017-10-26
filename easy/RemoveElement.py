#!/usr/bin/python
# -*- coding: utf-8 -*-
import random


def remove_element(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        if length < 1:
            return 0
        if length < 2:
            if nums[0] != val:
                return 1
            return 0
        i = 0
        j = length - 1
        while i <= j:
            if nums[i] != val:
                i += 1
            else:
                if nums[j] == val:
                    j -= 1
                else:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    j -= 1
                    i += 1

        return i


if __name__ == '__main__':
    times = 30
    is_ok = True
    while times > 0:
        times -= 1
        length = random.randint(0, 15)
        nums = []
        for i in range(length):
            nums.append(random.randint(0, 7))

        val = random.randint(0, 7)
        nums1 = []
        for i in nums:
            if i != val:
                nums1.append(i)
        if len(nums1) != remove_element(nums, val):
            is_ok = False
            print ",".join([str(i) for i in nums])
            break

    if is_ok:
        print "OK!!!!!!!"
    else:
        print "出错!!!!!!"