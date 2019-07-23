import java.util.Arrays;

public class selectionSort {
	public static void selectionSorting(int arr[]) {
		for(int i=0;i<arr.length-	1;i++) {
			int index=i;
			int temp;
			for(int j=i+1;j<arr.length;j++) {
				if(arr[j]<arr[index]) {
					index=j;
				}
			}

			if (index!=i) {
				temp=arr[index];
				arr[index]=arr[i];
				arr[i]=temp;

			}
		}
	}
	public static void main(String args[]) {
		System.out.println("selection sort program starting...");
		int arr[]= {99,98,97,1,90,100};
		System.out.println("before sorting array");
		System.out.println(Arrays.toString(arr));
		selectionSorting(arr);
		System.out.println("after selection sort on arr");
		System.out.println(Arrays.toString(arr));

	}
}
