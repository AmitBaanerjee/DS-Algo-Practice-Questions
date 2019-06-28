You have a string of lowercase English alphabetic letters. You can perform two types of operations on the string:
Append a lowercase English alphabetic letter to the end of the string.
Delete the last character in the string. Performing this operation on an empty string results in an empty string.
Given an integer, k, and two strings, s and t, determine whether or not you can convert s to t by performing exactly k of the above operations on . If it's possible, print Yes. Otherwise, print No.
For example, strings s=[a,b,c] and t=[d,e,f]. Our number of moves, k=6. To convert s to t, we first delete all of the characters in 3 moves. Next we add each of the characters of t in order. On the 6th move, you will have the matching string. If there had been more moves available, they could have been eliminated by performing multiple deletions on an empty string. If there were fewer than  moves, we would not have succeeded in creating the new string.
Function Description
Complete the appendAndDelete function in the editor below. It should return a string, either Yes or No.
appendAndDelete has the following parameter(s):
s: the initial string
t: the desired string
k: an integer that represents the number of operations

Input Format
The first line contains a string , s the initial string.
The second line contains a string , t the desired final string.
The third line contains an integer , k the number of operations.

#!/bin/python3

import math
import os
import random
import re
import sys

def appendAndDelete(s, t, k):
    lengths=len(s)
    lengtht=len(t)
    same=0
    if lengths+lengtht<k:
        return "Yes"
    for i,j in zip(s,t):
        if i==j:
            same+=1
        else:
            break
    print(same)
    differents=lengths-same
    differentt=lengtht-same
    totaldifferent=differents+differentt
    if totaldifferent<=k and totaldifferent%2==k%2:
        return "Yes"
    else:
        return "No"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
