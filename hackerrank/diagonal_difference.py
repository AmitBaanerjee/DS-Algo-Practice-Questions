#DIAGONAL DIFFERENCE
#Given a square matrix, calculate the absolute difference between the sums of its diagonals.
For example, the square matrix  is shown below:

# 1 2 3
# 4 5 6
# 9 8 9
# The left-to-right diagonal = 1+5+9=15. The right to left diagonal =3+5+9=17 . Their absolute difference is 2.

def diagonalDifference(arr):
    left_diagonal=0
    right_diagonal=0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i==j:
                left_diagonal+=arr[i][j]
                right_diagonal+=arr[i][(len(arr[0])-1)-j]
    return abs(left_diagonal-right_diagonal)

    
