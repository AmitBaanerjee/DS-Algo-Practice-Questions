1122. Relative Sort Array

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

from collections import defaultdict
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        remaining_items=[]
        result=[]
        dic=defaultdict(int)
        for i in arr1:
            if i not in arr2:
                remaining_items.append(i)
            else:
                dic[i]+=1
        remaining_items=sorted(remaining_items)
        for i in arr2:
            while(dic[i]>0):
                result.append(i)
                dic[i]-=1
        for i in remaining_items:
            result.append(i)
        return result 
