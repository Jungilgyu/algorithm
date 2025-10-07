import sys
from collections import deque
input = sys.stdin.readline

f = input().strip()

ucpc = deque(['U', 'C', 'P', 'C'])

for i in range(len(f)):
    if len(ucpc) == 0:
        break
        
    if f[i] == 'U' and ucpc[0] == 'U':
        ucpc.popleft()
    elif f[i] == 'C' and ucpc[0] == 'C':
        ucpc.popleft()

    elif f[i] == 'P' and ucpc[0] == 'P':
        ucpc.popleft()

if len(ucpc) == 0:
    print("I love UCPC")
else:
    print("I hate UCPC")
