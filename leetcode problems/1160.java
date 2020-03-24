1160. Find Words That Can Be Formed by Characters

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

class Solution {
    public int countCharacters(String[] words, String chars) {
        int answer=0;
        Map<Character,Integer> m= new HashMap<Character,Integer>();
        for(int i=0;i<chars.length();i++){
            if(m.containsKey(chars.charAt(i))){
                int val=m.get(chars.charAt(i));
                m.put(chars.charAt(i),val+1);
            }
            else{
                m.put(chars.charAt(i),1);
            }
        }
        for(String word:words){
            char[] c=word.toCharArray();
            boolean flag;

            Map<Character,Integer> temp=new HashMap<Character,Integer>();
            for(char letter:c){
            if(temp.containsKey(letter)){
                int val=temp.get(letter);
                temp.put(letter,val+1);
            }
            else{
                temp.put(letter,1);
            }  
            }
            flag=true;
            for(Map.Entry<Character,Integer> hm: temp.entrySet()){
                if(!m.containsKey(hm.getKey())){
                    flag=false;
                    break;
                }
                else{
                    if(m.get(hm.getKey())<hm.getValue()){
                        flag=false;
                        break;
                    }
                }
            }
            if (flag==true)
                answer+=word.length();
    }
         return answer; 
  }
}
