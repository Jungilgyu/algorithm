import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
card = list(map(int, input().split()))
heapq.heapify(card)

ans = 0
for _ in range(m):
    c1 = heapq.heappop(card)
    c2 = heapq.heappop(card)
    c_sum = c1 + c2
    heapq.heappush(card, c_sum)
    heapq.heappush(card, c_sum)


print(sum(card))