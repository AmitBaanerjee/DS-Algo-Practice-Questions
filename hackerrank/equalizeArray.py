# Karl has an array of integers. He wants to reduce the array until all remaining elements are equal. Determine the minimum number of elements to delete to reach his goal.
# For example, if his array is arr=[1,2,2,3], we see that he can delete the 2 elements 1 and 3 leaving arr=[2,2]. He could also delete both twos and either the 1 or the 3, but that would take 3 deletions. The minimum number of deletions is .
# Function Description
# Complete the equalizeArray function in the editor below. It must return an integer that denotes the minimum number of deletions required.
# equalizeArray has the following parameter(s):
# arr: an array of integers

import math
import os
import random
import re
import sys

def equalizeArray(arr):
    dic={}
    for i in arr:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]=dic[i]+1
    result=len(arr)-max(dic.values())
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
