# You have been asked to help study the population of birds migrating across the continent. Each type of bird you are interested in will be identified by an integer value. Each time a particular kind of bird is spotted, its id number will be added to your array of sightings. You would like to be able to find out which type of bird is most common given a list of sightings. Your task is to print the type number of that bird and if two or more types of birds are equally common, choose the type with the smallest ID number.
#
# For example, assume your bird sightings are of types arr=[1,1,2,2,3]. There are two each of types 1 and 2, and one sighting of type 3. Pick the lower of the two types seen twice: type 1.
#
# Function Description
#
# Complete the migratoryBirds function in the editor below. It should return the lowest type number of the most frequently sighted bird.
#
# migratoryBirds has the following parameter(s):
#
# arr: an array of integers representing types of birds sighted

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    dic=defaultdict(int)
    for i in arr:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    maxval=max(dic.values())
    resultlist=[]
    for i in dic:
        if dic[i]==maxval:
            resultlist.append(i)
    return resultlist[0]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
