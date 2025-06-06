import sys
n = int(input())
weights = list(map(int, input().split()))
weights.sort()


target = 1

for i in range(n):
    if weights[i] <= target:
        target += weights[i]
    else:
        break
print(target)

