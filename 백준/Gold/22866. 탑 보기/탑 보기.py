import sys
input = sys.stdin.readline

n = int(input())
b = list(map(int, input().split()))

count = [0] * n
near = [0] * n

stack = []
# 왼쪽
for i in range(n):
    while stack and b[stack[-1]] <= b[i]:
        stack.pop()

    if stack:
        count[i] += len(stack)
        near[i] = stack[-1] + 1
    stack.append(i)

# 오른쪽
stack = []
for i in range(n-1, -1, -1):
    while stack and b[stack[-1]] <= b[i]:
        stack.pop()

    if stack:
        count[i] += len(stack)
        if near[i] == 0: # 왼쪽검사 후, 큰게 없어
            near[i] = stack[-1] + 1 # 1-based
        # stack = 인덱스, near는 건불번호( 인덱스 + 1)
        else: # 있으면 거리비교 => 인덱스값 비교
            left = abs(i - (near[i] -1))
            right = abs(i - stack[-1])
            # 기존에 가까운게 있으면, 오른쪽 값과 비교후 더 작으면 갱신
            if right < left or (right == left and stack[-1] + 1 < near[i]):
                near[i] = stack[-1] + 1

    stack.append(i)

for i in range(n):
    if count[i] == 0:
        print(0)
    else:
        print(count[i], near[i])











