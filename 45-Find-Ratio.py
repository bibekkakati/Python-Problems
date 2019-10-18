# Program to find ratio of two number

a = 11254
b = 502456

swap = False

if(a < b):
    a,b = b,a
    swap = True

r1 = 0
r2 = 0

if(a % b == 0):
    r1 = a/b
    r2 = 1
else:
    l = b//2
    for i in range(1, l):
        if((a % i == 0) and (b % i == 0)):
            r1 = a//i
            r2 = b//i

if(swap):
    r1,r2 = r2,r1

print(r1, '/', r2)