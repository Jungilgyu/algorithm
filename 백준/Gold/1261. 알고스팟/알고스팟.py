import sys
import heapq
input = sys.stdin.readline

m, n = map(int, input().split())

area = [list(input().strip()) for _ in range(n)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def sol(si, sj):
    pq = []
    heapq.heappush(pq, (0, si, sj))

    while pq:
        cnt, i, j = heapq.heappop(pq)
        # if i == n-1 and j == m-1:
        #     return cnt

        if cost[i][j] < cnt:
            continue

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < n and 0 <= nj < m:
                if area[ni][nj] == '0':
                    if cnt < cost[ni][nj]:
                        cost[ni][nj] = cnt
                        heapq.heappush(pq, (cnt, ni, nj))
                else:
                    if cnt + 1 < cost[ni][nj]:
                        cost[ni][nj] = cnt + 1
                        heapq.heappush(pq, (cnt+1, ni, nj))

if n == 1 and m == 1:
    print(0)
else:
    cost = [[float('inf')] * m for _ in range(n)]
    sol(0, 0)
    print(cost[n-1][m-1])

