#merge sort
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 21:56:04 2019

@author: reina
"""

test = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

def merge_sort(n):
    return merge_sort_helper(n)[0]

def merge_sort_helper(n):
    length = len(n)
    if length <= 1:
        return [n]
    else:
        size = int(length / 2)
        left = merge_sort_helper(n[:size])
        right = merge_sort_helper(n[size:])
        merge_call = merge(left[0],right[0])
        merged = merge_call[0]
        return [merged]


def merge(left, right):
    big = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            big.append(right[0])
            right.pop(0)
        else:
            big.append(left[0])
            left.pop(0)
    while len(left) + len(right) > 0:
        if len(left) > 0:
            big.append(left[0])
            left.pop(0)
        if len(right) > 0:
            big.append(right[0])
            right.pop(0)
    if len(big) > 0:
        return [big]


print(merge_sort(test))
