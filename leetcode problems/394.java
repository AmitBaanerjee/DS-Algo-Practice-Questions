394. Decode String
Medium

2011

110

Favorite

Share
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".


class Solution {
    public String decodeString(String ss) {
        char[] chArray=ss.toCharArray();
        Stack<Character> s=new Stack<Character>();
        int value=0;
        for(char c:chArray){
            if (c!=']'){
                s.push(c);
            }
            else{
                StringBuilder sb=new StringBuilder();
                while(s.size()!=0 && Character.isLetter(s.peek())){
                    sb.insert(0,s.pop());
                }
                String word=sb.toString();
                //ignore [ character
                s.pop();
                sb=new StringBuilder();
                while(s.size()!=0 && Character.isDigit(s.peek())){
                    sb.insert(0,s.pop());
                }
                value=Integer.valueOf(sb.toString());
                for(int i=0;i<value;i++){
                   for(char ch:word.toCharArray()){
                       s.push(ch);
                   }
                }
            }
        }
        StringBuilder answer=new StringBuilder();
        while(s.size()!=0){
            answer.insert(0,s.pop());
        }
        return answer.toString();
    }
}
