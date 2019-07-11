//LEETCODE PROBLEM
/*
 * International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cba" can be written as "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".

 * 
 */

import java.util.Map;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.ArrayList;
public class MorseCodes {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String[] words= {"gin","zen","gig","msg"};
		String[] morseCodes= {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
		Map<Character,String> dictionary=new HashMap<Character,String>();
		List<String> transformations=new ArrayList<String>();
		int counter=0;
		for(int i=0;i<=25;i++) {
			dictionary.put(((char)(97+i)),morseCodes[i]);
		}
		for(int i=0;i<words.length;i++) {
			String transformation="";
			for(char c:words[i].toCharArray()) {
				transformation=transformation+dictionary.get(c);
			}
			transformations.add(transformation);
		}
		System.out.println(transformations.stream().distinct().count());
	}

}
