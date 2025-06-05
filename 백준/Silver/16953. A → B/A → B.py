import sys
from collections import deque

s, e = map(int, input().split())

q = deque()
q.append([s, 0])

ans = -1
while True:
    if len(q) == 0:
        break
    num, cnt = q.popleft()
    if num == e:
        ans = cnt + 1
        break

    for next_num in (num*2, num*10 + 1):
        if next_num <= 1000000000:
            q.append([next_num, cnt + 1])

print(ans)