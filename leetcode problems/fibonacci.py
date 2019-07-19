509. Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

from collections import defaultdict
class Solution:
    dic=defaultdict(int)
    def fib(self, number: int) -> int:
        if number==1:
            return 1
        if number==0:
            return 0
        if number- 1 not in self.dic:
            self.dic[number-1]=self.fib(number-1)
        if number -2 not in self.dic:
            self.dic[number-2]=self.fib(number -2)

        return self.dic[number-2] + self.dic[number-1]
