import sys

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
ans = 0

for i in range(n):
    temp = arr[i]

    start = 0
    end = n-1

    while start < end:

        # start, end 가 i(현재나)와 같으면 한칸씩 이동
        if start == i:
            start += 1
        elif end == i:
            end -= 1
        # 여기서 한번 더 검증
        if end <= start:
            continue

        total = arr[start] + arr[end]

        if total == temp:
            ans += 1
            break
        elif total > temp:
            end -= 1
        else:
            start += 1


print(ans)

# 0 1 2 3 4 5 6 7