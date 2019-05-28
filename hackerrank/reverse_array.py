#REVERSE ARRAY IN ORDER
# Given an array,A , of N integers, print each element in reverse order as a single line of space-separated integers.
#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the reverseArray function below.
def reverseArray(a):
    length=len(a)-1
    for i in range(len(a)//2):
        temp=a[i]
        a[i]=a[length-i]
        a[length-i]=temp
    return a
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
