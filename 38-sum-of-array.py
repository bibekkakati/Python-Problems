# Given an array of integers, find the sum of its elements.

from numpy import  *
import random

arr = array(random.sample(range(0,20),5))

total = 0

for num in arr:
    total += num

print("total of array ", arr, " is", total)