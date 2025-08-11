import sys
input = sys.stdin.readline
n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]

sushi = sushi + sushi

ans = 0
start = 0
end = k

first = set()
for i in range(start, end):
    first.add(sushi[i])
first.add(c)

ans = max(ans, len(first))

start += 1
end += 1

while True:
    if start == n:
        break
    temp = sushi[start:end]
    eat = set(temp)

    eat.add(c)
    ans = max(ans, len(eat))

    start += 1
    end += 1

print(ans)

