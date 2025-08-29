import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def find_block(i, j, visited):
    q = deque()
    q.append([i, j])
    temp = area[i][j]
    visited[i][j] = True
    res = [[i, j]]
    while q:
        ci, cj = q.popleft()
        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj] and (area[ni][nj] == temp or area[ni][nj] == 0):
                res.append([ni, nj])
                visited[ni][nj] = True
                q.append([ni, nj])

    if len(res) < 2:
        return False, False
    else:
        normal = []
        rainbow = []

        core_i, core_j = 21, 21
        for i, j in res:
            if area[i][j] == 0:
                rainbow.append([i, j])
            else:
                normal.append([i, j])
        normal.sort(key=lambda x: (x[0], x[1]))
        rainbow_cnt = len(rainbow)
        rres = normal + rainbow
        return rres, rainbow_cnt

# 중력
def gravity(board):
    new_board = [[-2] * n for _ in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(n):
            if board[i][j] == -1: #
                new_board[i][j] = -1
            elif board[i][j] != -2:
                ci = i
                while True:
                    ni = ci + 1
                    if ni >= n:
                        break
                    if new_board[ni][j] == -2:
                        ci = ni
                    else:
                        break
                new_board[ci][j] = board[i][j]
    return new_board

# 90도 회전
def turn(board):
    new_board = [[-2] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_board[i][j] = board[j][n-i-1]
    return new_board

# 시뮬
ans = 0
while True:
    # 숫자마다 visited를 따로 해야할듯
    max_group = []
    max_rainbow = 0
    end = 0
    for num in range(1, m+1):
        visited = [[False] * n for _ in range(n)]
        can_find = False
        for i in range(n):
            for j in range(n):
                if area[i][j] == num and not visited[i][j]:
                    result, rcnt = find_block(i, j, visited)
                    if result != False: # 해당 숫자에서 그룹 못찾음
                        can_find = True
                        # 가장 큰 그룹 갱신
                        if len(result) > len(max_group):
                            max_group = result
                            max_rainbow = rcnt
                        elif len(result) == len(max_group):
                            # 무지개 블록 비교
                            if rcnt > max_rainbow:
                                max_group = result
                                max_rainbow = rcnt
                            elif rcnt == max_rainbow:
                                # 이제 여기서 대표값 비교
                                result_core = result[0]
                                max_group_core = max_group[0]
                                if tuple(result_core) > tuple(max_group_core):
                                    max_group = result
                                    max_rainbow = rcnt
        if can_find == False:
            end += 1
    if end == m:
        break # 루프종료

    score = len(max_group)
    ans += score ** 2 # 점수 증가
    for i, j in max_group:
        area[i][j] = -2

    area = gravity(area)
    area = turn(area)
    area = gravity(area)

print(ans)
