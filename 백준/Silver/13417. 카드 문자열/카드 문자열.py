import sys
from collections import deque


T = int(input())
for _ in range(T):
    n = int(input())
    cards = list(input().split())

    q = deque()
    q.append(cards[0])

    for c in cards[1:]:
        if c <= q[0]:
            q.appendleft(c)
        else:
            q.append(c)

    print(''.join(q))