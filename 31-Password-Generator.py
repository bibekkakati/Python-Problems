# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of
# lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new
# password every time the user asks for a new password. Include your run-time code in a main method.
import random

char = "qwertyuioplkjhgfdsazxcvbnm1234567890@#!$%&*QWERTYUIOPLKJHGFDSAZXCVBNM"

passLen = int(input("Enter the passcode length (min: 6 and max: 12) : "))


password = "".join(random.sample(char,passLen))

if passLen in range(6,13):
    print(password)
else:
    print("input error")