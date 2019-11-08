200. Number of Islands
Medium

3456

127

Favorite

Share
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def neighbours(grid,r,c):
            pairs=[]
            if r>0:
                pairs.append([r-1,c])
            if r<len(grid)-1:
                pairs.append([r+1,c])
            if c>0:
                pairs.append([r,c-1])
            if c<len(grid[0])-1:
                pairs.append([r,c+1])
            return pairs

        def dfs(grid,r,c):
            grid[r][c]=0
            for i,j in neighbours(grid,r,c):
                if grid[i][j]=='1':
                    dfs(grid,i,j)

        count=0
        if grid==None:
            return None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    count+=1
                    dfs(grid,i,j)
        return count
