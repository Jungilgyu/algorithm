import sys
sys.setrecursionlimit(10**6)

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

ans = 0

def dfs(idx, current_sum):
    global ans
    if idx == n:  # 끝까지 다 본 경우
        return

    # 이번 원소 선택
    new_sum = current_sum + arr[idx]
    if new_sum == s:
        ans += 1
    dfs(idx + 1, new_sum)

    # 이번 원소 선택 안 함
    dfs(idx + 1, current_sum)

dfs(0, 0)
print(ans)
