# 506. Relative Ranks
#
# Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".
#
# Example 1:
# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal".
# For the left two athletes, you just need to output their relative ranks according to their scores.

class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        nums2=sorted(nums)
        ranks=['Bronze Medal','Silver Medal','Gold Medal']
        temp=[0 for i in nums]
        for i in nums2[::-1]:
            final_index=nums.index(i)
            if ranks!=[]:
                temp[final_index]=ranks.pop()
            else:
                temp[final_index]=str(nums2[::-1].index(i)+1)
        return temp
