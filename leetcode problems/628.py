628. Maximum Product of Three Numbers
Easy

768

284

Favorite

Share
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6


Example 2:

Input: [1,2,3,4]
Output: 24


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        length=len(nums)
        return max(nums[length-1]*nums[length-2]*nums[length-3],nums[length-1]*nums[1]*nums[0])
