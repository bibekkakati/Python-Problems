"""
Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a
scale from  1 to 100 for three categories: problem clarity, originality, and difficulty.
We define the rating for Alice's challenge to be the triplet A = (a[0],a[1],a[2]), and the rating for Bob's challenge to
be the triplet B = (b[0],b[1],b[2]).
Your task is to find their comparison points by comparing  with ,  with , and  with .

If , a[i] > b[i] then Alice is awarded  point.
If , a[i] < b[i] then Bob is awarded  point.
If , a[i] = b[i] then neither person receives a point.

Comparison points is the total points a person earned.
Return an array of two integers denoting the respective comparison points earned by Alice and Bob.
"""

from numpy import *
import random

A = array(random.sample(range(0, 100), 3))
B = array(random.sample(range(0, 100), 3))


def triplet():
    global alice, bob
    alice = 0
    bob = 0
    for i in range(0, 3):
        if A[i] == B[i]:
            print()
        elif A[i] > B[i]:
            alice += 1
        else:
            bob += 1
    print(array([alice, bob]))


print(A)

print(B)


triplet()
