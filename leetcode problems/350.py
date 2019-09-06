# 350. Intersection of Two Arrays II
#
# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]

class Solution:

    def intersect(self, nums1, nums2):
        nums1.sort(), nums2.sort()
        intersection = []
        for i in range(0,len(nums1)):
            status = self.BinarySearch(nums2,nums1[i])
            if status == True:
                intersection.append(nums1[i])
        return intersection

    def BinarySearch(self,nums,target):
        initial, final = 0 , len(nums)-1
        while initial <= final :
            middle_element = (initial+final)//2
            if nums[middle_element] > target:
                final = middle_element-1
            if nums[middle_element] < target:
                initial = middle_element +1
            if nums[middle_element] == target:
                nums.pop(middle_element)
                return True
        return False
