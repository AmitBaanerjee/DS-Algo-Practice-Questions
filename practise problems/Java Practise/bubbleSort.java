//Performing bubble sort in java according to geekforgeeks algorithm explanation

import java.util.Arrays;

public class bubbleSort {
	public static void main(String args[]) {
		System.out.println("Practising the bubble sort program in java...");
		int[] array= {5,4,3,2,1};
		int arrayLength=array.length;
		int numberOfShuffles=0;
		for(int i=0;i<arrayLength;i++) {
			for(int j=0;j<arrayLength-i-1;j++) {
				if(array[j]>array[j+1]) {
					int temp=array[j];
					array[j]=array[j+1];
					array[j+1]=temp;
					numberOfShuffles++;
				}
			}
			System.out.println("The arrays looks like this after iteration: "+i + "-->"+ Arrays.toString(array));
		}
		System.out.println("Bubble sort was performed with "+numberOfShuffles+ " number of shuffles");
	}
}
