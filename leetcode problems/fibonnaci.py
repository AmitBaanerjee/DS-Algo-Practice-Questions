#FIBONNACI SERIES
#Solution 1:Standard recursive approach
#Solution 2:Recursion with memoization(96% more effective)
from collections import defaultdict
class Solution:
    memoization=defaultdict(int)
    def fib(self, N):
        #standard solution
        # if N==0:
        #     return 0
        # if N==1:
        #     return 1
        # else:
        #     return self.fib(N-1)+self.fib(N-2)
        ##using memoization
        if N==0:
            return 0
        if N==1:
            return 1
        if N-1 not in self.memoization:
            self.memoization[N-1]=self.fib(N-1)
        if N-2 not in self.memoization:
            self.memoization[N-2]=self.fib(N-2)
        return self.memoization[N-1]+self.memoization[N-2]
