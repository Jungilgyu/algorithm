import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split())
    score = [[0] * k for _ in range(n)]
    submit = [0 for _ in range(n)]
    time = [0 for _ in range(n)]

    for i in range(m):
        t_id, q_num, s = map(int, input().split())
        score[t_id-1][q_num-1] = max(score[t_id-1][q_num-1], s)
        submit[t_id-1] += 1
        time[t_id-1] = i

    line = []

    for team_num in range(n):
        line.append([sum(score[team_num]), submit[team_num], time[team_num], team_num])

    line.sort(key=lambda x : (-x[0], x[1], x[2]))

    for rank in range(n):
        if line[rank][3] == t-1:
            print(rank+1)



