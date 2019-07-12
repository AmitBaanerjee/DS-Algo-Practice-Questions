In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

Example 1:

Input: [1,2,3,3]
Output: 3
Example 2:

Input: [2,1,2,5,3,2]
Output: 2

class Solution:
    def repeatedNTimes(self, input: List[int]) -> int:
        dic={}
        for i in input:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1

        for i in dic:
            if dic[i]==len(input)//2:
                return i
            
