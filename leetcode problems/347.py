347. Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if nums==[]:
            return []
        if k==1 and len(nums)==1:
            return nums
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1

        counts=[]
        k_freq=[]
        heapq.heapify(counts)
        for i,j in dic.items():
            heapq.heappush(counts,(-j,i))
        for i in range(k):
            k_freq.append((heapq.heappop(counts))[1])
        return k_freq



        
