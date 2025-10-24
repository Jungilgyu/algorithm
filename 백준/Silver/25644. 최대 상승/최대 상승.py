import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

temp = arr[0]
max_v = 0

for i in range(1, n):
    if arr[i] < temp:
        temp = arr[i]
# 2 9 4 1 1
    elif arr[i] > temp:
        max_v = max(max_v, arr[i] - temp)


print(max_v)



