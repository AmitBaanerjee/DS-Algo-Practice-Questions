# 268. Missing Number
#
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
# Example 1:
#
# Input: [3,0,1]
# Output: 2
# Example 2:
#
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        #edge cases
        if nums[-1]!=len(nums):
            return len(nums)
        elif nums[0]!=0:
            return 0

        for i in range(1,len(nums)):
            current=nums[i-1]+1
            if nums[i]!=current:
                return current
