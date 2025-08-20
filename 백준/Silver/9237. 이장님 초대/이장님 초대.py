import sys

n = int(input())
tree = list(map(int, input().split()))

tree.sort(reverse=True)

ans = 0
for i in range(n):
    ans = max(ans, i+1+tree[i])

print(ans+1)
