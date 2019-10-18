"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the
five integers.Then print the respective minimum and maximum values as a single line of two space-separated long integers
"""

from numpy import *
import random


def min_max():
    arr = array(random.sample(range(0, 20), 10))
    arr_s = sort(arr)
    length = len(arr_s)
    min_sum = 0
    max_sum = 0
    for i in range(0, length-1):
        min_sum += arr_s[i]
    for j in range(length-1, 0, -1):
        max_sum += arr_s[j]

    print("array is:", arr_s)
    print("minimum sum:", min_sum, "    ","maximum sum:", max_sum)
    print("length:", length)


min_max()
