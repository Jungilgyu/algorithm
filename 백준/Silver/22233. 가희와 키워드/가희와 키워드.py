import sys
input = sys.stdin.readline

n, m = map(int, input().split())
keywords = set(input().strip() for _ in range(n))

for _ in range(m):
    words = input().strip().split(',')
    for w in words:
        keywords.discard(w)
    print(len(keywords))

