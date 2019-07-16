# 852. Peak Index in a Mountain Array
#
# Let's call an array A a mountain if the following properties hold:
#
# A.length >= 3
# There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
# Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].
#
# Example 1:
#
# Input: [0,1,0]
# Output: 1
# Example 2:
#
# Input: [0,2,1,0]
# Output: 1


#solution is to implement the standard binary search algorithm and return the lement which satisfies the conditions
# of the problem.

class Solution:
    def peakIndexInMountainArray(self, mountain: List[int]) -> int:
        low,high=0,len(mountain)-1
        while low<high:
            mid=(low+high)//2
            if mountain[mid]<mountain[mid+1]:
                low=mid+1
            else:
                high=mid
        return low
