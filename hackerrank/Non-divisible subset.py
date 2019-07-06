# Given a set of distinct integers, print the size of a maximal subset of S where the sum of any  numbers in S is not evenly divisible by k.
# For example, the array S=[19,10,12,10,24,25,22] and k=4. One of the arrays that can be created is S'[0]=10,12,25. Another is S''[1]=[19,22,24]. After testing all permutations, the maximum length solution array has 3 elements.
# Function Description
# Complete the nonDivisibleSubset function in the editor below. It should return an integer representing the length of the longest subset of  meeting the criteria.
# nonDivisibleSubset has the following parameter(s):
# S: an array of integers
# k: an integer


#example scenario
# k=4
# s=[19,10,12,10,24,25,22]
#output=3

remainderlist=[x%k for x in s ]
count=0
if 0 in remainderlist:
    count+=1
remainderlist=[x for x in remainderlist if x !=0]

counter=[0]*k
for i in range(len(remainderlist)):
    counter[remainderlist[i]]+=1

index=[]
for i in range(len(counter)):
    maxcount=max(counter)
    maxremainder=counter.index(maxcount)

    if k-maxremainder not in index and maxcount!=0:
        index.append(maxremainder)

        if (maxremainder*2)%k==0:
            count+=1
        else:
            count=count+maxcount

    counter[maxremainder]=0
