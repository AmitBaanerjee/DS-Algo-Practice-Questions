// HackerLand Enterprise is adopting a new viral advertising strategy. When they launch a new product, they advertise it to exactly 5 people on social media.
//
// On the first day, half of those 5 people (i.e.,5/2=2 ) like the advertisement and each shares it with 3 of their friends. At the beginning of the second day,5/2*3=6  people receive the advertisement.
//
// Each day, recipients/2 of the recipients like the advertisement and will share it with 3 friends on the following day. Assuming nobody receives the advertisement twice, determine how many people have liked the ad by the end of a given day, beginning with launch day as day 1.
//
// For example, assume you want to know how many have liked the ad by the end of the 5th day.
//
// Day Shared Liked Cumulative
// 1      5     2       2
// 2      6     3       5
// 3      9     4       9
// 4     12     6      15
// 5     18     9      24
// The cumulative number of likes is 24.
//
// Function Description
//
// Complete the viralAdvertising function in the editor below. It should return the cumulative number of people who have liked the ad at a given time.
//
// viralAdvertising has the following parameter(s):
//
// n: the integer number of days
// Input Format
//
// A single integer, n, denoting a number of days.

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the viralAdvertising function below.
    static int viralAdvertising(int n) {
        int shared=0;
        int cumulative=0;
        int people=5;
        int output=0;
        for(int i=1;i<=n;i++) {
            shared=people/2;
            cumulative=people-shared;
            output=output+shared;
            people=shared*3;

        }
        return output;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int result = viralAdvertising(n);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
