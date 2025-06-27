import sys
input = sys.stdin.readline

n, c = map(int, input().split())

location = [int(input()) for _ in range(n)]

location.sort()

start = 1
end = max(location) - min(location)

def isPossible(mid):

    temp = location[0]
    cnt = 1
    for i in range(1, n):
        if location[i] - temp >= mid:
            cnt += 1
            temp = location[i]
    if cnt >= c:
        return True
    return False


ans = 0

while start <= end:
    mid = (start + end) // 2
    if isPossible(mid):
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)


