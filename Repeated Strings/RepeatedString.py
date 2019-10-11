#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count=0
    for i in list(s):
        if i == 'a':
            count+=1              #Count the 'a' in string
    sum=(n//len(s))*count         #multiply the 'a' in strings to n
    sub=n%len(s)
    for i in range(0,sub):
        if s[i]=='a':
            sum+=1
    return sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
