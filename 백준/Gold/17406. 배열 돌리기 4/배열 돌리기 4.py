import sys
from itertools import permutations
import copy
input = sys.stdin.readline

n, m, k = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
command = [list(map(int, input().split())) for _ in range(k)]

def rotate(r, c, s, board):
    # (r, c) 중앙값
    new = [[0] * m for _ in range(n)]
    new[r-1][c-1] = board[r-1][c-1] # 중앙값

    # 방향
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    d = 0

    i, j = r-s-1, c-s-1 # 시작값
    new[i][j] = board[i+1][j]
    while True:
        if i == r-1 and j == c-1:
            break

        ni, nj = i + di[d], j + dj[d]
        if r-s-1 <= ni < r+s and c-s-1 <= nj < c+s and new[ni][nj] == 0:
            new[ni][nj] = board[i][j]
            i, j = ni, nj
        else: # 방향전환
            d = (d+1) % 4
            ni, nj = i + di[d], j + dj[d]
            if d == 0: # 안으로 가는 경우
                if new[ni][nj] == 0:
                    new[ni][nj] = board[ni+1][nj]
            else: #그냥 방향전환만
                new[ni][nj] = board[i][j]
            i, j = ni, nj

    for x in range(n):
        for y in range(m):
            if new[x][y] == 0:
                new[x][y] = board[x][y]
    return new



cases = permutations(command)
ans = 5001
for case in cases:
    res = 5001
    temp = copy.deepcopy(area)
    for r, c, s in case:
        temp = rotate(r, c, s, temp)

    for row in temp:
        res = min(res, sum(row))

    ans = min(ans, res)
print(ans)



# ans = 5001
# for row in area:
#     ans = min(ans, sum(row))
# print(ans)