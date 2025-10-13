import sys
from collections import deque
from itertools import permutations, product
input = sys.stdin.readline

board = []
for _ in range(5):
    f = []
    for _ in range(5):
        l = list(map(int, input().split()))
        f.append(l)
    board.append(f)

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 1. 돌리기
def rotate(area):
    new = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            new[j][4-i] = area[i][j]
    return new

ans = float('inf')
# 2. 층별 모든 판의 경우
total = [[] for _ in range(5)]
for i in range(5):
    current = board[i]
    for _ in range(4):
        total[i].append(current)
        current = rotate(current)

def bfs(maze):
    global ans
    if maze[0][0][0] == 0 or maze[4][4][4] == 0:
        return
    visited = [[[False] * 5 for _ in range(5)] for _ in range(5)]
    q = deque()
    q.append([0, 0, 0, 0])
    visited[0][0][0] = True

    while q:
        floor, i, j, cnt = q.popleft()
        if cnt >= ans:
            continue

        if floor == 4 and i == 4 and j == 4:
            ans = min(ans, cnt)
            if ans == 12:
                print(12)
                sys.exit(0)
            return

        # 층이동 하는 경우
        for next_floor in (floor-1, floor+1):
            if 0 <= next_floor < 5 and not visited[next_floor][i][j] and maze[next_floor][i][j] == 1:
                q.append((next_floor, i, j, cnt + 1))
                visited[next_floor][i][j] = True

        # 판 내에서만 이동
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < 5 and 0 <= nj < 5 and not visited[floor][ni][nj] and maze[floor][ni][nj] == 1:
                q.append((floor, ni, nj, cnt+1))
                visited[floor][ni][nj] = True

for order in permutations(range(5)):
    for rotation in product(range(4), repeat=5):
        maze = [total[order[i]][rotation[i]] for i in range(5)]
        bfs(maze)

if ans == float('inf'):
    print(-1)
else:
    print(ans)


