"""
Chef and his friends were playing Passing the Parcel.

There are a total of N kids playing the game. Let their numbers be 1,2,3...N.

All N kids were made to sit uniformly in a circle in number order (ie. from 1 to N in CLOCKWISE DIRECTION).

The Parcel is first handed over to the first kid.

After getting bored, chef thought to try something different. He randomly started to ask his friends how far you will be
from parcel after passing it for t time units. (In one time unit, the parcel is passed from one kid to other in
clockwise direction.)

If you are holding parcel then you are 0 (zero) distance away from parcel.
Being far, is smallest distance between between kid and parcel.
Consider Example :

             1   2   3

             8       4

             7   6   5
If parcel is at 2, distance of kid 5 from parcel is 3.

INPUT :

First line will contain two integers N and Q, number of kids and number of queries.
Then the Q queries follow.
Each query contains two integers T, X, time for which parcel is circulated and kid's number.

Output:
For each query, output in a single line answer the distance between the X^th kid and the parcel.

Constraints
1 ≤ N,T ≤ 10^8
1 ≤ Q ≤ 10^5
1 ≤ X ≤ N
"""


def play_parcel():

    time = []
    xth_child = []
    kids = []

    n = int(input("Enter number of kids : "))
    q = int(input("Enter number of queries : "))

    while True:
        if (n < 1) | (n > 10**8) | (n == ""):
            print("Input error | Limit exceeded or Blank input")
            break
        else:
            for i in range(0, q):
                t = int(input("Time for which parcel is circulated : "))
                x = int(input("Kid\'s number : "))
                if (t < 1) | (t > 10**8) | (t == "") | (x < 1) | (x > n) | (x == ""):
                    print("Input error | Limit exceeded or Blank input")
                    break
                else:
                    if i > 0:
                        time.append(t + time[i-1])
                    else:
                        time.append(t)
                    xth_child.append(x)
        for i in range(0, n):
            kids.append(i+1)
        for i in range(0, q):
            dist = abs((xth_child[i] - (time[i] + 1)))
            if dist >= 10:
                dist = dist - 10

            if i > 0:
                print("Distance between", xth_child[i], " and", (time[i] - time[i-1]), " is", dist)
            else:
                print("Distance between", xth_child[i], " and", time[i], " is", dist)
        break


play_parcel()
