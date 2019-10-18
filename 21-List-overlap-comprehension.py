# write a program that returns a list that contains only the elements that are common between the lists (without
# duplicates). Make sure your program works on two lists of different sizes.
# using at least one list comprehension.

import random

a = random.sample(range(50),20)
b = random.sample(range(80),30)

list = [elem for elem in a for element in b if elem == element]

print(set(list))