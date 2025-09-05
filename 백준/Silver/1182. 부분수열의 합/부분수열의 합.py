import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
used = []
def sol(lst, idx):
    global ans
    # 최대길이
    if len(lst) == n:
        if sum(lst) == s:
            ans += 1
        return

    # 중간에 만족
    if len(lst) > 0 and sum(lst) == s:
        ans += 1

    for i in range(idx, n):
        lst.append(arr[i])
        sol(lst, i+1)
        lst.pop()

sol([], 0)
print(ans)



















