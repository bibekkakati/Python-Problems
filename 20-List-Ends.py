# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only
# the first and last elements of the given list. For practice, write this code inside a function.
import random

def make_list(upto, how_many):
    list_a = random.sample(range(upto),how_many)
    list_b = [list_a[0], list_a[len(list_a)-1]]

    print("Generated list is: ", list_a)
    print("new list of first and last element:", list_b)

make_list(int(input("Limit of the number: ")), int(input("how many numbers: ")))