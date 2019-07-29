# 500. Keyboard Row
# https://leetcode.com/problems/keyboard-row/
# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
#
# Example:
#
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        frow=set("qwertyuiop")
        srow=set("asdfghjkl")
        trow=set("zxcvbnm")
        result=[]
        for i in range(len(words)):
            op=set()
            for j in range(len(words[i])):
                if words[i][j] in frow:
                    op.add(1)
                elif words[i][j] in srow:
                    op.add(2)
                elif words[i][j] in trow:
                    op.add(3)
            if len(op)==1:
                result.append(words[i])
        return result
