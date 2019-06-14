Dan is playing a video game in which his character competes in a hurdle race. Hurdles are of varying heights, and Dan has a maximum height he can jump. There is a magic potion he can take that will increase his maximum height by 1 unit for each dose. How many doses of the potion must he take to be able to jump all of the hurdles.

Given an array of hurdle heights height, and an initial maximum height Dan can jump, ,k determine the minimum number of doses Dan must take to be able to clear all the hurdles in the race.

For example, if height=[1,2,3,3,2] and Dan can jump 1 unit high naturally, he must take 3-1=2 doses of potion to be able to jump all of the hurdles.

Function Description

Complete the hurdleRace function in the editor below. It should return the minimum units of potion Dan needs to drink to jump all of the hurdles.

hurdleRace has the following parameter(s):

--> k: an integer denoting the height Dan can jump naturally
--> height: an array of integers denoting the heights of each hurdle

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {
    static int hurdleRace(int k, int[] height) {
        int temp=0;
        int maxdose=0;
        for(int i=0;i<height.length;i++){
            if(height[i]>k){
                temp=height[i]-k;
                if (temp>maxdose){
                    maxdose=temp;
                }
            }
        }
        return maxdose;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] nk = scanner.nextLine().split(" ");

        int n = Integer.parseInt(nk[0]);

        int k = Integer.parseInt(nk[1]);

        int[] height = new int[n];

        String[] heightItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int heightItem = Integer.parseInt(heightItems[i]);
            height[i] = heightItem;
        }

        int result = hurdleRace(k, height);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
