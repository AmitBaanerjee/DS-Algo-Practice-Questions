# 1078. Occurrences After Bigram
#
# Given words first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.
#
# For each such occurrence, add "third" to the answer, and return the answer.
#
# Example 1:
#
# Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
# Output: ["girl","student"]
# Example 2:
#
# Input: text = "we will we will rock you", first = "we", second = "will"
# Output: ["we","rock"]

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        third=[]
        text=text.strip().split()
        for i in range(len(text)):
            if text[i]==first:
                if (i+1<len(text) and text[i+1]==second):
                    if (i+1+1<len(text)):
                        third.append(text[i+1+1])
        return third
