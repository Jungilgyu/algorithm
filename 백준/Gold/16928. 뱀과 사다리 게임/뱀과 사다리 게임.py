import sys
from collections import deque

n, m = map(int, input().split())
move = dict()
for _ in range(n+m):
    s, e = map(int, input().split())
    move[s] = e

def bfs():
    visited = [False] * 101
    q = deque()
    q.append((1, 0))
    visited[1] = True

    while q:
        cur, cnt = q.popleft()
        if cur == 100:
            return cnt

        for dice in range(1, 7):
            next = cur + dice
            if next > 100:
                continue

            if next in move:
                next = move[next]

            if not visited[next]:
                visited[next] = True
                q.append((next, cnt + 1))
    return -1

print(bfs())