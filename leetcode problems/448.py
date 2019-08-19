# 448. Find All Numbers Disappeared in an Array
#
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #optimal solution w/o extra space
        #pass1
        for i in range(len(nums)):
            position=abs(nums[i])
            nums[position-1]=(-1)*abs(nums[position-1])
        return [i+1 for i in range(len(nums)) if nums[i]>0]



        # if nums==[]:
        #     return
        # result=[]
        # s=set(nums)
        # for i in range(1,len(nums)+1):
        #     if i not in s:
        #         result.append(i)
        # return result
