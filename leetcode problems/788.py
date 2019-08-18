# 788. Rotated Digits
#
# X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.
#
# A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.
#
# Now given a positive number N, how many numbers X from 1 to N are good?
#
# Example:
# Input: 10
# Output: 4
# Explanation:
# There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

class Solution:
    def rotatedDigits(self, N: int) -> int:
        count=0
        dictionary={'2':'5','5':'2','6':'9','9':'6','0':'0','1':'1','8':'8'}
        for i in range(1,N+1):
            string_form=str(i)
            rotated_form=""
            for letter in string_form:
                if letter not in dictionary:
                    #ignore this number
                    break
                else:
                    rotated_form+=dictionary[letter]
            else:
                if (rotated_form!=string_form):
                    count+=1
        return count

    ##ALTERNATIVE
#     for i in range(1,N+1):
#             string_form=str(i)
#             rotated_form=""
#             flag=True
#             for letter in string_form:
#                 if letter not in dictionary:
#                     #ignore this number
#                     flag=False
#                     break
#                 else:
#                     rotated_form+=dictionary[letter]
#             if (rotated_form!=string_form) and flag==True:
#                 count+=1
#         return count
