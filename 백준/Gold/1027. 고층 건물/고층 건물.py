import sys

n = int(input())
b = list(map(int, input().split()))

ans = 0
for i in range(n):
    temp = b[i]

    cnt = 0
    # 왼쪽
    left = float('inf')
    for j in range(i-1, -1, -1):
        diff = (b[j] - b[i]) / (j - i)
        if diff < left:
            cnt += 1
            left = diff

    # 오른쪽
    right = float('-inf')
    for j in range(i+1, n):
        diff = (b[j] - b[i]) / (j - i)
        if diff > right:
            cnt += 1
            right = diff

    ans = max(cnt, ans)
print(ans)