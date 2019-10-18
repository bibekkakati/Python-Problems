"""
Print the following pattern

        * *
        * *
      * * * *
      * * * *
    * * * * * *
    * * * * * *
  * * * * * * * *
  * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *

"""


st = int(input("Enter the number of stairs"))

#make the stairs even

st=st+1 if(st % 2 != 0) else st

star = 2

space = st - 2

for i in range(1, st+1):
    for j in range(0, space):
        print(" ", end = "")
    for k in range(0, star):
        print("* ", end = "")
    print("\n")
    if(i % 2 == 0):
        space = space - 2
        star = star + 2