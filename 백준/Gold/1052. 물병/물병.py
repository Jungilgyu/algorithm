import sys

n, k = map(int, input().split())

# print(bin(n).count('1'))

ans = 0
while bin(n).count('1') > k:
    low = n & -n
    ans += low
    n += low

print(ans)


