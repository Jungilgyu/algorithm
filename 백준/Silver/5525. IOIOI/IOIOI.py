import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = list(input())
# print(s)

p = ['I'] + ['O', 'I'] * n
# 시작
start = 0
end = start + 2*n

ans = 0
temp = s[start:end+1]
if temp == p:
    ans += 1
# print(ans)
for i in range(2*n+1, m):
    temp.pop(0)
    temp.append(s[i])
    if temp == p:
        ans += 1

print(ans)

