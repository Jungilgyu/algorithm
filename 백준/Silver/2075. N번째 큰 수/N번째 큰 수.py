import sys
import heapq

n = int(input())

pq = []

for _ in range(n):
    nums = list(map(int, input().split()))
    for num in nums:
        if len(pq) < n:
            heapq.heappush(pq, num)
        else:
            if num > pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, num)

print(pq[0])




