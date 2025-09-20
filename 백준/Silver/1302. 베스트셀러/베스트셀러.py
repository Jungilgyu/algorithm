import sys
input = sys.stdin.readline

n = int(input())

count = dict()

for _ in range(n):
    book = input().strip()
    if book not in count:
        count[book] = 1
    else:
        count[book] += 1

ans = []
max_key = max(count, key=count.get)
max_val = count[max_key]
for key, value in count.items():
    if value == max_val:
        ans.append(key)
ans.sort()
print(ans[0])

