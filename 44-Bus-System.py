"""
The city's bus system carries 1,200,000 people each day. How many people does the bus system carry each year? (1 year = 365 days)
Solve without using *, / operator, bitwise operator or loop.
"""

people_in_a_day = 1200000

def rec_loop(people, days):
    if(days > 0):
       return (people + rec_loop(people, days-1))
    else:
        return 0

count = 365
people_in_a_year = rec_loop(people_in_a_day, count)

print("People in a year ",people_in_a_year)
