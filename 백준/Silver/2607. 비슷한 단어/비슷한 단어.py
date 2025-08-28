import sys
input = sys.stdin.readline

n = int(input())
words = [list(input().strip()) for _ in range(n)]

base = [0] * 26
for ch in words[0]:
    base[ord(ch) - ord('A')] += 1

ans = 0
for i in range(1, n):
    temp = words[i]

    temp_cnt = [0] * 26
    for ch in temp:
        temp_cnt[ord(ch) - ord('A')] += 1


    diff = 0
    for j in range(26):
        diff += abs(base[j] - temp_cnt[j])

    if abs(len(words[0]) - len(temp)) > 1:
        continue

    if diff == 0 or diff == 1 or diff == 2:
        ans += 1
print(ans)