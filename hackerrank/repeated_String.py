# #REPEATED STRING
# Lilah has a string, s, of lowercase English letters that she repeated infinitely many times.
#
# Given an integer, n, find and print the number of letter a's in the first n letters of Lilah's infinite string.
#
# For example, if the string s="abcac" and n=10, the substring we consider is abcacabcac, the first 10 characters of her infinite string. There are  occurrences of a in the substring.
#
# Function Description
#
# Complete the repeatedString function in the editor below. It should return an integer representing the number of occurrences of a in the prefix of length n in the infinitely repeating string.
#
# repeatedString has the following parameter(s):
#
# s: a string to repeat
# n: the number of characters to consider
def repeatedString(s,n):
    count=0
    if len(s)==1 :
        if s=="a":
            count=n
    else:
        count=s.count("a")
        count=count*(n//len(s))
        count=count+ s[:n%len(s)].count("a")
    return count

print(repeatedString("aba",10))
print(repeatedString("a",1000000000000))
