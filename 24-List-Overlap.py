# Take two lists, say for example these two:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
#
# Extras:
#
# Randomly generate two lists to test this

import random

a = random.sample(range(30), 15)
b = random.sample(range(40), 20)
list = []

for elem in a:
    for element in b:
        if elem == element:
            list.append(elem)

# list overlap comprehension =======
# list = [elem for elem in a for element in b if elem == element]

print(list)

