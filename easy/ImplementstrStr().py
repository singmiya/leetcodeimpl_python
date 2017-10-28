#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import string


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if len(needle) <= 0:
        return 0
    i = 0
    j = 0
    next = getNext(needle)
    while i < len(haystack) and j < len(needle):
        if j == -1 or haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            j = next[j]

    if j == len(needle):
        return i - j
    else:
        return -1

def getNext(needle):
    next = [0 for i in range(len(needle))]
    next[0] = -1
    j = 0
    k = -1
    while(j < len(needle) - 1):
        if k == -1 or needle[j] == needle[k]:
            j += 1
            k += 1
            if needle[j] == needle[k]:
                next[j] = next[k]
            else:
                next[j] = k
        else:
            k = next[k]

    return next


if __name__ == '__main__':
    l1 = random.randint(20, 40)
    haystack = random.sample("abcd" * 240, l1)
    l2 = random.randint(3, 6)
    needle = random.sample("abcd" * 2, l2)

    # haystack = ''.join(haystack)
    # needle = ''.join(needle)
    haystack = ''.join("")
    needle = ''.join("")
    print strStr(list(haystack), list(needle))
