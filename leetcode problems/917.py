# 917. Reverse Only Letters
#
# Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.
#
# Example 1:
#
# Input: "ab-cd"
# Output: "dc-ba"
# Example 2:
#
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:
# 
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        stack=[]
        output=""
        for i in range(len(S)):
            if S[i].isalpha():
                stack.append(S[i])
        for i in range(len(S)):
            if S[i].isalpha()==False:
                output=output+S[i]
            else:
                output=output+stack.pop()
        return output
