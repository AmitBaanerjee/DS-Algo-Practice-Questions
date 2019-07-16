# 942. DI String Match
#
# Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
#
# Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
#
# If S[i] == "I", then A[i] < A[i+1]
# If S[i] == "D", then A[i] > A[i+1]
#
# Example 1:
#
# Input: "IDID"
# Output: [0,4,1,3,2]
# Example 2:
#
# Input: "III"
# Output: [0,1,2,3]
# Example 3:
#
# Input: "DDI"
# Output: [3,2,0,1]

class Solution:
    def diStringMatch(self, string: str) -> List[int]:
        leftcounter=0
        rightcounter=len(string)
        result=[]
        for i in string:
            if i=="I":
                result.append(leftcounter)
                leftcounter+=1
            elif i=="D":
                result.append(rightcounter)
                rightcounter-=1
        if string[-1]=="D":
            result.append(rightcounter)
        else:
            result.append(leftcounter)
        return result

#L R
#----
#1 4
#1 3
#2 3
#2 2
