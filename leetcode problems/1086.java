1086. High Five

Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.

Example 1:

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation:
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.

class Solution {
    public int[][] highFive(int[][] values) {
        TreeMap<Integer,ArrayList<Integer>> tm=new TreeMap<Integer,ArrayList<Integer>>();
        for(int i=0;i<values.length;i++) {

				if(tm.containsKey(values[i][0])) {
					tm.get(values[i][0]).add(values[i][1]);
				}
				else {
					tm.put(values[i][0],new ArrayList<Integer>(Arrays.asList(values[i][1])));
				}
		}

        Set<Integer> s=tm.keySet();
		int [][] answer=new int[s.size()][2];
		for(Map.Entry<Integer, ArrayList<Integer>> me: tm.entrySet()) {
			int sum=0;
			int key=me.getKey();
			ArrayList<Integer> v=me.getValue();
			Collections.sort(v,Collections.reverseOrder());
			for(int i=0;i<5;i++) {
				sum=sum+v.get(i);
			}
			answer[key-1]= new int[]{key,sum/5};
		}
        return answer;
    }
}
