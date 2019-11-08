994. Rotting Oranges

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.



Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.


from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((i,j,0))

        def neighbours(image,i,j):
            pairs=[]
            if i>0:
                pairs.append([i-1,j])
            if i<len(image)-1:
                pairs.append([i+1,j])
            if j>0:
                pairs.append([i,j-1])
            if j<len(image[0])-1:
                pairs.append([i,j+1])
            return pairs

        depth=0
        while q:
            row,col,depth=q.popleft()
            for rr,cc in neighbours(grid,row,col):
                if grid[rr][cc]==1:
                    grid[rr][cc]=2
                    q.append((rr,cc,depth+1))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return -1
        return depth
