# Brie’s Drawing teacher asks her class to open their books to a page number. Brie can either start turning pages from the front of the book or from the back of the book. She always turns pages one at a time. When she opens the book, page 1 is always on the right side:
#
# image
#
# When she flips page 1, she sees pages 2 and 3. Each page except the last page will always be printed on both sides. The last page may only be printed on the front, given the length of the book. If the book is n pages long, and she wants to turn to page p, what is the minimum number of pages she will turn? She can start at the beginning or the end of the book.
#
# Given n and p, find and print the minimum number of pages Brie must turn in order to arrive at page p.
#!/bin/python3

import os
import sys

def pageCount(n, p):
    def front():
        start=1
        flag="false"
        frontcount=0
        if p==start:
            return 0
        while flag=="false":
            start=start+2
            frontcount+=1
            if p<=start:
                flag="true"
        return frontcount
    def back():
        end=n
        backcount=0
        if end==p:
            return 0
        elif end%2!=0:
            if p==end:
                return 0
            elif p==end-1:
                return 0
            else:
                flag="false"
                while flag=="false":
                    end=end-2
                    backcount+=1
                    if p>=end:
                        flag="true"
                return backcount
        elif end%2==0:
            if p==end:
                return 0
            end=end-1
            backcount+=1
            flag="false"
            while flag=="false":
                if p==end or p ==end-1:
                    flag="true"
                end=end-2
                backcount+=1
            return backcount
    frontop=front()
    backop=back()
    output=min(frontop,backop)
    return output
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
