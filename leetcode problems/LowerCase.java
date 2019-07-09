Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"

class Solution {
    public String toLowerCase(String str) {
        char[] characters=str.toCharArray();
        StringBuilder sb=new StringBuilder();
        for(int i=0;i<characters.length;i++){
            if(characters[i]>='A' && characters[i]<='Z'){
                characters[i]=(char)(characters[i]+('a'-'A'));
            }
            sb.append(characters[i]);
        }
        return sb.toString();
    }
}
