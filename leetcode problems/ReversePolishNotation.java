// 150. Evaluate Reverse Polish Notation
//
// Evaluate the value of an arithmetic expression in Reverse Polish Notation.
// Valid operators are +, -, *, /. Each operand may be an integer or another expression.
//
// Note:
//
// Division between two integers should truncate toward zero.
// The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
// Example 1:
//
// Input: ["2", "1", "+", "3", "*"]
// Output: 9
// Explanation: ((2 + 1) * 3) = 9
// Example 2:
//
// Input: ["4", "13", "5", "/", "+"]
// Output: 6
// Explanation: (4 + (13 / 5)) = 6
//
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;
public class ReversePolishNotation {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Stack<String> s=new Stack<String>();
		String[] tokens= {"2", "1", "+", "3", "*"};

		List<String> operators=new ArrayList<String>();
		operators.add("+");
		operators.add("-");
		operators.add("/");
		operators.add("*");

		for(int i=0;i<tokens.length;i++) {
			if (!operators.contains(tokens[i])) {
				s.push(tokens[i]);
			}
			else {
				int operand1=Integer.valueOf(s.pop());
				int operand2=Integer.valueOf(s.pop());
				String operator=tokens[i];
				if (operator=="+") {
					s.push(Integer.toString(operand1+operand2));
				}
				else if(operator=="-") {
					s.push(Integer.toString(operand1-operand2));
				}
				else if(operator=="*") {
					s.push(Integer.toString(operand1*operand2));
				}
				else {

						s.push(Integer.toString(operand2/operand1));

				}

			}
			System.out.println(s.peek());
		}
	}

}
