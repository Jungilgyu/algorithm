import sys

input = sys.stdin.readline
s = input().strip()

pos = {}
for i, ch in enumerate(s):
    if ch not in pos:
        pos[ch] = [i]
    else:
        pos[ch].append(i)

keys = list(pos.keys())
count = 0

for i in range(len(keys)):
    for j in range(i + 1, len(keys)):
        a1, a2 = pos[keys[i]]
        b1, b2 = pos[keys[j]]
        if (a1 < b1 < a2 < b2) or (b1 < a1 < b2 < a2):
            count += 1

print(count)
