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

visited = [False] * (n+1)
visited[1] = True
ans = 0

for neighbor in adj_arr[1]:
    if not visited[neighbor]:
        visited[neighbor] = True
        ans += 1

    for nneighbor in adj_arr[neighbor]:
        if not visited[nneighbor]:
            visited[nneighbor] = True
            ans += 1
print(ans)
