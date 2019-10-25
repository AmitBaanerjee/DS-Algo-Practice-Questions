289. Game of Life
Medium

1190

219

Favorite

Share
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

public class Solution {
    public void gameOfLife(int[][] board) {
       // Store the adjacet value in the matrix
       // Make it negative if it was previously zero
        for(int i = 0; i < board.length; i++) {
            for(int j = 0; j < board[0].length; j++) {
                if(board[i][j] == 0) board[i][j] = -1 * getadj(i, j, board.length, board[0].length, board);
                else board[i][j] = getadj(i,j, board.length, board[0].length, board);
            }
        }

        // Now the board will contain the total number of 1's in adjacent cell
        // And the value will be negative if current board had 0 in this position
        // Now just manipulate again based on the conditions given in the matrix
        for(int i = 0; i < board.length; i++) {
            for(int j = 0; j < board[0].length; j++) {
                if(board[i][j] > 0 ) {
                    if(board[i][j] == 2 || board[i][j] == 3) board[i][j] = 1;
                    else board[i][j] = 0;
                } else {
                    if(board[i][j] == -3) board[i][j] = 1;
                    else board[i][j] = 0;
                }
            }
        }

    }
       public int getadj(int i, int j, int n, int m, int[][] mat) {
        int res = 0;
        if(i-1 >= 0 && (mat[i-1][j] > 0)) res++; // up
        if(j-1 >= 0 && mat[i][j-1] > 0) res++;   // left
        if(i+1 < n && mat[i+1][j] > 0) res++;    // down
        if(j+1 < m && mat[i][j+1] > 0) res++;    // right
        if(i -1 >= 0 && j-1 >= 0 && mat[i-1][j-1] > 0) res++; // dig - left - up
        if(i+1 < n && j+1 < m && mat[i+1][j+1] > 0) res++; // dig - right - down
        if(i+1 < n && j-1 >= 0 && mat[i+1][j-1] > 0) res++; // dig - left - down
        if(i-1 >= 0 && j+1 < m && mat[i-1][j+1] > 0) res++; // dig - right - up
        if(res == 0 && mat[i][j] == 1) return 1; // Make sure if it was positive we don't make it zero
        return res;
       }
}
