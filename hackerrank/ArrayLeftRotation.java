/*
 A left rotation operation on an array shifts each of the array's elements 1 unit to the left. For example, if 2 left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2].
 Given an array a of n integers and a numberd, , perform d left rotations on the array. Return the updated array to be printed as a single line of space-separated integers. 

 Function Description:

 Complete the function rotLeft in the editor below. It should return the resulting array of integers.

 rotLeft has the following parameter(s):

 An array of integers .
 An integer , the number of rotations.*/
a=[41,73,89,7,10,1,59,58,84,77,77,97,58,1,86,58,26,10,86,51]
d=10
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the rotLeft function below.
    static int[] rotLeft(int[] a, int d) {

        int [] temp=new int[a.length];
        int len=a.length;
        for(int i=0;i<a.length;i++){
            if (i+d<len){
                temp[i]=a[i+d];
            }
            else{
                temp[i]=a[(i+d)-len];
            }
        }
        return temp;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] nd = scanner.nextLine().split(" ");

        int n = Integer.parseInt(nd[0]);

        int d = Integer.parseInt(nd[1]);

        int[] a = new int[n];

        String[] aItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int aItem = Integer.parseInt(aItems[i]);
            a[i] = aItem;
        }

        int[] result = rotLeft(a, d);

        for (int i = 0; i < result.length; i++) {
            bufferedWriter.write(String.valueOf(result[i]));

            if (i != result.length - 1) {
                bufferedWriter.write(" ");
            }
        }

        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
