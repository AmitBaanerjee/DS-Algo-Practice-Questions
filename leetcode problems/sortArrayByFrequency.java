/*
1636. Sort Array by Increasing Frequency

Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

 

Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]class Solution {
    public int[] frequencySort(int[] nums) {
        Map<Integer, Integer> numsFrequency = new HashMap();
        int[] frequencySortedNums = new int[nums.length];
        int index = 0;
        for(int i : nums){
            if(numsFrequency.containsKey(i))
                numsFrequency.put(i, numsFrequency.get(i) + 1);
            else
                numsFrequency.put(i, 1);
        }
        
        List<Map.Entry<Integer, Integer>> sortNumsFrequency = 
                new ArrayList(numsFrequency.entrySet());
        Collections.sort(sortNumsFrequency, new Comparator<Map.Entry<Integer, Integer>>(){
            public int compare(Map.Entry<Integer, Integer> e1, Map.Entry<Integer, Integer> e2){
                //case when values are same
                if(e1.getValue() == e2.getValue()){
                    if(e1.getKey() > e2.getKey())
                        return -1;
                    else 
                        return 1;
                }
                //case when values are different
                else if (e1.getValue() < e2. getValue()){
                    return -1;
                }
                else
                    return 1;
            }
        });
        for(int i = 0; i < sortNumsFrequency.size(); i++){
            for(int j=0; j < sortNumsFrequency.get(i).getValue(); j++){
                frequencySortedNums[index++] = sortNumsFrequency.get(i).getKey();
            }
        }
        
        return frequencySortedNums;
    }
}
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
Example 2:

Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
Example 3:

Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]
*/

