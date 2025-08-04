import sys

n = int(input())
seq = list(map(int, input().split()))

stack = []
ans = [-1] * n
for i in range(n-1, -1, -1):
    while stack and stack[-1] <= seq[i]:
        stack.pop()

    if stack:
        ans[i] = stack[-1]
    stack.append(seq[i])

print(*ans)

