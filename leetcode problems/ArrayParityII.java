# 922. Sort Array By Parity II
#
# Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
#
# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
#
# You may return any answer array that satisfies this condition.
#
# Example 1:
#
# Input: [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
#
#PYTHON SOLUTION #
class Solution:
    def sortArrayByParityII(self, input: List[int]) -> List[int]:
        evenset,oddset=[],[]
        output=[0 for i in input]
        for i in input:
            if i%2==0:
                evenset.append(i)
            else:
                oddset.append(i)
        for i in range(len(output)):
            if i%2==0:
                output[i]=evenset[0]
                del evenset[0]
            else:
                output[i]=oddset[0]
                del oddset[0]
        return output

 #JAVA SOLUTION
class Solution {
    public int[] sortArrayByParityII(int[] A) {
        int [] odd= new int[A.length/2];
        int oddIndex=0;
        int [] even=new int[A.length/2];
        int evenIndex=0;
        for (int i=0;i<A.length;i++){
            if (A[i]%2==0){
                even[evenIndex]=A[i];
                evenIndex++;
            }
            else{
                odd[oddIndex]=A[i];
                oddIndex++;
            }
        }
        int[] result=new int[A.length];
        for(int i=0;i<result.length;i++){
            if(i%2==0){
                result[i]=even[evenIndex-1];
                evenIndex--;
            }
            else{
                result[i]=odd[oddIndex-1];
                oddIndex--;
            }
        }
        return result;
    }
}
            
