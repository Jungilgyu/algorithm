import sys

n = int(input())
m = int(input())
lamp = list(map(int, input().split()))

def check(lamp, mid):
    if mid - lamp[0] < 0:
        return False
    for i in range(1, m):
        if lamp[i] - lamp[i-1] > 2 * mid:
            return False
    if n - lamp[-1] > mid:
        return False

    return True

# 가로등의 최소 높이
left = 1
right = n
ans = 0
while left <= right:
    mid = (left + right) // 2

    if check(lamp, mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)