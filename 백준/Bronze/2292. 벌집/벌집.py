import sys
n = int(input())

cnt = 1    
last = 1    

while n > last:
    last += 6 * cnt   #
    cnt += 1

print(cnt)

