#given an input list,
#find the maximum sum which is possible among all the elements of the list
#display the sum
#example:- input=[1,2,-5,7,8,-10]
#Output should be 18

input =[1,2,-1,3,4,10,10,-10,1]
tempsum=finalsum=0
for i in input:
    tempsum=max(tempsum,tempsum+i)
    finalsum=max(finalsum,tempsum)
print("max sum is ",finalsum )
