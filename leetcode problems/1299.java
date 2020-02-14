/*1299. Replace Elements with Greatest Element on Right Side

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
*/

class Solution {
    public int[] replaceElements(int[] arr) {
        int[] greatest=new int[arr.length];
        greatest[greatest.length-1]=-1;
        for(int i=arr.length-2;i>=0;i--){
            greatest[i]=Math.max(greatest[i+1],arr[i+1]);
        }
        return greatest;
    }
}
