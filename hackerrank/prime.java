//Program to check if a number is a prime number or Not
//A number is said to be a prime number if it is greater than 1 and it is not divisible by any other number other than 1 and itself
//The time complexity of this problem is O(sqrt(n))


import java.io.*;
import java.util.*;

public class Solution {
    public static void checkPrime(int n){
        boolean flag=true;
            for(int i=2;i*i<=n;i++){
                if(n%i==0){
                    flag=false;
                }
            }
            if(n==1){
                flag=false;
            }
            if(n==2){
                flag=true;
            }

        System.out.println((flag==false)?"Not prime":"Prime");
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        for (int i=0;i<n;i++){
            int num=sc.nextInt();
            checkPrime(num);
        }
    }
}
