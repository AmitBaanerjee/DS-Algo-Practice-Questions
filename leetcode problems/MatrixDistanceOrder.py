# 1030. Matrix Cells in Distance Order
#
# We are given a matrix with R rows and C columns has cells with integer coordinates (r, c), where 0 <= r < R and 0 <= c < C.
#
# Additionally, we are given a cell in that matrix with coordinates (r0, c0).
#
# Return the coordinates of all cells in the matrix, sorted by their distance from (r0, c0) from smallest distance to largest distance.  Here, the distance between two cells (r1, c1) and (r2, c2) is the Manhattan distance, |r1 - r2| + |c1 - c2|.  (You may return the answer in any order that satisfies this condition.)
#
# Example 1:
#
# Input: R = 1, C = 2, r0 = 0, c0 = 0
# Output: [[0,0],[0,1]]
# Explanation: The distances from (r0, c0) to other cells are: [0,1]
# Example 2:
#
# Input: R = 2, C = 2, r0 = 0, c0 = 1
# Output: [[0,1],[0,0],[1,1],[1,0]]
# Explanation: The distances from (r0, c0) to other cells are: [0,1,1,2]
# The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.
# Example 3:
#
# Input: R = 2, C = 3, r0 = 1, c0 = 2
# Output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
# Explanation: The distances from (r0, c0) to other cells are: [0,1,1,2,2,3]
# There are other answers that would also be accepted as correct, such as [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].

#ACCEPTED Solution
from heapq import heappush,heappop
class Solution:
    def allCellsDistOrder(self, r: int, c: int, r0: int, c0: int) -> List[List[int]]:
        tuples,result=[],[]
        for i in range(r):
            for j in range(c):
                mdiff=abs(i-r0)+abs(j-c0)
                heappush(tuples,(mdiff,[i,j]))
        while len(tuples)>0:
            mdis,coor=heappop(tuples)
            result.append(coor)
        return result
        
#---------------------------------------------------
#TIME EXCEEDED LOW LEVEL SOLUTION
class Solution:
    def sort_tuples(self,tuples):
    # doing bubble sort
        length=len(tuples)
        for i in range(0,length):
            for j in range(0,length-i-1):
                if tuples[j][0]>tuples[j+1][0]:
                    tuples[j],tuples[j+1]=tuples[j+1],tuples[j]
        return tuples
    def allCellsDistOrder(self, r: int, c: int, r0: int, c0: int) -> List[List[int]]:
        tuples,result=[],[]
        for i in range(r):
            for j in range(c):
                mdiff=abs(i-r0)+abs(j-c0)
                tuples.append((mdiff,i,j))
        sortedtuples=self.sort_tuples(tuples)
        for i in sortedtuples:
            result.append([i[1],i[2]])
        return result
