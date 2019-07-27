# 821. Shortest Distance to a Character
#
# Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.
#
# Example 1:
#
# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

class Solution:
    def shortestToChar(self, string: str, character: str) -> List[int]:
        indexes=[]
        output=[]
        for i in range(len(string)):
            if string[i]==character:
                indexes.append(i)
        for i in range(0,len(string)):
            m=[]
            for j in indexes:
                m.append(abs(i-j))
            output.append(min(m))
        return output
