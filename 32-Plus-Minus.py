"""
Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print
the decimal value of each fraction on a new line.
"""

from numpy import *
import random

size_of_array = int(input("Enter Size of Array : "))

arr = array(random.sample(range(-100, 100), size_of_array))

size_pos = 0
size_neg = 0
size_zeros = 0


def ratio_positive_negative_zero():
    global size_pos
    global size_neg
    global size_zeros
    for i in range(0, size_of_array):
        if arr[i] > 0 & arr[i] <= 100:
            size_pos += 1
        elif arr[i] < 0 & arr[i] >= -100:
            size_neg += 1
        elif arr[i] == 0:
            size_zeros += 1


print(arr)
ratio_positive_negative_zero()
print("Zero:", size_zeros, "Positive:", size_pos, "Negative:", size_neg)
print("Zero ratio:", size_zeros/size_of_array, "Positive ratio:", size_pos/size_of_array,
      "Negative ratio:", size_neg/size_of_array)
