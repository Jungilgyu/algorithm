import sys
input = sys.stdin.readline
s = input().rstrip()

#1은 앞부터, 0은 뒤부터
one_cnt = 0
zero_cnt = 0

for i in range(len(s)):
    if s[i] == "0":
        zero_cnt += 1
    else:
        one_cnt += 1

one_cnt = one_cnt // 2
zero_cnt = zero_cnt //2

front = []
for ch in s:
    if ch == "1" and one_cnt > 0:
        one_cnt -= 1
    else:
        front.append(ch)
res = []
for ch in reversed(front):
    if ch == "0" and zero_cnt > 0:
        zero_cnt -= 1
    else:
        res.append(ch)

print(''.join(reversed(res)))

