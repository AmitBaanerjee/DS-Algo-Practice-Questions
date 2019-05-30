# Anna and Brian are sharing a meal at a restuarant and they agree to split the bill equally. Brian wants to order something that Anna is allergic to though, and they agree that Anna won't pay for that item. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.
#
# For example, assume the bill has the following prices: bill=[2,4,6]. Anna declines to eat item k=bill[2] which costs 6. If Brian calculates the bill correctly, Anna will pay (2+4)/2. If he includes the cost of bill[2], he will calculate (2+4+2)/2. In the second case, he should refund 3 to Anna.
#
# Function Description
#
# Complete the bonAppetit function in the editor below. It should print Bon Appetit if the bill is fairly split. Otherwise, it should print the integer amount of money that Brian owes Anna.
#
# bonAppetit has the following parameter(s):
#
# bill: an array of integers representing the cost of each item ordered
# k: an integer representing the zero-based index of the item Anna doesn't eat
# b: the amount of money that Anna contributed to the bill

#!/bin/python

import math
import os
import random
import re
import sys

def bonAppetit(ar, k, b):
    annaBill = sum(ar[i] for i in range(len(ar)) if i != k)//2
    print 'Bon Appetit' if annaBill == b else str(b-annaBill)
if __name__ == '__main__':
    nk = raw_input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = map(int, raw_input().rstrip().split())

    b = int(raw_input().strip())

    bonAppetit(bill, k, b)
