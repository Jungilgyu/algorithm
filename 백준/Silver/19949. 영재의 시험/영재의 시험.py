import sys
sys.setrecursionlimit(10**6)

ans = list(map(int, input().split()))

cnt = 0
def dfs(lst):
    global cnt
    # 종료 조건
    if len(lst) == 10:
        score = 0
        for i in range(10):
            if lst[i] == ans[i]:
                score += 1

        if score >= 5:
            cnt += 1
        return

    for i in range(1, 6):
        if len(lst) >= 2 and lst[-1] == lst[-2] == i:
            continue

        lst.append(i)
        dfs(lst)
        lst.pop()


dfs([])
print(cnt)
