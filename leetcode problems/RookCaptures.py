999. Available Captures for Rook

On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.
https://leetcode.com/problems/available-captures-for-rook/

Example 1:

Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation:
In this example the rook is able to capture all the pawns.

Example 2:

Input: [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 0
Explanation:
Bishops are blocking the rook to capture any pawn.

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        #first find the position of row, column of rook in the board
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j]=="R":
                        r=i
                        c=j

            rook_row=""
            rook_column=""
            count=0
            #get rook row as a string excluding '.'
            for i in range(len(board[r])):
                if board[r][i]=='.':
                    continue
                else:
                    rook_row=rook_row+board[r][i]
            print(rook_row)

            #get rook column as a string excluding '.'
            for i in range(len(board)):
                if board[i][c]==".":
                    continue
                else:
                    rook_column=rook_column+board[i][c]
            print(rook_column)

            if 'pR' in rook_row: count += 1
            if 'Rp' in rook_row: count += 1
            if 'pR' in rook_column: count += 1
            if 'Rp' in rook_column: count += 1
            return count
