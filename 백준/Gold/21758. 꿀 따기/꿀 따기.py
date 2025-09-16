import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

ans = 0
# 왼쪽 누적합
psum = [0] * n
psum[0] =  arr[0]
for i in range(1, n):
    psum[i] = psum[i-1] + arr[i]

# 오른쪽 누적합
psum2 = [0] * n
psum2[n-1] = arr[n-1]
for i in range(n-2, -1, -1):
    psum2[i] = psum2[i+1] + arr[i]


# 1. 벌통 맨 오른쪽, a는 맨왼쪽 고정
ans = 0
for i in range(1, n-1):
    bee1 = psum[n-1] - arr[0] - arr[i]
    bee2 = psum[n-1] - psum[i]
    temp = bee1 + bee2

    ans = max(ans, temp)

# 2. 벌통 맨 왼쪽 고정
for i in range(n-2, 0, -1):
    bee1 = psum2[0] - arr[n-1] - arr[i]
    bee2 = psum2[0] - psum2[i]
    temp = bee1 + bee2
    ans = max(ans, temp)

# 3. 벌통 중간
for i in range(1, n-1):
    bee1 = psum[i] - arr[0]
    bee2 = psum2[i] - arr[n-1]

    temp = bee1 + bee2
    ans = max(ans, temp)

print(ans)


