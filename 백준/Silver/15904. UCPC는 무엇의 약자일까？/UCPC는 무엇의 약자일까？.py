import sys
input = sys.stdin.readline
s = input().strip()
target = "UCPC"
idx = 0

for ch in s:
    if ch == target[idx]:
        idx += 1
        if idx == len(target):
            break

if idx == len(target):
    print("I love UCPC")
else:
    print("I hate UCPC")