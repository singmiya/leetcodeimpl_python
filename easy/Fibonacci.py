#!/usr/bin/python
# -*- coding: utf-8 -*-

"""计算斐波那契数列
    F(1) = 1
    F(2) = 1
    .
    .
    .
    F(n) = F(n - 1) + F(n - 2)
"""


def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print fibonacci(10)