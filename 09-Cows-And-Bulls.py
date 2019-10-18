# Create a program that will play the “cows and bulls” game with the user. The game works like this:

# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed
# correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is
#  a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user
# guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh
# game and tell the user at the end.
import random

print("Welcome to Cows and Bulls game!")

userNum = [int(uNum) for uNum in str(input("Enter any 4-digit number : "))]
randNum = [int(rNum) for rNum in str(random.randint(0, 9999))]

cows = 0
bulls = 0
bullList = []
dupList = []
dupList_1 = []
cowList = []

for i in range(0, 4):
    if userNum[i] == randNum[i]:
        cowList.append(userNum[i])
    else:
        dupList.append(userNum[i])
        dupList_1.append(randNum[i])

for x in dupList:
    for y in dupList_1:
        if dupList.count(str(x)) == dupList_1.count(str(y)):
            if str(x) == str(y):
                bullList.append(str(x))

count_1 = len(set(bullList))
count_2 = len(cowList)
bulls += count_1
cows += count_2


print("You have " + str(cows) + " cows.")
print("You have " + str(bulls) + " bulls.")
