import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [0] * (n+1)

for i in range(n):
    prefix[i+1] = prefix[i] + arr[i]


start = 0
end = 1

cnt = 0
while start <= n and end <= n:

    temp = prefix[end] - prefix[start] # start+1부터 end까지의 합

    if temp > m:
        start += 1
        if start == end:
            end += 1
    elif temp < m:
        end += 1
    else:
        cnt += 1
        end += 1
print(cnt)



