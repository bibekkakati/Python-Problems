# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to
# the user the same string, except with the words in backwards order.

userInput = input("Write something : ")


def reverseSentence():
    rev = userInput.split()
    rev.reverse()
    return " ".join(rev)


print(reverseSentence())