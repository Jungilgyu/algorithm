import sys
input = sys.stdin.readline

s = input().strip()
base = [-1] * 26

for i in range(len(s)):
    # 처음등장
    if base[ord(s[i]) - ord('a')] == -1:
        base[ord(s[i]) - ord('a')] = i

print(*base)


