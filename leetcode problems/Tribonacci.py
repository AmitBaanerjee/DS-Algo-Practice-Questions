1137. N-th Tribonacci Number

The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537

from collections import defaultdict
class Solution:
    memo=defaultdict(int)

    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        if n-1 not in self.memo:
            self.memo[n-1]=self.tribonacci(n-1)
        if n-2 not in self.memo:
            self.memo[n-2]=self.tribonacci(n-2)
        if n-3 not in self.memo:
            self.memo[n-3]=self.tribonacci(n-3)

        return self.memo[n-1]+self.memo[n-2]+self.memo[n-3]
