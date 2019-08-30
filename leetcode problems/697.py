# 697. Degree of an Array
#
# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
#
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
#
# Example 1:
#
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation:
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:
#
# Input: [1,2,2,3,1,4,2]
# Output: 6

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #first find number with the max frequency
        #check where that number starts and on which index it ends
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        maxfreq=max(dic.values())
        maxfreq_numbers=[]

        for i in dic:
            if dic[i]==maxfreq:
                maxfreq_numbers.append(i)

        values=[]
        for i in maxfreq_numbers:
            start_index=nums.index(i)
            last_index=(len(nums)-1)-nums[::-1].index(i)
            values.append(len(nums[start_index:last_index+1]))

        return min(values)
