import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):

    count = 0

    arr = 'QWERTYUIOPLKJHGFDSAZXCVBNM'

    arr1 = list(arr)

    l = len(s)

    for i in range(l):
        if s[i] in arr1:
            count += 1

    return(count+1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
