import sys
input = sys.stdin.readline


word = input().strip()

count = [0] * 26

for char in word:
    temp = ''
    if char.islower():
        temp = char.upper()
    else:
        temp = char
    count[ord(temp) - ord('A')] += 1

max_v = max(count)
res = []
for i in range(26):
    if count[i] == max_v:
        res.append(i)

if len(res) >= 2:
    print('?')
else:
    print(chr(res[0] + 65))
