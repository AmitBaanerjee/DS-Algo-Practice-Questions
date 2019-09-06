# 830. Positions of Large Groups
#
# In a string S of lowercase letters, these letters form consecutive groups of the same character.
#
# For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".
#
# Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.
#
# The final answer should be in lexicographic order.
#
#
#
# Example 1:
#
# Input: "abbxxxxzzy"
# Output: [[3,6]]
# Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
# Example 2:
#
# Input: "abc"
# Output: []
# Explanation: We have "a","b" and "c" but no large group.
# Example 3:
#
# Input: "abcdddeeeeaabbbcd"
# Output: [[3,5],[6,9],[12,14]]

class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        result=[]
        i=0
        while i <(len(S)-1):
            if S[i+1]==S[i]:
                start=i
                end=i
                j=i+1
                while(j<len(S) and S[j]==S[i]):
                    end+=1
                    j+=1
                if end-start>=2:
                    result.append([start,end])
                    i=end
            i+=1
        return result
