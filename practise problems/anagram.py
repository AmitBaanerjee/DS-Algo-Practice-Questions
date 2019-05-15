# anagram practise problem 1
# example-->
# cat=act
# real fun= funeral
#approach === create a dictionary and check inside that

#SOLUTION
import sys
string1="real fun"
string2="funeral    "
dictionary={}
string1=string1.strip().split()
string2=string2.strip().split()
string1=''.join(string1)
string2=''.join(string2)
if len(string1)!=len(string2):
    print("Strings are not anagram of each other")
    sys.exit()
else:
    for i in string1:
        if i not in dictionary:
            dictionary[i]=1
        else:
            dictionary[i]+=1
    for j in string2:
        if j in dictionary:
            dictionary[j]-=1
        else:
            dictionary[j]=1
    for key in dictionary:
        if dictionary[key]!=0:
            print("Strings not anagram because of: '", key,"'")
            sys.exit()
    print("strings are anagram of each other")
