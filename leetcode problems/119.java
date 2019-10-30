119. Pascal's Triangle II

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?

class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<List<Integer>> triangle=new ArrayList<List<Integer>>();
        triangle.add(new ArrayList<>(Arrays.asList(1)));
        for(int i=1;i<=rowIndex;i++){
            List<Integer>prev=triangle.get(i-1);
            List<Integer> row=new ArrayList<Integer>();
            row.add(1);
            for(int j=1;j<i;j++){
                row.add(prev.get(j-1)+prev.get(j));
            }
            row.add(1);
            triangle.add(row);
        }
        return triangle.get(rowIndex);
    }
}
