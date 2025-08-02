import sys
input = sys.stdin.readline

n = int(input())
stack = []
cnt = 0

for _ in range(n):
    x, y = map(int, input().split())

    while stack and stack[-1] > y:
        stack.pop()
        cnt += 1

    if not stack or stack[-1] < y:
        if y != 0:
            stack.append(y)

# 남아있는 높이 처리
cnt += len(stack)

print(cnt)