import sys
input = sys.stdin.readline

start = input().strip()
cnt = 0

while len(start) > 1:  
    cnt += 1
    start = str(sum(map(int, start))) 

print(cnt)
if int(start) % 3 == 0:
    print("YES")
else:
    print("NO")
