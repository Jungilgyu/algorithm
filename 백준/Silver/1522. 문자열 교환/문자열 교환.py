import sys
input = sys.stdin.readline
s = input().rstrip()

k = s.count('a')
ss = s + s

res = float('inf')
for i in range(len(s)):
    window = ss[i : i + k]
    b = window.count('b')
    res = min(res, b)

print(res)