import sys

T = int(input())
for _ in range(T):
    n = int(input())
    score = list(map(int, input().split()))
    valid = dict()
    for num in score:
        if num in valid:
            valid[num] += 1
        else:
            valid[num] = 1

    valid_team = [] # 유효한 팀
    for num in valid:
        if valid[num] == 6:
            valid_team.append(num)

    cnt = max(score)  # 참가한 팀 수
    team_cnt = [[] for _ in range(cnt + 1)]

    s = 1
    for i in range(n):
        if score[i] in valid_team:
            team_cnt[score[i]].append(s)
            s += 1
    # for x in team_cnt:
    #     print(x)
    winner = 0
    winner_team = []
    min_v = float('inf')

    for i in range(len(team_cnt)):
        if len(team_cnt[i]) < 6:
            continue
        if sum(team_cnt[i][:4]) < min_v:
            winner = i
            winner_team = team_cnt[i]
            min_v = sum(team_cnt[i][:4])
        elif sum(team_cnt[i][:4]) == min_v:
            if team_cnt[i][4] < winner_team[4]:
                winner = i
                winner_team = team_cnt[i]
                min_v = sum(team_cnt[i][:4])
    # print(winner_team)
    print(winner)
