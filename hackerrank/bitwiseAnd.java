# Objective
# Welcome to the last day! Today, we're discussing bitwise operations. Check out the Tutorial tab for learning materials and an instructional video!
# Task
# Given set S={1,2,3,..N}. Find two integers, A and B (where A<B), from set S such that the value of A & B is the maximum possible and also less than a given integer, K. In this case, & represents the bitwise AND operator.
# Input Format
# The first line contains an integer,T, the number of test cases.
# Each of the T subsequent lines defines a test case as 2 space-separated integers, N and K, respectively.

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {



    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int t = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int tItr = 0; tItr < t; tItr++) {
            String[] nk = scanner.nextLine().split(" ");

            int n = Integer.parseInt(nk[0]);

            int k = Integer.parseInt(nk[1]);
            int result=0;
            for(int i=1;i<n;i++){
                for (int j=i+1;j<=n;j++){
                    int temp=i&j;
                    if (temp<k && temp>result){
                        result=temp;
                    }
                    if (temp==k-1){
                        break;
                    }
                }
            }
            System.out.println(result);

        }

        scanner.close();
    }
}
