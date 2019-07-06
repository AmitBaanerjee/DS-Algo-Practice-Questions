# # problem 2
# # Find & print the total number of distinct pairs equal to input parameter "Sum"
# Example:- input=[1,3,2,2] sum=4
#             output= 1,3
#                     2,2
def sumpairs(inputlist,sum):
    dictionary={}
    outputlist=set()
    for i in inputlist:
        if i in dictionary:
            outputlist.add(tuple((dictionary[i],i)))
        else:
            dictionary[sum-i]=i
    if len(outputlist)== 0 :
        return "No elements in inputlist"
    return outputlist
test=sumpairs([1,3,2,2],4)
print(test)
