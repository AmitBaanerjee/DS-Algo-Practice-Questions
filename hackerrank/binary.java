/*Program to convert a base 10 number to a base 2 binary number.
  Display binary representation of the number in your console.
  Also count the number of consecutive ones which are occurring in the binary representation of the number.
  EXAMPLE:-
  Input-7
  Output:Binary representation is :- 111 
  	 Number of consecutive 1's are 3
  */

import java.util.Arrays;
import java.util.Scanner;

public class binary {
	public static void main(String args[]) {
		Scanner sc=new Scanner(System.in);
		System.out.println("enter a number to convert into binary:- ");
		int n=sc.nextInt();
		int temp1=0;
		int temp2=0;
		int i=0;
		int len=0;
		int[] binaryArray=new int[10];
		while (n!=0) {
			temp1=n%2;
			n=n/2;
			binaryArray[i]=temp1;
			i++;
		}
		len=(binaryArray.length);
		for (i=0;i<=len/2;i++) {
			temp2=binaryArray[i];
			binaryArray[i]=binaryArray[len-1-i];
			binaryArray[len-1-i]=temp2;
		}
		int counter=0;
		int result=0;
		for(i=0;i<len;i++) {
			if(binaryArray[i]==0) {
				counter=0;
			}
			else {
				counter++;
				result=Math.max(counter, result);
			}
		}
		System.out.println(Arrays.toString(binaryArray));
		System.out.println("maximum number of consecutive ones in the binary"
				+"representation is : "+result);
	}
}
