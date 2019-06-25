package binarySearch;

import java.util.Scanner;
import java.util.concurrent.TimeUnit;

public class bs {
	public static int binarySearch(int[] array,int number,int low,int high) {
		if(low<=high) {
			int mid=low+(high-low)/2;

			if (number==array[mid]) {
				return mid;
			}
			if(number<array[mid]) {
				high=mid-1;
				return binarySearch(array,number,low,high);
			}
			
				low=mid+1;
				return binarySearch(array,number,low,high);
			
		
		}
		return -1;
		
		
	}
	public static void main(String args[]) throws InterruptedException {
		int n;
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the size of the array : ");
		n=sc.nextInt();
		int[] array=new int[n];
		for (int i=0;i<n;i++) {
			System.out.println("Enter a number to be added to the array --> ");
			array[i]=sc.nextInt();
		}
		System.out.println("enter the number to search ");
		int num=sc.nextInt();
		System.out.println("We will start the binary search program in 3 sec..");
		TimeUnit.SECONDS.sleep(3);
		int low=0;
		int high=array.length-1;
		int result=binarySearch(array,num,low,high);
		if (result!=-1) {
		System.out.println("number is present at index : "+result);
		}
		else {
			System.out.println("number was not found");
		}
		sc.close();
		
	}
}
