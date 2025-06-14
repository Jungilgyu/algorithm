import sys

n = int(input())
arr = list(map(int, input().split()))
res = [0] * n

# res = [0, 0, 0, 0]
for i in range(n):
    cnt = 0
    for j in range(n):
        if res[j] == 0:
            cnt += 1
        if cnt == arr[i]+1:
            res[j] = i+1
            break
print(*res)