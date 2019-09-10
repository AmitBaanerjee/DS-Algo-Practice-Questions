# 844. Backspace String Compare
#
# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
#
# Example 1:
#
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:
#
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:
#
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:
#
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".

class Solution:
    #use stacks to solve the problem
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack=[]
        t_stack=[]
        for i in s:
            if i=="#":
                if len(s_stack)>=1:
                    item=s_stack.pop()
                else:
                    pass
            else:
                s_stack.append(i)

        for i in t:
            if i=="#":
                if len(t_stack)>=1:
                    item=t_stack.pop()
                else:
                    pass
            else:
                t_stack.append(i)

        return "".join(s_stack)=="".join(t_stack)
