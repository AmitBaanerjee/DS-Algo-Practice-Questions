64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.


class Solution {
    //brute force time exceeded
    // public static int dfs(int row, int col, int [][] grid){
    //     if (row==grid.length || col==grid[0].length)
    //         return Integer.MAX_VALUE;
    //     if (row==grid.length-1 && col==grid[0].length-1)
    //         return grid[row][col];
    //     return grid[row][col]+Math.min(dfs(row+1,col,grid),dfs(row,col+1,grid));
    // }
    // public int minPathSum(int[][] grid) {
    //     return dfs(0,0,grid);
    // }
    public int minPathSum(int [][] grid){
        int [][]store=new int [grid.length][grid[0].length];
        for(int i=grid.length-1;i>=0;i--){
            for (int j=grid[0].length-1;j>=0;j--){
                if (j==grid[0].length-1 && i==grid.length-1)
                    store[i][j]=grid[i][j];
                else if(i==grid.length-1 && j!=grid[0].length-1)
                    store[i][j]=grid[i][j]+store[i][j+1];
                else if(i!=grid.length-1 && j==grid[0].length-1)
                    store[i][j]=grid[i][j]+store[i+1][j];
                else if(i!=grid.length-1 && j!=grid[0].length-1)
                    store[i][j]=grid[i][j]+ Math.min(store[i+1][j],store[i][j+1]);
            }
        }
        return store[0][0];
    }
}
