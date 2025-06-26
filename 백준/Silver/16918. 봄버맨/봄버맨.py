import sys

R, C, N = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

def explode(board):
    new_board = [['O'] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                new_board[i][j] = '.'
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < R and 0 <= nj < C:
                        new_board[ni][nj] = '.'
    return new_board

if N == 1:
    result = board
elif N % 2 == 0:
    result = [['O'] * C for _ in range(R)]
elif N % 4 == 3:
    result = explode(board)
else:  # N % 4 == 1
    result = explode(explode(board))

for row in result:
    print("".join(row))
