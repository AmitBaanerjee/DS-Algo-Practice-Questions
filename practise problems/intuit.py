"""
Given a board and an end position for the player, write a function to determine if it is possible to travel from every open cell on the board to the given end position.

board1 = [
    [ 0,  0,  0, 0, -1 ],
    [ 0, -1, -1, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
    [ 0, -1,  0, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
]

board2 = [
    [  0,  0,  0, 0, -1 ],
    [  0, -1, -1, 0,  0 ],
    [  0,  0,  0, 0,  0 ],
    [ -1, -1,  0, 0,  0 ],
    [  0, -1,  0, 0,  0 ],
    [  0, -1,  0, 0,  0 ],
]

board3 = [
    [ 0,  0,  0,  0,  0,  0, 0 ],
    [ 0, -1, -1, -1, -1, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1, -1, -1, -1, -1, 0 ],
    [ 0,  0,  0,  0,  0,  0, 0 ],
]

board4 = [
    [0,  0,  0,  0, 0],
    [0, -1, -1, -1, 0],
    [0, -1, -1, -1, 0],
    [0, -1, -1, -1, 0],
    [0,  0,  0,  0, 0],
]

end1 = (0, 0)
end2 = (5, 0)

Expected output:

isReachable(board1, end1) -> True
isReachable(board1, end2) -> True
isReachable(board2, end1) -> False
isReachable(board3, end1) -> False
isReachable(board4, end1) -> True

n: width of the input board
m: height of the input board


"""
board = [
  [0,  0,  0, -1, -1],
  [0,  0, -1,  0,  0],
  [0, -1,  0, -1,  0],
  [0,  0, -1,  0,  0],
  [0,  0,  0,  0,  0],
  [0,  0,  0,  0,  0],
  [0,  0,  0,  0,  0],
]

start1 = (3, 1)
start2 = (5, 3)
start3 = (5, 1)

start4 = (6, 0)
start5 = (6, 4)
start6 = (0, 0)
start7 = (2, 2)


board1 = [
    [ 0,  0,  0, 0, -1 ],
    [ 0, -1, -1, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
    [ 0, -1,  0, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
]

board2 = [
    [  0,  0,  0, 0, -1 ],
    [  0, -1, -1, 0,  0 ],
    [  0,  0,  0, 0,  0 ],
    [ -1, -1,  0, 0,  0 ],
    [  0, -1,  0, 0,  0 ],
    [  0, -1,  0, 0,  0 ],
]

board3 = [
    [ 0,  0,  0,  0,  0,  0, 0 ],
    [ 0, -1, -1, -1, -1, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1, -1, -1, -1, -1, 0 ],
    [ 0,  0,  0,  0,  0,  0, 0 ],
]

board4 = [
    [ 0,  0,  0,  0, 0 ],
    [ 0, -1, -1, -1, 0 ],
    [ 0, -1, -1, -1, 0 ],
    [ 0, -1, -1, -1, 0 ],
    [ 0,  0,  0,  0, 0 ],
]

end1 = (0, 0)
end2 = (5, 0)

def neighbours(board,row,col):
    coord=[]
    if r<maxr-1:
        if board[r+1][c]==0:
            cooord.append((r+1,c))

    #check left
    if c>0:
        if board[r][c-1]==0:
            coord.append((r,c-1))

    #check right
    if c<maxc-1:
        if board[r][c+1]==0:
            coord.append((r,c+1))

    #check bottom
    if r<maxr-1:
        if board[r+1][c]==0:
            coord.append((r+1,c))

def dfs(board,row,col,end):
    maxr=len(board)
    maxc=len(board[0])
    if neighbours(row,col)==[] or g_flag==False:
        return False
    for i,j in neighbours(board,row,col):
        if (i,j) in visited:
            return False
        else:
            if i==end[0] and j==end[1]:
                return True
            else:
                g_flag=dfs(board,i,j,end)



g_flag=True
visited=set()
for i in range(len(board)):
    for j in range(len(board[i])):
        flag=dfs(board,i,j,end)
        if flag==False:
            print(False)
            break
        else:
            pass








def check_board(board,coordinates):
    maxr=len(board)
    maxc=len(board[0])
    r=coordinates[0]
    c=coordinates[1]
    #check top
    answer=[]
    if r>0 :
        if board[r-1][c]==0:
            answer.append((r-1,c))
        else:
            pass
    #check bottom
    if r<maxr-1:
        if board[r+1][c]==0:
            answer.append((r+1,c))

    #check left
    if c>0:
        if board[r][c-1]==0:
            answer.append((r,c-1))

    #check right
    if c<maxc-1:
        if board[r][c+1]==0:
            answer.append((r,c+1))
    return answer

print(check_board(board,start7))
