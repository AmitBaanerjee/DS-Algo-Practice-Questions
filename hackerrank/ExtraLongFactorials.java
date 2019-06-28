# Extra long extraLongFactorials
# Find the factorial for large numbers greater than 20 which cant be stored in int data type.
# Big integer class has been used for such computations.

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    static void extraLongFactorials(int n) {
        BigInteger b= new BigInteger("1");
        for(int i=1;i<=n;i++){
            b=b.multiply(BigInteger.valueOf(i));
        }
        System.out.println(b);
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        extraLongFactorials(n);

        scanner.close();
    }
}
