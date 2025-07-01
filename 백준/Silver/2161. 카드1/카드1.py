import sys
from collections import deque

n = int(input())
cards = deque()

for i in range(1, n+1):
    cards.append(i)

discard = []
while len(cards) > 1:
    x = cards.popleft()
    y = cards.popleft()

    discard.append(x)
    cards.append(y)

last = cards.popleft()
discard.append(last)
print(*discard)
