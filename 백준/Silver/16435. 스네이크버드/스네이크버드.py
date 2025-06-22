import sys

N, L = map(int, input().split())
h = list(map(int, input().split()))
h.sort()

res = L
for i in range(N):
    if h[i] <= res:
        res += 1

print(res)

