# 867. Transpose Matrix
#
# Given a matrix A, return the transpose of A.
#
# The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.
#
# Example 1:
#
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# Example 2:
#
# Input: [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]

#123    147
#456    258
#789    369

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        trans=[[0 for i in range(len(matrix))]for j in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                trans[j][i]=matrix[i][j]
        return trans
