import sys
from collections import deque

s = input()
t = input()

q = deque()
q.append(t)

is_find = False
while q:
    char = q.popleft()
    if char == s:
        is_find = True
        break
    if len(char) <= len(s):
        continue
    if char[-1] == 'A':
        q.append(char[:-1])
    if char[-1] == 'B':
        q.append(char[:-1][::-1])

print(1 if is_find else 0)
