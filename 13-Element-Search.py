# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to
# largest) and another number. The function decides whether or not the given number is inside the list and returns (
# then prints) an appropriate boolean.
import random


def find(elem_list, elem_to_find):
    for elem in elem_list:
        if elem == elem_to_find:
            return True
    return False

def elem_input():
    return input("Enter the number you want to search in list : ")

el_list = random.sample(range(50), 20)

print(find(el_list, elem_input()))
print(el_list)