# 541. Reverse String II
# Easy
#
# 274
#
# 850
#
# Favorite
#
# Share
# Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
# Example:
#
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
#

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a=list(s)
        for i in range(0,len(s),2*k):
            a[i:i+k]=reversed(a[i:i+k])
        return "".join(a)
