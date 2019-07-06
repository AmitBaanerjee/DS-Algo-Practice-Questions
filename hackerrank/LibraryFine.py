Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:
If the book is returned on or before the expected return date, no fine will be charged (i.e.:fine =0.)
If the book is returned after the expected return day but still within the same calendar month and year as the expected return date,fine =15 hackos*(the number of late days) .
If the book is returned after the expected return month but still within the same calendar year as the expected return date, the fine=500*(number of late days).
If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 hackos.
Charges are based only on the least precise measure of lateness. For example, whether a book is due January 1, 2017 or December 31, 2017, if it is returned January 1, 2018, that is a year late and the fine would be 10000 hackos.
Function Description
Complete the libraryFine function in the editor below. It must return an integer representing the fine due.
libraryFine has the following parameter(s):
d1, m1, y1: returned date day, month and year
d2, m2, y2: due date day, month and year

#!/bin/python3

import math
import os
import random
import re
import sys

def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1==y2:
        if m1==m2:
            if d1==d2:
                return 0
            elif d1>d2:
                return (d1-d2)*15
            elif d1<d2:
                return 0
        elif m1>m2:
            monthdiff= (m1-m2)
            return monthdiff*500
        elif m1<m2:
            return 0
    elif y1>y2:
        return 10000
    elif y1<y2:
        return 0
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d1M1Y1 = input().split()

    d1 = int(d1M1Y1[0])

    m1 = int(d1M1Y1[1])

    y1 = int(d1M1Y1[2])

    d2M2Y2 = input().split()

    d2 = int(d2M2Y2[0])

    m2 = int(d2M2Y2[1])

    y2 = int(d2M2Y2[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
