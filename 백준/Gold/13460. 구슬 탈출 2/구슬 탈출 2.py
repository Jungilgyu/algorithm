import sys
from collections import deque

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

di = [0, 0, -1, 1] # 왼 오 위 아
dj = [-1, 1, 0, 0]

def sol(redi, redj, bluei, bluej):
    q = deque()
    q.append([redi, redj, bluei, bluej, 0])
    visited = set()
    visited.add((redi, redj, bluei, bluej))

    while q:
        ri, rj, bi, bj, cnt = q.popleft()

        if cnt >= 10:
            continue

        for k in range(4): # 방향설정
            balls = [(ri, rj, 'R'), (bi, bj, 'B')]
            if k == 0:
                balls.sort(key=lambda x: x[1])
            elif k == 1:
                balls.sort(key=lambda x: x[1], reverse=True)
            elif k == 2:
                balls.sort(key=lambda x: x[0])
            else:
                balls.sort(key=lambda x: x[0], reverse=True)

            red_in = False
            blue_in = False
            cri, crj, cbi, cbj = -1, -1, -1, -1
            for i in range(2):
                ci, cj, color = balls[i]

                while True:
                    ni, nj = ci + di[k], cj + dj[k] # 다음 위치

                    if board[ni][nj] == '#': # 벽
                        break

                    elif board[ni][nj] == 'O': # 목적지면
                        if color == 'R':
                            red_in = True
                        else:
                            blue_in = True
                        break

                    elif (color == 'R' and ni == cbi and nj == cbj) or (color == 'B' and ni == cri and nj == crj):
                        break

                    ci, cj = ni, nj

                if color == "R":
                    if red_in:
                        cri, crj = -1, -1
                    else:
                        cri, crj = ci, cj
                else:
                    if blue_in:
                        cbi, cbj = -1, -1
                    else:
                        cbi, cbj = ci, cj

            if blue_in:
                continue

            if red_in and not blue_in:
                return cnt + 1

            if not blue_in and not red_in and (cri, crj, cbi, cbj) not in visited:
                q.append([cri, crj, cbi, cbj, cnt + 1])
                visited.add((cri, crj, cbi, cbj))

    return -1

# 시작 빨강, 파랑 위치 찾기
sri, srj = 0, 0
sbi, sbj = 0, 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            sri, srj = i, j
            board[i][j] = '.'
        elif board[i][j] == 'B':
            sbi, sbj = i, j
            board[i][j] = '.'

print(sol(sri, srj, sbi, sbj))
