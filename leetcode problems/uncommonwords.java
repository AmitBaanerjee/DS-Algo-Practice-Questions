// 884. Uncommon Words from Two Sentences
//
// We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)
//
// A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
//
// Return a list of all uncommon words.
//
// You may return the list in any order.
//
// Example 1:
//
// Input: A = "this apple is sweet", B = "this apple is sour"
// Output: ["sweet","sour"]
// Example 2:
//
// Input: A = "apple apple", B = "banana"
// Output: ["banana"]

class Solution {
    public String[] uncommonFromSentences(String a, String b) {
        String c=a+" "+b;
		String[] aa=c.split(" ");
		Map<String,Integer> counts=new HashMap<String,Integer>();
		for (int i=0;i<aa.length;i++) {
			if(!counts.containsKey(aa[i])) {
				counts.put(aa[i], 1);
			}
			else {
				int count=counts.get(aa[i]);
				count++;
				counts.put(aa[i], count);
			}
		}
		List<String> answer=new ArrayList<String>();
		for(Map.Entry<String, Integer> hm:counts.entrySet()) {
			if (hm.getValue()==1) {
				answer.add(hm.getKey());
			}
		}
        String[] output=new String[answer.size()];
		for(int i=0;i<output.length;i++) {
			output[i]=answer.get(i);
		}
        return output;
    }
}
