# 557. Reverse Words in a String III
#
# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#
# Example 1:
#
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.

class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse_word(word):
            answer=""
            for i in range(len(word)-1,-1,-1):
                answer=answer+word[i]
            return answer

        words,reversed_words=s.split(" "),[]
        for i in words:
            reversed_words.append(reverse_word(i))
        return (" ".join(reversed_words))
