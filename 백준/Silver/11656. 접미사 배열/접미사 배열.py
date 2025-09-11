import sys
input = sys.stdin.readline

s = input().strip()

ans = []
for i in range(len(s)):
    temp = s[i:]
    ans.append(temp)
    
ans.sort()
for w in ans:
    print(w)







