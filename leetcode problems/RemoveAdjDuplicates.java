# 1047. Remove All Adjacent Duplicates In String
#
# Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
#
# We repeatedly make duplicate removals on S until we no longer can.
#
# Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.
#
#
#
# Example 1:
#
# Input: "abbaca"
# Output: "ca"
# Explanation:
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

class Solution {
    public String removeDuplicates(String S) {
        Stack<Character> st=new Stack<Character>();
        char[] c=S.toCharArray();
        st.push(c[0]);
        for (int i=1;i<c.length;i++){
            if (st.size()==0){
                st.push(c[i]);
            }
            else{
                char word1=st.peek();
                if(word1==c[i]){
                    char temp=st.pop();
                }
                else{
                    st.push(c[i]);
                }
            }
        }
        String output="";
        while(!st.isEmpty()){
            char x=st.pop();
            output=Character.toString(x)+output;
        }
        return output;
    }
}
