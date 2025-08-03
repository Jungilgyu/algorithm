import sys
sys.setrecursionlimit(10**6)

n = int(input())
egg = [list(map(int, input().split())) for _ in range(n)]

ans = 0
def dfs(idx):
    global ans

    if idx == n:
        broken = sum(1 for d, _ in egg if d <= 0)
        ans = max(ans, broken)
        return

    if egg[idx][0] <= 0:
        dfs(idx + 1)
        return

    did_hit = False
    for i in range(n):
        if i == idx or egg[i][0] <= 0:
            continue

        did_hit = True

        cur_d, target_d = egg[idx][0], egg[i][0]

        egg[idx][0] -= egg[i][1]
        egg[i][0] -= egg[idx][1]

        dfs(idx+1)

        egg[idx][0], egg[i][0] = cur_d, target_d

    if not did_hit:
        dfs(idx+1)

dfs(0)
print(ans)

