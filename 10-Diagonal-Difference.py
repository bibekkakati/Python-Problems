"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
"""
from numpy import *
import random

a = int(input("Enter the size of matrix (max = 4) : "))

A = array([random.sample(range(-100, 100), a), random.sample(range(-100, 100), a), random.sample(range(-100, 100), a), random.sample(range(-100, 100), a)])

diagonal_1 = []
diagonal_2 = []


def ab_diff():
    global diagonal_1
    global diagonal_2
    i = 0
    j = 0
    while i < a:
        diagonal_1.append(A[i][j+i])
        i += 1
    i = 0
    j = a-1
    while i < a:
        diagonal_2.append(A[i][j-i])
        i += 1


ab_diff()

absolute_diff = abs(sum(diagonal_1) - sum(diagonal_2))

print("Generated matrix is \n", A)
print("First diagonal is ", diagonal_1)
print("Second diagonal is ", diagonal_2)
print("Absolute difference between the sum of diagonals is ", absolute_diff)
