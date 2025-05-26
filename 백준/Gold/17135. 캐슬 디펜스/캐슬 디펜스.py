import sys
from itertools import combinations
from collections import deque

import copy

n, m, d = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
dx = [0, -1, 0]
dy = [-1, 0, 1]
def get_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def pull(board):
    new_board = [[0] * m for _ in range(n)]
    for i in range(n - 1):
        new_board[i + 1] = board[i][:]
    return new_board

def attack(board, x, y):
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append((x - 1, y, 1))  # 바로 윗줄부터 시작
    while queue:
        x, y, dist = queue.popleft()
        if dist > d:
            break
        if 0 <= x < n and 0 <= y < m and not visited[x][y]:
            visited[x][y] = True
            if board[x][y] == 1:
                return (x, y)
            for dir in range(3):  # 왼쪽 → 위 → 오른쪽
                nx = x + dx[dir]
                ny = y + dy[dir]
                if 0 <= nx < n and 0 <= ny < m:
                    queue.append((nx, ny, dist + 1))
    return None

def sol(archer):
    board = copy.deepcopy(area)
    killed = 0
    while True:
        targets = set()
        for archer_x, archer_y in archer:
            target = attack(board, archer_x, archer_y)
            if target:
                targets.add(target)
        for x, y in targets:
            if board[x][y] == 1:
                board[x][y] = 0
                killed += 1
        board = pull(board)
        if sum(sum(row) for row in board) == 0:
            break
    return killed

lst = [i for i in range(m)]
cases = combinations(lst, 3)
ans = 0
for case in cases:
    archer = [[n, case[0]], [n, case[1]], [n, case[2]]]
    ans = max(ans, sol(archer))

print(ans)
