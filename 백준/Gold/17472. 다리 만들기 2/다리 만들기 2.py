import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

def bfs(i, j, num):
    q = deque([(i, j)])
    area[i][j] = num
    while q:
        x, y = q.popleft()
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and area[nx][ny] == 1:
                area[nx][ny] = num
                q.append((nx, ny))

num = 2
for i in range(n):
    for j in range(m):
        if area[i][j] == 1:
            bfs(i, j, num)
            num += 1
island_cnt = num - 2

edges = []
for i in range(n):
    for j in range(m):
        if area[i][j] > 1:
            start = area[i][j]
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                length = 0
                x, y = i, j
                while True:
                    x += dx; y += dy
                    if not (0 <= x < n and 0 <= y < m):
                        break
                    if area[x][y] == start:
                        break
                    if area[x][y] == 0:
                        length += 1
                        continue
                    if area[x][y] != start:
                        if length >= 2:
                            edges.append((length, start, area[x][y]))
                        break

parent = list(range(num))
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        parent[b] = a
        return True
    return False

edges.sort()
total, used = 0, 0
for cost, a, b in edges:
    if union(a, b):
        total += cost
        used += 1

if used == island_cnt-1:
    print(total)
else:
    print(-1)
