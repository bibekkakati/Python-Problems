# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them
# whether they guessed too low, too high, or exactly right.
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

number = random.randint(1, 9)
guess = []

userGuess = input("Guess any number between 1 and 9 : ")
guess.append(userGuess)

if userGuess.lower() == "exit":
    print("Better luck next time.")

while userGuess.lower() != "exit":

    if int(userGuess) == number:
        print("Exactly right.")
        break
    elif int(userGuess) > number:
        print("Too high.")
        break
    elif int(userGuess) < number:
        print("Too low.")
        break
    else:
        print("No input")