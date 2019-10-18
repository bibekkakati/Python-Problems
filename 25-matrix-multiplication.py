from numpy import *
import random


a = array([random.sample(range(-10, 10), 3), random.sample(range(-10, 10), 3), random.sample(range(-10, 10), 3)])
b = array([random.sample(range(-10, 10), 3), random.sample(range(-10, 10), 3), random.sample(range(-10, 10), 3)])
c = array(ones((3, 3), int))


def mat_mul():
    global a, b, c
    for i in range(0, 3):
        for j in range(0, 3):
            c[i][j] = a[i][0]*b[0][j] + a[i][1]*b[1][j] + a[i][2]*b[2][j]


mat_mul()
print("A = \n", a)
print("B = \n", b)
print("A*B = \n", c)
