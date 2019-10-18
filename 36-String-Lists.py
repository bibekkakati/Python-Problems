# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

string = str(input("Write any word to check if it is palindrome: "))
stringList = []

for s in string:
    stringList.append(s)
a = stringList[::-1]
if a == stringList:
    print("Yes, It is palindrome.")
else:
    print("It is not a palindrome.")
