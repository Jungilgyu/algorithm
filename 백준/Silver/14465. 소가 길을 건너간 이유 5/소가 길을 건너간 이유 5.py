import sys
input = sys.stdin.readline

n, k, b = map(int, input().split())
broken = [int(input()) for _ in range(b)]

s = [True] * (n+1)
for num in broken:
    s[num] = False


# 1 2 3 4 5 6 7 8 9 10
# x x o o x o o o x x
#
# [0, 0, 1, 2, 2, 3, 4, 5, 5, 5]

pre_sum = [0] * (n+1)
for i in range(1, n+1):
    if s[i]:
        pre_sum[i] = pre_sum[i-1] + 1
    else:
        pre_sum[i] = pre_sum[i-1]

ans = float('inf')
for i in range(1, n - k + 2):
    front = i
    end = i + k - 1
    cnt = k - (pre_sum[end] - pre_sum[front-1])
    ans = min(ans, cnt)

print(ans)