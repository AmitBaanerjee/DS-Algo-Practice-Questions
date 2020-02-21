# 461. Hamming Distance
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
#
# Note:
# 0 ≤ x, y < 231.
#
# Example:
#
# Input: x = 1, y = 4
#
# Output: 2
#
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
#
# The above arrows point to positions where the corresponding bits are different.
#

***PYTHON SOLUTION ***
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        integer_output=x^y
        binary_output=bin(x^y)
        count=0
        for i in range(2,len(binary_output)):
            if binary_output[i]=="1":
                count=count+1
        return count
    
*** JAVA SOLUTION ***

class Solution {
    
    public String appendZero(String input,int maxLength){
        StringBuilder sb=new StringBuilder();
        for(int i=0;i< maxLength-input.length();i++){
            sb.append("0");
        }
        sb.append(input);
        return sb.toString();
    }
    
    public int hammingDistance(int x, int y) {
        
        String xx=Integer.toBinaryString(x);
        String yy=Integer.toBinaryString(y);

        int maxLength=Math.max(xx.length(),yy.length());
        
        String finalX=appendZero(xx,maxLength);
        String finalY=appendZero(yy,maxLength);
        int counter=0;
        for(int i=0;i<maxLength;i++){
            if (finalX.charAt(i)!=finalY.charAt(i)){
                counter+=1;
            }
        }
        return counter;
    }
}
