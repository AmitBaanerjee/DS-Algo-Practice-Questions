# Objective 
# Today, we're working with regular expressions. Check out the Tutorial tab for learning materials and an instructional video!
# Task
# Consider a database table, Emails, which has the attributes First Name and Email ID. Given N rows of data simulating the Emails table, print an alphabetically-ordered list of people whose email address ends in @gmail.com.
# Input Format
# The first line contains an integer, N, total number of rows in the table.
# Each of the N subsequent lines contains 2 space-separated strings denoting a person's first name and email ID, respectively.
# EXample:-
# Sample Input--->
# 6
# riya riya@gmail.com
# julia julia@julia.me
# julia sjulia@gmail.com
# julia julia@gmail.com
# samantha samantha@gmail.com
# tanya tanya@gmail.com
#
# Sample Output--->
# julia
# julia
# riya
# samantha
# tanya

if __name__ == '__main__':
    N = int(input())
    nameList=[]
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if "gmail" in emailID:
            namepart=emailID.split('@')[0]
            domaincomp=emailID.split('@')[1]
            typecomp=domaincomp.split('.')[1]
            domain=domaincomp.split('.')[0]
            if domain=="gmail":
                nameList.append(firstName)
    nameList.sort()
    for i in nameList:
        print(i)
