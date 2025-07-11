import sys
input = sys.stdin.readline

n, m = map(int, input().split())
words = dict()
for _ in range(n):
    word = input().rstrip()
    if len(word) >= m:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

sorted_items = sorted(
    words.items(),
    key=lambda x: (-x[1], -len(x[0]), x[0])
)

sorted_dict = dict(sorted_items)
for key in sorted_dict:
    print(key)

