//BUBBLE SORT IN JAVA

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    public static void bubbleSort(int[] array){
        int length=array.length;
        int numSwaps=0;
        int temp=0;
        for(int i=0;i<length;i++){
            for(int j=0;j<length-1;j++){
                if (array[j]>array[j+1]){
                    temp=array[j];
                    array[j]=array[j+1];
                    array[j+1]=temp;
                    numSwaps+=1;
                }
            }
        }
        System.out.println("Array is sorted in "+numSwaps+" swaps.");
        System.out.println("First Element: "+array[0]);
        System.out.println("Last Element: "+array[array.length-1]);
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] a = new int[n];
        for(int a_i=0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
        }
        bubbleSort(a);
    }
}
