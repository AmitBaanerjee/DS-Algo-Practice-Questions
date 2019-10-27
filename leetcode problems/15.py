15. 3Sum
Medium

4756

568

Favorite

Share
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        answer=[]
        s=set()
        for i in range(len(nums)):
            target=0-nums[i]
            left=i+1
            right=len(nums)-1
            while left<right:
                if target==nums[left]+nums[right]:
                    s.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif nums[left]+nums[right]>target:
                    right-=1
                else:
                    left+=1
        return list(s)
            
