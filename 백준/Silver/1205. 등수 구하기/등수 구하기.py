import sys
n, s, p = map(int, input().split())

try:
    score_lst = list(map(int, input().split()))
except EOFError:
    score_lst = []

# 첫 점수일 경우 무조건 1등
if not score_lst:
    print(1)
else:
    score_lst.append(s)
    score_lst.sort(reverse=True)

    # 내가 몇 번째 등수인지 (1-based)
    rank = 1
    for i in range(len(score_lst)):
        if score_lst[i] > s:
            rank += 1
        else:
            break

    # p등까지 안에 못 들어가면 탈락
    if rank > p:
        print(-1)
    else:
        # 랭킹이 꽉 찼는데, s점이 여러 개이고,
        # s가 끝에 위치한 동점자라면 탈락할 수도 있으므로 조심
        count_same = score_lst.count(s)
        idx = score_lst.index(s)

        # 같은 점수들이 끝까지 밀려서 p 초과로 나갈 수 있으면 탈락
        if len(score_lst) > p and idx + count_same > p:
            print(-1)
        else:
            print(rank)
