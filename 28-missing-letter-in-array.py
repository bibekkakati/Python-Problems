"""
Write a method that takes an array of consecutive(increasing) letters as input and that returns the missig letter in the array.
"""

letters = list(input("Enter some letters:\n"))

letters = sorted(letters)

l = len(letters)

result = []

for i in range(ord(letters[0]), ord(letters[l-1])+1):
    if chr(i) in letters:
        result.append(chr(i))
    else:
        result.append(chr(i))

print(result)
