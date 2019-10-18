# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the
# user. If the number is a multiple of 4, print out a different message. Ask the user for two numbers: one number to
# check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user.
# If not, print a different appropriate message.

num = int(input("Please enter a number: "))
check = int(input("Enter another number: "))

div = num / check

if num % 2 == 0:
    print("Entered first number is even.")
else:
    print("Entered first number is odd.")

if num % 4 == 0:
    print("number is multiple of 4.")
else:
    print("Number is not a multiple of 4.")

if div % 2 == 0:
    print("Second number evenly divides into first number.")
else:
    print("Second number dosen't evenly divides into first number.")