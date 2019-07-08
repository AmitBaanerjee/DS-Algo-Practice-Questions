##SINGLE NUMBER

Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:

Your algorithm should have a linear runtime complexity.

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

class Solution {
    public int singleNumber(int[] nums) {
        int resultKey=0;
		Map<Integer,Integer> m=new HashMap<Integer,Integer>();
		for(int i:nums) {
			if(m.containsKey(i)) {
				int val=m.get(i);
					val++;
					m.put(i, val);
			}
			else {
				m.put(i, 1);
			}
		}
		for(Map.Entry<Integer, Integer> entry:m.entrySet()) {
			if(entry.getValue()==1) {
				resultKey=entry.getKey();
			}
		}
		return resultKey;
    }
}
