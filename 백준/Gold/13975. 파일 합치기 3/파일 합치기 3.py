import sys
import heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    files = list(map(int, input().split()))
    heapq.heapify(files)

    ans = 0
    temp = 0
    cnt = 0
    while files:
        x = heapq.heappop(files)
        temp += x
        cnt += 1
        if cnt == 2:
            ans += temp
            heapq.heappush(files, temp)
            temp = 0
            cnt = 0

    print(ans)