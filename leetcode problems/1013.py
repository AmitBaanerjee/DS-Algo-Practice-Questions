# 1013. Partition Array Into Three Parts With Equal Sum
#
# Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.
#
# Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])
#
# Example 1:
#
# Input: [0,2,1,-6,6,-7,9,1,2,0,1]
# Output: true
# Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
# Example 2:
#
# Input: [0,2,1,-6,6,7,9,-1,2,0,1]
# Output: false
# Example 3:
#
# Input: [3,3,6,5,-2,2,5,1,-9,4]
# Output: true
# Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

# class Solution:
#     def canThreePartsEqualSum(self, array: List[int]) -> bool:
#         total=sum(array)
#         partition_sum=total//3
#         partitions=[]
#         temp_sum=0
#         pointer=0
#         for i in range(len(array)):
#             temp_sum+=array[i]
#             if temp_sum==partition_sum:
#                 temp_sum=0
#                 partitions.append(array[pointer:i+1])
#                 pointer=i+1
#         return len(partitions)==3

    #betterment of efficiency try
class Solution:
    def canThreePartsEqualSum(self, array: List[int]) -> bool:
        total=sum(array)
        temp_sum=0
        counter=0
        for i in range(len(array)):
            temp_sum+=array[i]
            if temp_sum==total//3:
                temp_sum=0
                counter+=1
        return counter==3
