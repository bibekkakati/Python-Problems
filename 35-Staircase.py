"""
Print a staircase of size n using # symbols and spaces.
"""

size = 10

for i in range(1, size+1):
    """ To remove preceded spaces......"""
    if i == 10:
        print("#"*i)
    else:
        print(" "*(size-(i+1)), "#"*i)
