16. 3Sum Closest

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        answer=nums[1]+nums[2]+nums[0]
        for i in range(len(nums)-2):
            num1=nums[i]
            left=i+1
            right=len(nums)-1
            while(left<right):
                total=nums[i]+nums[left]+nums[right]
                if total==target:
                    return total
                if abs(total-target)<abs(answer-target):
                    answer=total
                if total<target:
                    left+=1
                else:
                    right-=1
        return answer
