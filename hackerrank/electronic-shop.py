# Monica wants to buy a keyboard and a USB drive from her favorite electronics store. The store has several models of each. Monica wants to spend as much as possible for the  items, given her budget.
#
# Given the price lists for the store's keyboards and USB drives, and Monica's budget, find and print the amount of money Monica will spend. If she doesn't have enough money to both a keyboard and a USB drive, print -1 instead. She will buy only the two required items.
#
# For example, suppose she has b=60 to spend. Three types of keyboards cost keyboards=[40,50,60]. Two USB drives cost drives=[5,8,12]. She could purchase a 40 keyboard+12 drives=52, or a 50 keyboard+ 8 usb=58. She chooses the latter. She can't buy more than 2 items so she can't spend exactly 60.
#
# Function Description
#
# Complete the getMoneySpent function in the editor below. It should return the maximum total price for the two items within Monica's budget, or -1 if she cannot afford both items.
#
# getMoneySpent has the following parameter(s):
#
# keyboards: an array of integers representing keyboard prices
# drives: an array of integers representing drive prices
# b: the units of currency in Monica's budget

#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    output=-1
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            if output<drives[j]+keyboards[i]<=b:
                output=drives[j]+keyboards[i]
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
