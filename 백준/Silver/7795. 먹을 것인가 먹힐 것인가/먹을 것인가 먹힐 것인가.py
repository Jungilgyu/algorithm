import sys

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # 이분탐색 => 일단 정렬이 기본 베이스
    a.sort()
    b.sort()

    ans = 0
    p2 = 0

    for p1 in range(n):
        while p2 < m:
            if a[p1] <= b[p2]:
                break
            p2 += 1

        ans += p2
    print(ans)


















