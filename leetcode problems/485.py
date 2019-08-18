485. Max Consecutive Ones

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
             The maximum number of consecutive 1s is 3.

class Solution:
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    string_form=""
    for i in nums:
        string_form=string_form+str(i)
    consecutive_list=string_form.split("0")
    return len(max(consecutive_list))
