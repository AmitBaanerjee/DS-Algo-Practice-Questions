# 283. Move Zeroes
#
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

class Solution:
    def find_index(self,index,nums):
        for i in range(index,len(nums)):
            if nums[i]!=0:
                return i
        return None

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            if nums[i]==0:
                if nums[i+1]!=0:
                    nums[i],nums[i+1]=nums[i+1],nums[i]
                elif nums[i+1]==0:
                    result=self.find_index(i+1,nums)
                    if result==None:
                        break
                    else:
                        nums[i],nums[result]=nums[result],nums[i]
        print(nums)
