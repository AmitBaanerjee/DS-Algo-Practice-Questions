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
        Stack<Character> stack=new Stack<Character>();
        for(int i=0;i<S.length();i++){
            if (stack.size()==0 || stack.peek()!=S.charAt(i))
                stack.push(S.charAt(i));
            else{
                stack.pop();
            }
        }
        StringBuilder sb=new StringBuilder();
        while(!stack.isEmpty()){
            sb.insert(0,Character.toString(stack.pop()));
        }
        return sb.toString();
    }
}
