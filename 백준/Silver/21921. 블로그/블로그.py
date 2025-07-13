import sys
input = sys.stdin.readline

n, x = map(int, input().split())
cnt = list(map(int, input().split()))

window_sum = sum(cnt[:x])
max_sum = window_sum
ans = 1

for i in range(x, n):
    window_sum += cnt[i] - cnt[i-x] # 맨뒤에 하나 더하고, 맨앞을 뺌

    if window_sum > max_sum:
        max_sum = window_sum
        ans = 1
    elif window_sum == max_sum:
        ans += 1

if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(ans)