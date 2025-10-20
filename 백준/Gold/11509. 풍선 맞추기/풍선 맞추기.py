import sys
input = sys.stdin.readline


# 11509 풍선맟주기

n = int(input())
ballon = list(map(int, input().split()))

a = [0] * 1000001
ans = 0

for h in ballon:
    if a[h] > 0:
        a[h] -= 1
        a[h-1] += 1

    else:
        ans += 1
        a[h-1] += 1
print(ans)




