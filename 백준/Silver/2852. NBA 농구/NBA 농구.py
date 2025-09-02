import sys
input = sys.stdin.readline

n = int(input())
infos = list(input().split() for _ in range(n))

def to_seconds(timestr: str) -> int:
    m, s = map(int, timestr.split(":"))
    return m * 60 + s

def to_timestr(seconds: int) -> str:
    m, s = divmod(seconds, 60)
    return f"{m:02}:{s:02}"

score1, score2 = 0, 0
time1, time2 = 0, 0
prev_time = 0

for team, t in infos:
    cur_time = to_seconds(t)

    if score1 > score2:
        time1 += cur_time - prev_time
    elif score2 > score1:
        time2 += cur_time - prev_time

    if team == '1':
        score1 += 1
    else:
        score2 += 1

    prev_time = cur_time

end_time = to_seconds("48:00")
if score1 > score2:
    time1 += end_time - prev_time
elif score2 > score1:
    time2 += end_time - prev_time

print(to_timestr(time1))
print(to_timestr(time2))