Divisible sum pairs
You are given an array of n integers, ar=ar[0],ar[1],.. and a positive integer,k . Find and print the number of (i,j) pairs where i<j and ar[i] + ar[j] is divisible by k.

For example, ar=[1,2,3,4,5,6] and k=3. Our three pairs meeting the criteria are [1,4],[2,3] and [4,6].

Function Description

Complete the divisibleSumPairs function in the editor below. It should return the integer count of pairs meeting the criteria.

divisibleSumPairs has the following parameter(s):

n: the integer length of array ar
ar: an array of integers
k: the integer to divide the pair sum by
Input Format

The first line contains 2 space-separated integers, n and k.
The second line contains n space-separated integers describing the values of ar .

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    counter=0
    for i in range(len(ar)):
        j=i+1
        while j<len(ar):
            if (ar[i]+ar[j])%k==0:
                counter+=1
            j+=1
    return counter
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
