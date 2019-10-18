"""
You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line
ready to jump in the positive direction (i.e, toward positive infinity).

The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is
possible, return YES, otherwise return NO.
"""


# def kangaroo():
#     dis_vel = []
#     for i in range(0, 4):
#         if i == 0 or i == 2:
#             ask_user = int(input("Enter initial point : "))
#         else:
#             ask_user = int(input("Enter jumping distance : "))
#         dis_vel.append(ask_user)

#     """ ===================== LOOPING =================== """

#     first_kang_pos = dis_vel[0]
#     second_kang_pos = dis_vel[2]
#     for j in range(0, 10000):
#         first_kang_pos += dis_vel[1]
#         second_kang_pos += dis_vel[3]
#         if first_kang_pos == second_kang_pos:
#             print("YES in distance :", j)
#             break
#         elif j == 10000-1:
#             print("No")

#     """ ================ MATHEMATICAL FORMULA ( NOT SURE ** COPY-PASTE ) ==================== """

#     # if ((dis_vel[0] - dis_vel[2]) % (dis_vel[1] - dis_vel[3])) == 0:
#     #     print("YES")
#     # else:
#     #     print("NO")


# kangaroo()

def distance_covered(time):
    if (time>0):
        return distance_covered(time-1) + 2
    else:
        return 0

speed = 2 #m/s
time = 4 #mins
time = 4*60 #seconds

res = distance_covered(time)
print(res)
