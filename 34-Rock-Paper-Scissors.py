# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a
# message of congratulations to the winner, and ask if the players want to start a new game.

# =========================================================
import time
import random
import sys


print("Welcome to Rock Scissors Paper Game.")

# take players name
player_1_name = input("Enter your name: ")
player_2_name = input("Enter your name: ")

# take players play input
play_1 = input("Hey "+player_1_name+"! what do you want Rock,Scissor or Paper:").lower()
play_2 = input("Hey "+player_2_name+"! what do you want Rock,Scissor or Paper:").lower()

if play_1 == play_2:
    print("Its a tie.")
elif play_1 == "rock" and play_2 == "scissor":
    print("Congratulations " + player_1_name + " You Won The Game.")
elif play_1 == "rock" and play_2 == "paper":
    print("Congratulations " + player_2_name + " You Won The Game.")
elif play_1 == "scissor" and play_2 == "rock":
    print("Congratulations " + player_2_name + " You Won The Game.")
elif play_1 == "scissor" and play_2 == "paper":
    print("Congratulations " + player_1_name + " You Won The Game.")
elif play_1 == "paper" and play_2 == "rock":
    print("Congratulations " + player_1_name + " You Won The Game.")
elif play_1 == "paper" and play_2 == "scissor":
    print("Congratulations " + player_2_name + " You Won The Game.")
else:
    print("input error: Please input from options.")


