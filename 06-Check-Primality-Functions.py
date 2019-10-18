# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten,
# a prime number is a number that has no divisors.)


def user_number():
    return int(input("Enter any number : "))


user_input = user_number()

a = [x for x in range(2,user_input) if user_input % x == 0]

if user_input > 1:
    if len(a) == 0:
        print('prime')
    else:
        print('NOT prime')
else:
    print('NOT prime')