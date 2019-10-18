"""
Sam is a professor at the university and likes to round each student's grade according to these rules:

If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
"""

from numpy import *
import random

n = int(input("Enter no. of grades to be generated: "))

grades = array(random.sample(range(0,101), n))

print("Initial grades:", grades)


def stu_grade():
    for i in range(0, len(grades)):
        if grades[i] < 38:
            grades[i] = grades[i]
        else:
            for j in range(1, 3):
                if (grades[i] + j) % 5 == 0:
                    grades[i] = grades[i] + j
                else:
                    grades[i] = grades[i]

    print("Up grades:", grades)


stu_grade()
