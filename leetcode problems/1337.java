1337. The K Weakest Rows in a Matrix

Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians), return the indexes of the k weakest rows in the matrix ordered from the weakest to the strongest.

A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers in row j, or they have the same number of soldiers but i is less than j. Soldiers are always stand in the frontier of a row, that is, always ones may appear first and then zeros.

Example 1:

Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers for each row is: 
row 0 -> 2 
row 1 -> 4 
row 2 -> 1 
row 3 -> 2 
row 4 -> 5 
Rows ordered from the weakest to the strongest are [2,0,3,1,4]
Example 2:

Input: mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
Output: [0,2]
Explanation: 
The number of soldiers for each row is: 
row 0 -> 1 
row 1 -> 4 
row 2 -> 1 
row 3 -> 1 
Rows ordered from the weakest to the strongest are [0,2,3,1]


class Solution {
    public int[] kWeakestRows(int[][] mat, int k) {
        TreeMap<Integer,ArrayList<Integer>> t=new TreeMap<Integer,ArrayList<Integer>>();
        int counter;
        int rowNum=0;
        for(int i=0;i<mat.length;i++){
            counter=0;
            rowNum=i;
            for (int j=0;j<mat[i].length;j++){
                if (mat[i][j]==1)
                    counter+=1;
            }
            if(t.get(counter)==null){
                t.put(counter,new ArrayList<Integer>(Arrays.asList(rowNum)));
            }
            else{
                ArrayList<Integer> temp=t.get(counter);
                temp.add(rowNum);
                t.put(counter,temp);
            }
        }
        int[] result=new int[k];
        int index=0;
        for(Map.Entry<Integer,ArrayList<Integer>> m:t.entrySet()){
            ArrayList<Integer> a=m.getValue();
            for(int i=0;i<a.size();i++){
                result[index]=a.get(i);
                index++;
                if(index==k)
                    break;
            }
            if(index==k)
                break;
        }

        
        return result;
    }
}
