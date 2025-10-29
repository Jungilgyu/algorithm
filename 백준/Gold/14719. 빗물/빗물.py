import sys
input = sys.stdin.readline

h, w = map(int, input().split())
heights = list(map(int, input().split()))

ans = 0

for i in range(1, w-1):
    left = max(heights[:i])
    right = max(heights[i+1:])

    s = min(left, right)
    if heights[i] <= s:
        ans += s - heights[i]

print(ans)