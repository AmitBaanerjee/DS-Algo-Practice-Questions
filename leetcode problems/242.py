# 242. Valid Anagram
#
# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1={}
        dic2={}
        for i in s:
            if i not in dic1:
                dic1[i]=1
            else:
                dic1[i]+=1
        for i in t:
            if i not in dic2:
                dic2[i]=1
            else:
                dic2[i]+=1
        if dic1==dic2:
            return True
        else:
            return False
