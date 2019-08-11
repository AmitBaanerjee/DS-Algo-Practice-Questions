784. Letter Case Permutation

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.

class Solution {
    public List<String> letterCasePermutation(String str) {
        if (str==null){
            return new LinkedList<>();
        }
        Queue<String> q= new LinkedList<String>();
        q.offer(str);
        for (int i=0;i<str.length();i++){
            if(Character.isDigit(str.charAt(i))){
                continue;
            }
            int size=q.size();
            for(int j=0;j<size;j++){
                String current=q.poll();
                char[] c=current.toCharArray();
                c[i]=Character.toLowerCase(c[i]);
                q.offer(String.valueOf(c));
                c[i]=Character.toUpperCase(c[i]);
                q.offer(String.valueOf(c));
             }
        }
        return new LinkedList<>(q);
    }
}
