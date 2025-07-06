import sys

n = int(input())
heights = list(map(int, input().split()))
stack = []
answer = [0] * n

for i in range(n):
    while stack and stack[-1][1] < heights[i]:
        stack.pop()

    if stack:
        answer[i] = stack[-1][0] + 1
    else:
        answer[i] = 0

    stack.append((i, heights[i]))

print(*answer)









