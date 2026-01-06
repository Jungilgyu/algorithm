import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

# 최대 친구의 친구까지

adj_arr = [[] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj_arr[a].append(b)
    adj_arr[b].append(a)


def bfs():
    q = deque()
    q.append([1, 0]) # depth

    p = set()
    while q:
        current, depth = q.popleft()

        if depth >= 2:
            continue

        for neighbor in adj_arr[current]:
            p.add(neighbor)
            q.append([neighbor, depth + 1])

    return len(p) - 1 if p else 0

print(bfs())
