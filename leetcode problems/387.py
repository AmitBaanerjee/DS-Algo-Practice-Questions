# 387. First Unique Character in a String
#
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.

from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic=defaultdict(int)
        for i in s:
            dic[i]+=1

        print(dic)
        for i in s:
            if dic[i]==1:
                return s.index(i)
        return -1
