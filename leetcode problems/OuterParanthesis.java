
/*A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

Input: "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

 * 
 * 
 * 
 * */

import java.util.Iterator;
import java.util.Stack;
public class OuterParanthesis {

	public static void main(String[] args) {
		Stack<Character> s=new Stack<Character>();
		int i=0;
		char left='(';
		char right=')';
		String input="(()())(())(()(()))";
		int leftcounter=0;
		int rightcounter=0;
		String output="";
		while(i<input.length()) {
			
			if (input.charAt(i)==left) {
				s.push(input.charAt(i));
				leftcounter++;
			}
			else if(input.charAt(i)==right) {
				s.push(input.charAt(i));
				rightcounter++;
			}
			if(leftcounter==rightcounter) {
				s.remove(s.size()-1);
				s.remove(0);
				if(s.size()==0) {
					output=output+"";
				}
				else {
					Iterator<Character> iter=s.iterator();
					while(iter.hasNext()) {
						output=output+iter.next();
					}
					s.clear();
					
				}
			}
			i++;
		}
		System.out.println(output);
		
	}

}
