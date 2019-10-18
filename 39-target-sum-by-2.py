
"""   S A T U R D A Y   C O D I N G   C H A L L E N G E   """

# Name : Bibek Kakati

# Challenge Name: Target Sum By 2

# Video Link: https://youtu.be/HJxQUDaNOgI ( ~ Hitesh Choudhary )


"""

PROBLEM:
    Given an array of N numbers and another number S.
    Find any two numbers whose sum is exactly S.

EXAMPLE:
    If Array = [4,6,8,12,-4,10] and Sum = 8
    then Result = [12,-4]
    
SOLUTION APPROACH:
    We will use a for loop for iteration and if-else statement to check the presence of element.

"""


""" H E R E   I S   T H E   C O D E """


arr = list(map(int, input("Enter the numbers ( give space between numbers ):\n").split()))  # array input

s = int(input("Enter any number: "))  # sum to compare

length = len(arr)  # length of array

result = []  # empty list to store the result(two numbers)

for i in arr:  # iteration through elements in array
    a = s - i  # a will store the value which is difference between sum and each elements in array
    if a in arr:  # if value of a is found in array
        result.extend([i, a])
    else:
        continue
    if result:  # break the loop to avoid storing repeated values
        break

print(arr)  # to print given array

if not result:  # if no two such numbers exist
    print("Sum of any two numbers in the given array is not equal to ", s)
else:
    print(result)  # to print resultant array
