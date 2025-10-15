import sys
input = sys.stdin.readline

s = input().strip()

def check(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

ans = 0
flag = False # 중간에 팰린드롬이 있는지
for i in range(len(s) - 1):
    if check(s[i:]):
       ans += i
       flag = True
       break

if flag:
    print(len(s) + ans)
else:
    print(len(s) * 2 - 1)



