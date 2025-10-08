import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

def sol(lst):
    res = 0
    for i in range(len(lst) - 1):
        res += abs(lst[i] - lst[i+1])
    return res

ans = 0

cases = permutations(arr, n)
for case in cases:
    ans = max(ans, sol(case))

print(ans)


