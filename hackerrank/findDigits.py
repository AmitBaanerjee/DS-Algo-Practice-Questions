# An integer d is a divisor of an integer n if the remainder of n/d=0.
# Given an integer, for each digit that makes up the integer determine whether it is a divisor. Count the number of divisors occurring within the integer.
# Note: Each digit is considered to be unique, so each occurrence of the same digit should be counted (e.g. for n=111, 1 is a divisor of 111 each time it occurs so the answer is 3).
# Function Description
# Complete the findDigits function in the editor below. It should return an integer representing the number of digits of d that are divisors of d.
# findDigits has the following parameter(s):
# n: an integer to analyze
# Input Format
# The first line is an integer, , indicating the number of test cases.
# The t subsequent lines each contain an integer, n.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    temp=n
    test=0
    counter=0
    while(temp):
        test = temp%10
        if not test==0:
            if (n % test)==0:
                counter+=1
        temp=temp//10
    return counter
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
