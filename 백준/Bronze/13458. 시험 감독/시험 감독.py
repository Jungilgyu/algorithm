import sys
import math
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

ans = 0
for place in a:
    place -= b # 총 감독관 할당
    ans += 1

    if place <= 0:
        continue
    else:
        ans += math.ceil(place/c)

print(ans)


