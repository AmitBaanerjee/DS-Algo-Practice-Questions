560. Subarray Sum Equals K

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2


class Solution {
    public int subarraySum(int[] nums, int k) {
        int[] totalSums= new int[nums.length+1];
        totalSums[0]=0;
        for(int i=1;i<=nums.length;i++){
            totalSums[i]=totalSums[i-1]+nums[i-1];
        }
        int counter=0;
        for (int i=0;i<totalSums.length;i++){
            for (int j=i+1;j<totalSums.length;j++){
                if (totalSums[j]-totalSums[i]==k)
                    counter++;
            }
        }
        return counter;
    }
}
