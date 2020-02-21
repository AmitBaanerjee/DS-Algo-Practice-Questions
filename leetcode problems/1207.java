1207. Unique Number of Occurrences

Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer,Integer> hm=new HashMap<Integer,Integer>();
        for(int i:arr){
            if (hm.containsKey(i)){
                hm.put(i,hm.get(i)+1);
            }
            else{
                hm.put(i,1);
            }
        }
        
        List<Integer> l=new ArrayList<Integer>();
        Boolean flag=true;
        for(Map.Entry<Integer,Integer> m:hm.entrySet()){
            if(! l.contains(m.getValue())){
                l.add(m.getValue());
            }
            else{
                flag=false;
                break;
            }
        }
        return flag;
        
    }
}
