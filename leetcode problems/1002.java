1002. Find Common Characters

Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]

-----------------------------------*********------------------------------------
class Solution {
    public List<String> commonChars(String[] A) {
        if(A.length==0)
            return new ArrayList<String>();
        
        Map<Character,Integer> main=new HashMap<Character,Integer>();
        
        String first=A[0];
        for(int i=0;i<first.length();i++){
            if(main.containsKey(first.charAt(i))){
                int val=main.get(first.charAt(i));
                main.put(first.charAt(i),val+1);
            }
            else
                main.put(first.charAt(i),1);
        }

        for(int i=1;i<A.length;i++){

            char[] word=A[i].toCharArray();
            
            Map<Character,Integer> local=new HashMap<Character,Integer>();
            for(int j=0;j<word.length;j++){
                if(local.containsKey(word[j])){
                    int val=local.get(word[j]);
                    local.put(word[j],val+1);
                }
                else
                    local.put(word[j],1);
            }
            
                      
            for(Map.Entry<Character,Integer> m:local.entrySet()){
                if(!main.containsKey(m.getKey()))
                    local.put(m.getKey(),-1);
                else
                    local.put(m.getKey(),Math.min(local.get(m.getKey()),main.get(m.getKey())));
            }
            Iterator iter=local.keySet().iterator();
            while(iter.hasNext()){
                if(local.get(iter.next())==-1)
                    iter.remove();
            }
            
            main.clear();
            main.putAll(local);
        }
        List<String> answer=new ArrayList<String>();
        for(Map.Entry<Character,Integer>m:main.entrySet()){
            for(int i=0;i<m.getValue();i++){
                answer.add(Character.toString(m.getKey()));
            }
        }
        return answer;
    }
}
