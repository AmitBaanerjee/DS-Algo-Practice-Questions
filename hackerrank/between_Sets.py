#BETWEEN TWO SETS
# You will be given two arrays of integers and asked to determine all integers that satisfy the following two conditions:
#
# The elements of the first array are all factors of the integer being considered
# The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays. You must determine how many such numbers exist.
#
# For example, given the arrays a=[2,6] and b=[24,36], there are two numbers between them: 6 and 12.6%2=0 ,6%6=0 ,24%6=0  and 36%6=0 for the first value. Similarly, 12%2=0 ,12%6=0  and 24%12=0,36%12=0 .
#
# Function Description
#
# Complete the getTotalX function in the editor below. It should return the number of integers that are betwen the sets.
#
# getTotalX has the following parameter(s):
#
# a: an array of integers
# b: an array of integers

#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):

    alast=a[-1]
    bfirst=b[0]
    op=0
    for i in range(alast,bfirst+1):
        countera,counterb=0,0
        for j in a:
            if i%j==0:
                countera+=1
        for k in b:
            if k%i==0:
                counterb+=1
        if counterb==len(b) and countera==len(a):
            op+=1
    return op

print(getTotalX([2,4],[16,32,96]))
#output should be 3
