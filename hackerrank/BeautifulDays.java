// Lily likes to play games with integers. She has created a new game where she determines the difference between a number and its reverse. For instance, given the number 12, its reverse is 21. Their difference is 9. The number 120 reversed is 21, and their difference is 99.
//
// She decides to apply her game to decision making. She will look at a numbered range of days and will only go to a movie on a beautiful day.
//
// Given a range of numbered days,[i..j]  and a number k, determine the number of days in the range that are beautiful. Beautiful numbers are defined as numbers where |i-reverse(i)| is evenly divisible by k. If a day's value is a beautiful number, it is a beautiful day. Print the number of beautiful days in the range.
//
// Function Description
//
// Complete the beautifulDays function in the editor below. It must return the number of beautiful days in the range.
//
// beautifulDays has the following parameter(s):
//
// i: the starting day number
// j: the ending day number
// k: the divisor
// Input Format
//
// A single line of three space-separated integers describing the respective values of i, j, and k.

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    static int reverseNumber(int input){
        int temp=input;
        String result="";
        while(temp!=0) {
            int temp1=temp%10;
            temp=temp/10;
            result=result+Integer.toString(temp1);
        }
        return Integer.parseInt(result);
    }
    static int beautifulDays(int i, int j, int k) {
        int reversed=0;
        int beautifulDays=0;
        for(;i<=j;i++){
            reversed=reverseNumber(i);
            if (Math.abs(reversed-i)%k==0){
                beautifulDays=beautifulDays+1;
            }
        }
        return beautifulDays;

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] ijk = scanner.nextLine().split(" ");

        int i = Integer.parseInt(ijk[0]);

        int j = Integer.parseInt(ijk[1]);

        int k = Integer.parseInt(ijk[2]);

        int result = beautifulDays(i, j, k);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
