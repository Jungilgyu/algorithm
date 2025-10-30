import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

board = [[0] * (101) for _ in range(101)]

for x, y in paper:
    for i in range(x, x+10):
        for j in range(y, y+10):
            if board[i][j] == 0:
                board[i][j] = 1

cnt = 0
for row in range(101):
    for col in range(101):
        if board[row][col] == 1:
            temp = 0
            # 맨 위, 맨 오른쪽인 경우
            if row == 100 or col == 100:
                temp += 1

            for k in range(4):
                nxt_row, nxt_col = row + di[k], col + dj[k]
                if 0 <= nxt_row < 101 and 0 <= nxt_col < 101:
                    if board[nxt_row][nxt_col] == 0:
                        temp += 1
            cnt += temp

print(cnt)
