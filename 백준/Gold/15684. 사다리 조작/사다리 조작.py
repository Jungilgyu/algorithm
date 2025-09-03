import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, h = map(int, input().split())

# board[x][y] = 1 → y에서 y+1로 가는 가로선
# board[x][y] = -1 → y+1에서 y로 가는 가로선
board = [[0] * (n+1) for _ in range(h+1)]

for _ in range(m):
    a, b = map(int, input().split())
    board[a][b] = 1
    board[a][b+1] = -1

def check():
    for start in range(1, n+1):
        j = start
        for i in range(1, h+1):
            j += board[i][j]
        if j != start:
            return False
    return True

ans = 4

# 가능한 후보 좌표(grid)에 대해서만 탐색
grid = []
for i in range(1, h+1):
    for j in range(1, n):
        if board[i][j] == 0 and board[i][j+1] == 0:
            grid.append((i, j))

def dfs(cnt, idx):
    global ans
    if check():
        ans = min(ans, cnt)
        return
    if cnt == 3 or cnt >= ans:  # 최대 3개
        return

    for k in range(idx, len(grid)):
        x, y = grid[k]
        if board[x][y] == 0 and board[x][y+1] == 0:  # 놓을 수 있는지 확인
            board[x][y] = 1
            board[x][y+1] = -1
            dfs(cnt+1, k+1)   # 다음 후보부터 탐색
            board[x][y] = 0
            board[x][y+1] = 0

dfs(0, 0)
print(ans if ans < 4 else -1)