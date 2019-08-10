// 190. Reverse Bits
//
// Reverse bits of a given 32 bits unsigned integer.
//
// Example 1:
//
// Input: 00000010100101000001111010011100
// Output: 00111001011110000010100101000000
// Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
// Example 2:
//
// Input: 11111111111111111111111111111101
// Output: 10111111111111111111111111111111
// Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10101111110010110010011101101001.

public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        String bin=Integer.toBinaryString(n);
        int remainingLength=32-bin.length();
        String[] totalbits=new String[32];
        for(int i=0;i<remainingLength;i++){
            totalbits[i]="0";
        }
        char[] bits=bin.toCharArray();
        for(int i=remainingLength;i<32;i++){
            totalbits[i]=Character.toString(bits[i-remainingLength]);
        }
        String output="";
        for(int i=31;i>=0;i--){
            output=output+totalbits[i];
        }
        return Integer.parseUnsignedInt(output,2);
    }
}
