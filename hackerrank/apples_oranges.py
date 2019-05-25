#APPLES AND ORANGES
# Function Description
#
# Complete the countApplesAndOranges function in the editor below. It should print the number of apples and oranges that land on Sam's house, each on a separate line.
#
# countApplesAndOranges has the following parameter(s):
#
# s: integer, starting point of Sam's house location.
# t: integer, ending location of Sam's house location.
# a: integer, location of the Apple tree.
# b: integer, location of the Orange tree.
# apples: integer array, distances at which each apple falls from the tree.
# oranges: integer array, distances at which each orange falls from the tree.
# Input Format
#
# The first line contains two space-separated integers denoting the respective values of s and t.
# The second line contains two space-separated integers denoting the respective values of a and b.
# The third line contains two space-separated integers denoting the respective values of m and n.
# The fourth line contains  space-separated integers denoting the respective distances that each apple falls from point a.
# The fifth line contains  space-separated integers denoting the respective distances that each orange falls from point b.
#
# Constraints
#
# Output Format
#
# Print two integers on two different lines:
#
# The first integer: the number of apples that fall on Sam's house.
# The second integer: the number of oranges that fall on Sam's house.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(start, end, atree, otree, apples, oranges):
    alist,olist=0,0
    for i in apples:
        i=atree+i
        if start<=i<=end:
            alist+=1
    for i in oranges:
        i=otree+i
        if start<=i<=end:
            olist+=1
    print(alist)
    print(olist)
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
