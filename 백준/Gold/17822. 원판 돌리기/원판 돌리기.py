import sys
from collections import deque
input = sys.stdin.readline

n, m, t = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
command = [list(map(int, input().split())) for _ in range(t)]

# 돌리기 함수
def spin(target, direction, cnt, b):
    new_board = []
    for i in range(len(b)):
        q = deque(b[i])
        if (i+1) % target == 0:
            for _ in range(cnt):
                if direction == 0:
                    q.rotate(1)
                else:
                    q.rotate(-1)
        new_board.append(q)

    return new_board

# 인접한거 지우기 함수
def remove(b):
    target = []
    visited = [[False] * m for _ in range(n)]
    is_adj = False # 인접한게 있었는지 확인
    for i in range(n):
        for j in range(m):
            flag = False # 인접한걸 찾았는지 확인 => i,j 넣을지 말지 판단
            temp = b[i][j]
            if temp == 0:
                continue
                
            for k in (-1, 1):
                # 다른 판 (상하)
                ni = i+k
                if 0 <= ni < n and b[ni][j] == temp and not visited[ni][j]:
                    target.append([ni, j])
                    visited[ni][j] = True
                    flag = True
                    is_adj = True

                # 같은 판 (좌우)
                nj = ((j+k) + m) % m
                if b[i][nj] == temp and not visited[i][nj]:
                    target.append([i, nj])
                    visited[i][nj] = True
                    flag = True
                    is_adj = True
            # 인접한걸 찾았으면
            if flag:
                target.append([i, j])
    # x표시
    for x, y in target:
        b[x][y] = 0

    return is_adj

# 인접한 거 없을 떄 값 변경하는 함수
def change_v(b):
    total = 0
    cnt = 0
    for i in range(n):
        for j in range(m):
            if b[i][j] != 0:
                total += b[i][j]
                cnt += 1
    if cnt == 0:
        return

    avg = total / cnt

    for i in range(n):
        for j in range(m):
            if b[i][j] != 0:
                if b[i][j] > avg:
                    b[i][j] -= 1
                elif b[i][j] < avg:
                    b[i][j] += 1

# 원판의 모든숫자 더하기 함수
def cnt_sum(b):
    res = 0
    for i in range(n):
        for j in range(m):
            res += b[i][j]

    return res

for x, d, k in command:
    board = spin(x, d, k, board)
    do_next = remove(board)
    if not do_next:
        change_v(board)

print(cnt_sum(board))
