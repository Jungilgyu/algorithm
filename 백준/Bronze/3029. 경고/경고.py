import sys
input = sys.stdin.readline

c = input().strip()
t = input().strip()


def to_seconds(timestr):
    h, m, s = map(int, timestr.split(":"))
    return h * 3600 + m * 60 + s

def to_timestr(seconds):
    h, mm = divmod(seconds, 3600)
    m, s = divmod(mm, 60)
    return f"{h:02}:{m:02}:{s:02}"

start = to_seconds(c)
end = to_seconds(t)

res = end - start
if res < 0:
    res += 60*60*24
elif res == 0:
    res = 60*60*24

print(to_timestr(res))