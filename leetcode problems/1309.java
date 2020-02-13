/*
1309. Decrypt String from Alphabet to Integer Mapping

Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.
Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
Example 2:

Input: s = "1326#"
Output: "acz"
Example 3:

Input: s = "25#"
Output: "y"
Example 4:

Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
Output: "abcdefghijklmnopqrstuvwxyz"
*/

class Solution {
    public String freqAlphabets(String s) {
        List<String> numbers= new ArrayList<String>();
        char[] letters=s.toCharArray();
        int i=letters.length-1;
        String entry;
        while(i>=0){
            if (letters[i]!='#'){
                numbers.add(Character.toString(letters[i]));
                i=i-1;
            }
            else{
                entry=new StringBuilder().append(letters[i-2]).append(letters[i-1]).toString();
                numbers.add(entry);
                i=i-3;
            }
        }
        String answer="";
        for(String x:numbers){
            int number=Integer.parseInt(x);
            number=number + 96;
            char ch;
            ch=(char) number;
            answer=Character.toString(ch)+answer;
            
        }
        return answer;
    }
}
