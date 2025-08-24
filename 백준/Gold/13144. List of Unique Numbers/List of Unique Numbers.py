import sys
from collections import deque

n = int(input())
lst = list(map(int, input().split()))

seen = [0] * (max(lst) + 1)
ans = 0
start, end = 0, 0

while start < n:
    while end < n and not seen[lst[end]]:
        seen[lst[end]] = 1
        end += 1

    ans += (end - start)
    seen[lst[start]] = 0
    start += 1

print(ans)