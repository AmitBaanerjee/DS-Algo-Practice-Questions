import java.util.Arrays;
import java.util.Stack;

public class sortStack {

	public static void main(String[] args) {
		Stack<Integer> s=new Stack<Integer>();
		s.add(5);
		s.add(4);
		s.add(3);
		s.add(2);
		s.add(1);
		Stack<Integer> temp=new Stack<Integer>();
		while(!s.isEmpty()) {
			int item=s.pop();
			if(temp.isEmpty()) {
				temp.push(item);
			}
			else {
				while(!temp.isEmpty() && item>temp.peek()) {
					s.push(temp.pop());
				}
				temp.push(item);
			}
		}
		System.out.println(Arrays.toString(temp.toArray()));
	}

}
