645. Set Mismatch

The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]

from collections import defaultdict
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate=0
        missing=0
        dic=defaultdict(int)
        for i in nums:
            dic[i]+=1
        for i in range(1,len(nums)+1):
            if i in dic:
                if dic[i]==2:
                    duplicate=i
            else:
                missing=i
        return [duplicate,missing]
